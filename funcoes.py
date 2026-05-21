# Funções

# Sintaxe
def nome_da_funcao(parametros):
  "corpo da funcao"

# Funcao sem parametro
def exibe_mensagem():
  print("Seja bem vindo")

exibe_mensagem()

# Funcao com retorno
def exibe_mensagem():
  return "Seja bem vindo"

print(exibe_mensagem())

# Função sem ação (pass)
def funcao():
  pass

var1 = funcao()
print(type(var1))

# Função com interação do usuário
def mensagem(nome):
  print(f"Seja bem vindo {nome}")

nome = input("Digite seu nome: ")
mensagem(nome)

# Função com parametro padrao

def funcao(msg, nome='usuario'): # usa usuario como padrao
  print(msg, nome)

funcao("Seja bem vindo")
funcao("Seja bem vindo", "Mateus")

# Operacao dentro de uma funcao

def soma(n1, n2):
  return n1 + n2

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

print(f"A soma dos numeros é: {soma(n1, n2)}")

# Estrutura condicional em funcoes

def divisao(n1, n2):
  if n2 == 0:
    return "Operacao invalida"
  else:
    return n1 / n2

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

print(f"A divisao dos numeros é: {divisao(n1, n2)}")

# Funcao FizzBuzz
def fizz_buzz(num):
  if num % 3 == 0 and num % 5 == 0:
    return f'FizzBuzz, {num} é divisivel por 3 e 5'
  elif num % 3 == 0:
    return f'Fizz, {num} é divisivel por 3'
  elif num % 5 == 0:
    return f'Buzz, {num} é divisivel por 5'
  return num

num = int(input("Digite um numero: "))
print(fizz_buzz(num))

# Funcao com *args e *kwargs
# funcao sem uma definicao de qtd de parametros

def funcao(*args, **kwargs):
  print(args)
  print(kwargs)

funcao(1, 2, 3, nome="Mateus", idade=27)

'''
resultado:
(1, 2, 3)
{'nome': 'Mateus', 'idade': 27}
'''

# Funcao que recebe outra funcao
def msg_boas_vindas():
  return "Boas vindas"

def mestre(funcao):
  return funcao()

print(mestre(msg_boas_vindas))