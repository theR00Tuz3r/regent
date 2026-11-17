# Regent

**Regent** (REsearch aGENT) is a basic AI-powered research tool that uses a locally running Ollama model to research topics and generate structured responses.

It can search the web using DuckDuckGo, retrieve information from Wikipedia, and save research results to a text file.

## Features

- Uses a local LLM through [Ollama](https://ollama.com/).
- Searches the web with DuckDuckGo.
- Retrieves information from Wikipedia.
- Generates structured research responses containing a topic, summary, sources, and tools used.
- Saves research output to `research_output.txt`.

## Requirements

- Python 3.10 or newer
- [Ollama](https://ollama.com/) installed and running
- an ollama model (defult is llama3.1:8b)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/theR00Tuz3r/regent.git
   cd regent
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows:

   ```powershell
   .venv\Scripts\activate
   ```

3. Install the Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the Ollama model:

   ```bash
   ollama pull llama3.1:8b
   ```

5. Make sure Ollama is running before starting Regent.

## Usage

Run the application from the project directory:

```bash
python main.py
```

Enter a research question when prompted. Regent will use its available tools and print a structured response.

Research output can also be saved through the agent's file-saving tool. By default, saved results are appended to `research_output.txt`.

## Project Structure

```text
regent/
├── main.py
├── tools.py
├── requirements.txt
├── README.md
└── LICENSE
```

- `main.py` — Initializes the Ollama model, research agent, and response structuring.
- `tools.py` — Defines the DuckDuckGo search, Wikipedia, and text-saving tools.
- `requirements.txt` — Lists the Python dependencies.
- `LICENSE` — MIT License.

## Configuration

The default model is configured in `main.py`:

```python
llm = ChatOllama(model="llama3.1:8b", temperature=0)
```

Change the model name to use another model that is available in your Ollama installation.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Repository

[https://github.com/theR00Tuz3r/regent](https://github.com/theR00Tuz3r/regent)
