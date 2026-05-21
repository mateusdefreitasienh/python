# Exercício String

dados = " nome: LUIZ ; cidade: Porto Alegre ; idade: 20 "

dados = dados.replace(";", ",")
lista_dados = dados.split(",")

for i, item in enumerate(lista_dados):
  lista_dados[i] = lista_dados[i].strip()

print(lista_dados)