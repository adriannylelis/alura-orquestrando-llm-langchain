# Orquestrando LLMs com LangChain

Projeto desenvolvido durante o curso "Orquestrando LLMs com LangChain" da Alura.

Descrição
---------
Este repositório contém artefatos e um pequeno projeto-exemplo criado enquanto eu acompanhava o curso da Alura sobre orquestração de LLMs com LangChain. O objetivo deste projeto é servir como base para experimentar modelos, pipelines e integrações com ferramentas externas (por exemplo, armazenamento de embeddings, ferramentas de extração, etc.).

Curso de referência
-------------------
Curso: https://www.alura.com.br/curso-online-python-gemini-orquestrando-llms-langchain

Contrato (curto)
- Entrada: prompts e dados em `dados/` (opcional).
- Saída: respostas geradas pelo(s) modelo(s), pipelines e artefatos registrados localmente.
- Erros: falta de chaves/API, dependências não instaladas.

Pré-requisitos
--------------
- Python 3.10+ (recomendado)
- Conta e chave(s) de API do provider de LLM que você pretende usar (ex.: OpenAI, Google Gemini, etc.).

Instalação rápida
-----------------
1. Crie e ative um ambiente virtual (opcional, recomendado):

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows (bash.exe)
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

Configuração de chaves
----------------------
As credenciais e chaves do projeto devem ser mantidas fora do código-fonte. Este repositório contém arquivos auxiliares:

- `my_keys.py` — local para armazenar chaves localmente durante desenvolvimento (NÃO comitar chaves reais).
- `my_models.py` — configurações locais de modelos e mapeamentos.

Recomendações:
- Use variáveis de ambiente (ex.: `export OPENAI_API_KEY=...'` ou `setx` no Windows) em vez de commitar chaves.
- Se usar `my_keys.py`, garanta que está no `.gitignore`.

Estrutura do repositório
------------------------
- `my_helper.py`  — utilitários e helpers do projeto.
- `my_keys.py`    — arquivo local para chaves (dev apenas).
- `my_models.py`  — definição e configurações de modelo.
- `requirements.txt` — dependências do Python.
- `dados/`        — pasta para armazenar datasets ou arquivos usados pelos exemplos.

Como usar (exemplo rápido)
--------------------------
1. Configure suas chaves (variáveis de ambiente ou `my_keys.py`).
2. Abra um REPL Python ou crie um script que importe os módulos do projeto. Exemplo mínimo:

```python
from my_helper import alguma_funcao

resp = alguma_funcao("Escreva um resumo sobre LangChain em 3 linhas")
print(resp)
```

Notas e boas práticas
---------------------
- Nunca versionar chaves de API.
- Para experimentos com modelos grandes, monitore custo e latência.
- Separe arquivos de configuração (por exemplo, `my_models.py`) para facilitar troca de modelos.

Contribuição
------------
Pull requests são bem-vindos. Para mudanças maiores, abra uma issue descrevendo a proposta antes de implementar.

Licença
-------
Escolha e adicione uma licença se quiser tornar o projeto público (ex.: MIT). Atualmente não há licença explícita neste repositório.


-------
Para dúvidas ou colaborações, abra uma issue neste repositório.


