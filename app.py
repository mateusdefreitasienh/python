# Primeiro codigo em Python

print('Olá mundo')

# Input
idade = input("Informe sua idade: ")

idade = int(idade)

# Print
print("A idade digitada é:", idade)
print(f"A idade digitada é: {idade}")

# Estrutura condicional

if int(idade) > 0:
  print("Idade válida")
else:
  print("Idade inválida")

a = True
b = False

if a and b:
  print("Falso")
elif a or b:
  print("Verdadeiro")

# Laço de repetição (for)

print("Laço for basico")
for i in range(int(idade)):
  print(f"Item {i} da lista")

print("Laço for 'controlado'")
for i in range(2, int(idade)):
  print(f"Item {i} da lista")

print("Laço for 'controlado' e com iteracao diferente")
for i in range(3, int(idade), 3):
  print(f"Item {i} da lista")

# Comando break
chave = 6

for i in range(10):
  print(i)
  if i == chave:
    print(f"Valor da {chave} encontrado")
    break

# Laço de repetição (do)

while idade < 20:
  print("Idade válida")
  idade += 1

contador = 0
while contador < 12:
  if contador % 2 == 0:
    contador += contador
  contador += 1
  print(contador)


# Arredondamento

import math

resultado = math.sqrt(13)
print("Resultado sem arredondamento:", resultado)
print(f"Resultado com arredondamento usando formatação: {resultado:.2f}")
print("Resultado com arredondamento usando round:", round(resultado, 2))


 git config --global user.email "you@example.com"
  git config --global user.name "Your Name"