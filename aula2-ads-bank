from os import pathconf_names
# Aula 2

print("Bem vindo ao ADS Bank")

# Entradas

salario_bruto = float(input("Digite o salario bruto em R$: "))
valor_parcela = int(input("Digite o valor da parcela em R$: "))
qtd_parcelas = int(input("Digite o numero de meses do financiamento: "))

# Processamento

aprovado = False

score = -1
while score < 0 or score > 1000:
  score = int(input("Digite seu score: "))

idade = -1
while idade < 0 or idade > 100:
  idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 75:
  if score >= 700: # ate 45% do salario
    if valor_parcela <= salario_bruto * 0.45:
      aprovado = True
      print("APROVADO")
    else:
      print("REPROVADO POR COMPROMETIMENTO DE RENDA!")
  elif score >= 500 and score < 700: # ate 30% do salario
    if valor_parcela <= salario_bruto * 0.3:
      aprovado = True
      print("APROVADO")
    else:
      print("REPROVADO POR COMPROMETIMENTO DE RENDA!")
  elif score >= 300 and score < 500: # ate 15% do salario
    if valor_parcela <= salario_bruto * 0.15:
      aprovado = True
      print("APROVADO COM FIADOR")
    else:
      print("REPROVADO POR COMPROMETIMENTO DE RENDA!")
  elif score < 300:
    print("REPROVADO POR BAIXO SCORE")
else:
  print("CRÉDITO NEGADO: IDADE FORA DA FAIXA")

if score >= 800:
  valor_parcela *= 1.02
elif 500 <= score < 800:
  valor_parcela *= 1.05
else:
  valor_parcela *= 1.1

print(f"Novo parcela de R$ {valor_parcela:.2f} e saldo devedor R$ {valor_parcela*qtd_parcelas:.2f}")
