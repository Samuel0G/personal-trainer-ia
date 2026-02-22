import json

def salvar(dados):
    with open("memoria.json", "w") as f:
        json.dump(dados, f, indent=4)


def carregar_progresso():
    try:
        with open("memoria.json", "r") as f:
            return json.load(f)
    except:
        return {}
