import json

print("Bem vindo(a) à área de anotações!")
anotacao = {
    "titulo": input("Digite o título da anotação: "),
    "conteudo": input("Agora, digite o conteúdo da anotação: "),
}
with open("anotacao.json", "w") as arquivo:
    json.dump(anotacao, arquivo, indent=4)  