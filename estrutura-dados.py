# Estrutura de dados em Python

# LISTAS (ordenada e mutaveis)

frutas = ["maça", "banana", "laranja"]

print("Primeira fruta: ", frutas[0])

# Adicionar elementos - append
frutas.append("uva")

# Remover elementos - remove

frutas.remove("banana")

# iterar a lista

for fruta in frutas:
  print("Frutas: ", fruta)


# TUPLAS (ordenada e imutáveis)

cores = ("vermelho", "verde", "azul")
print("Segunda cor da tupla: ", cores[1])

# CONJUNTOS (nao ordenada e sem elementos duplicados)

numeros = {1, 2, 3, 4, 5}

numeros.add(6)
numeros.remove(3)

pares = {2, 4, 6}

# Operadores de conjuntos
print("Uniao: ", numeros.union(pares))
print("Intercessão: ", numeros.intersection(pares))

# DICIONÁRIOS (colecao nao ordenada de de pares chave-valor)

aluno = {"nome": "Mateus", "idade": 27, "curso": "ADS"}

print("Nome do aluno no dicionario: ", aluno["nome"])

# adicionando valor
aluno["nota"] = 9.5

# remover par chave-valor
del aluno["idade"]

for chave, valor in aluno.items():
  print("Chave valor dic: ", chave, valor)


# List Comprehensions (forma concisa de criar listas)

quadrados = [x**2 for x in range(10)]
print("Lista de quadrados de 0 a 10: ", quadrados)

pares = [x for x in range(10) if x % 2 == 0]
print("Lista de pares de 0 a 10: ", pares)

# Exemplo 1: contagem de frequência
texto = "Python é incrível"
frequencia = {}

for char in texto:
  if char in frequencia:
    frequencia[char] += 1
  else:
    frequencia[char] = 1

print("Frequência de caracteres no texto: ", frequencia)

# Exemplo 2: Remover Duplicados
numeros = [1, 2, 2, 3, 4, 4, 5]
unicos = list(set(numeros))
print("Lista sem duplicados: ", unicos)

