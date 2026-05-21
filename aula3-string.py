# Aula 2
# Strings

# Contagem de caracteres len(<variavel>)

frase = "Porto Alegre é uma cidade localizada no Rio Grande do Sul"

print(f"A frase '{frase}' possui {len(frase)} letras")

# Contagem de caracter específico .count("<caracter>")

frase = "Porto Alegre é uma cidade localizada no Rio Grande do Sul"

print(f"A frase '{frase}' possui {frase.count("a")} letras 'a'")

#  Substituição de elementos .replace("<string>")

frase = "Porto Alegre é uma cidade localizada no Rio Grande do Sul"

nova_frase = frase.replace("Porto Alegre", "Curitiba")

print(nova_frase)

#  Identificando posição de caracter .find("<caracter>")

frase = "Porto Alegre é uma cidade localizada no Rio Grande do Sul"

print(f"A letra 'c' está na posição {frase.find("c")}")

#  Limitando o tamanho da frase variavel[posicao_inicial:posicao_final]

frase = "Porto Alegre é uma cidade localizada no Rio Grande do Sul"

print(frase[0:12])

# String em laço for

frase = "Porto Alegre é uma cidade localizada no Rio Grande do Sul"

for letra in frase:
  print(letra, end='\t')


# Separar as strings .split("<string>")

frase = "Porto Alegre é uma cidade localizada no Rio Grande do Sul"

print("Frase com split", frase.split(" "))

# Operadores Logicos com String

frase = "Porto Alegre é uma cidade localizada no Rio Grande do Sul"

if "Porto" in frase:
  print("Sim")

# Alterando maiúsculas e minúsculas

alerta = "Risco de Morte"

print(alerta.upper())
print(alerta.lower())

# Converter tipos

num = 12345
print(type(num))
string_num = str(num)
print(type(string_num))

# Exemplo calculadora IMC
# peso = input("Digite seu peso em kg: ")
# peso = float(peso.replace(",", "."))
# altura = float(input("Digite a sua altura em m: ").replace(",", "."))
# imc = str(round(peso/(altura**2), 2)).replace(".", ",")

# print(f"Seu IMC é: {imc}")

# Strip - remover espaços desnecessários

frase = "   Análise e Desenvolvimento De Sistemas     "
print("Frase sem strip: ", frase)
print("Frase com strip: ", frase.strip())

# Formatação de strings

frase = "Porto Alegre é uma cidade localizada no Rio Grande do Sul"
print(frase.center(70)) # centralizar a mensagem em um espaço
print(frase.center(100, "="))
print(frase.rjust(70)) # ajustar para esquerda
print(frase.ljust(70)) # ajustar prar direita
