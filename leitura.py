import json

with open("anotacao.json", "r") as arquivo:
    dados = json.load(arquivo)

print("Título: ",dados["titulo"])
print("Conteúdo",dados['conteudo'])