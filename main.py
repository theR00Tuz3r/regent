from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools: list[str]


llm = ChatOllama(model="llama3.1:8b", temperature=0)

# Step 1: the agent researches and answers in plain text (no JSON required)
agent_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a research assistant that helps generate a research paper. "
            "Use the available tools as needed, then give a clear answer and "
            "mention which sources you used.",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(llm=llm, prompt=agent_prompt, tools=tools)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True,
)

# Step 2: a separate call converts the answer into the structured schema
structure_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Convert the research answer into the requested structure. "
            "Only use information present in the answer and tool list.",
        ),
        (
            "human",
            "Question: {query}\n\nAnswer: {answer}\n\nTools used: {tools_used}",
        ),
    ]
)
structurer = structure_prompt | llm.with_structured_output(ResearchResponse)

query = input("What can I help you research? ")
raw_response = agent_executor.invoke({"query": query})

try:
    output = raw_response["output"]
    # Some providers return a list of blocks instead of a string
    if isinstance(output, list):
        output = output[0]["text"]

    tools_used = sorted({step[0].tool for step in raw_response["intermediate_steps"]})

    structured_response = structurer.invoke(
        {
            "query": query,
            "answer": output,
            "tools_used": ", ".join(tools_used) or "none",
        }
    )
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)