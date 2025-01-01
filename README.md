# AgenticAI

## Local Installation
### Setting Up Environment
```
conda create -n AgenticAI python==3.12
conda activate AgenticAI
```
### Ollama installation
```
pip install ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3.2
```
Ref: [Ollama](https://github.com/ollama/ollama)

### Running LLM on local machine
```
python 1_ollama_local.py
```

## Phidata
Ref: [Phidata](https://www.phidata.com/)
```
pip install phidata duckduckgo-search newspaper4k lxml_html_clean yfinance
```
### Olama and Phidata
```
python 2_phi_llm.py
```
### Financial Agent
```
python 3_fin_agent.py
```
### Adding Tool
```
python 4_get_company_symbol_tool.py 
```
### Agentic Workflow
```
python 5_Agentic_Workflow.py 
```
