"""
Exercícios - Python

Observação: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

01 - área de um retângulo.
02 - área de um quadrado.
03 - área de um círculo.
04 - Se o produto que você quer avaliar custa (??) reais,
qual será o vaor do mesmo com desconto de (??)%.
05 - conversão de reais para dolar.
06 - conersão de dolar para reais.

"""
# Exercício 01 - área do retângulo

print("Calcule a area de um retangulo")

base = input("Qual o tamanho da base do seu retangulo? ")
altura = input("Qual o tamanho da altura do seu retangulo? ")
area = float(base) * float(altura)

print(f'O seu retangulo possui area: {area} unidade de medida')


# Exercício 02 - área do quadrado

print("Calcule a area de um quadrado")

lado = input("Qual o tamanho do lado do seu quadrado? ")
area = float(lado) * float(lado)

print(f'O seu quadrado possui area: {area} unidade de medida')


# Exercício 03 - área do círculo

print("Calcule a area de um círculo")

# Convertendo para float logo no input para simplificar o cálculo abaixo
raio = float(input("Qual o raio do seu círculo? "))
area = 3.14 * (raio ** 2)

print(f'O seu círculo possui area: {area} unidade de medida')


# Exercício 04 - Desconto de produto

print("Calcule o valor de um produto com desconto")

preco = float(input("Qual o preço original do produto (R$)? "))
desconto = float(input("Qual a porcentagem de desconto (%)? "))

# O cálculo: preço original menos (preço * porcentagem / 100)
valor_final = preco - (preco * desconto / 100)

print(f'O produto com {desconto}% de desconto custará: R$ {valor_final}')


# Exercício 05 - Conversão de Real para Dólar

print("Converta Reais (BRL) para Dólar (USD)")

reais = float(input("Quantos reais você tem (R$)? "))
cotacao = float(input("Qual a cotação atual do dólar? "))

dolares = reais / cotacao

print(f'Com R$ {reais} você consegue comprar: US$ {dolares}')


# Exercício 06 - Conversão de Dólar para Real

print("Converta Dólar (USD) para Reais (BRL)")

dolares = float(input("Quantos dólares você tem (US$)? "))
cotacao = float(input("Qual a cotação atual do dólar? "))

reais = dolares * cotacao

print(f'Seus US$ {dolares} valem em reais: R$ {reais}')
