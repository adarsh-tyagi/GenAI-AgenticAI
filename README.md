# This repository consist my learning of various genai topics

- Langchain
- LangGraph
- MCP
- RAG (Retrieval Augumented Generation)
- Vectorless RAG
- Deep Agents


<b> NOTE: We will be using different API keys to use the resources. Generate these free API keys and store in .env file with these values to use in your code.</b>
- GROQ - model use
- GEMINI - model use
- TAVILY SEARCH - agentic browser
- PAGEINDEX - vectorless rag

### Code Setup
We are using `uv` package and project manager here.
1. Create folder and inside the folder run `uv init` and this will create basic scaffolding.
2. Now create the virtual env by running `uv venv`
3. Then activate it by running `.venv\Scripts\activate`
4. Then create other necessary file like requirements.txt and .env file
5. To install the requirements use `uv add -r requirements.txt` command

### To setup env as notebook kernel, sometimes we need to sync the environment
If ipykernel is already installed, the missing step is usually registering the environment as a Jupyter kernel. Installing the package alone does not make the env appear in the kernel picker.

- `uv run python -m ipykernel install --user --name my-uv-env --display-name "Python (my-uv-env)"` - That creates a Jupyter kernel spec pointing to your uv environment, which is what Jupyter actually lists.
- `jupyter kernelspec list` - to verify if it exists

<b>After registering, fully restart VS Code or the Jupyter app, then reopen the notebook and choose the new kernel name from the selector</b>