import json
import os

ARQUIVO_DADOS = "tasks.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)