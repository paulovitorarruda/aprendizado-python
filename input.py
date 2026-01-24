"""
Funçao input() - Função para receber dados do usuário

"""
"""
1º forma

nome = input("Qual é o seu nome?")
print("Olá," ,nome)

idade = input("Qual a sua idade?")
print("Sua idade é: " +idade)

"""

"""
2º forma

nome = input("Qual é o seu nome?")
idade = input("Qual a sua idade?")

print("Seu nome é: {0} e Sua idade é: {1}".format(nome,idade))

"""

nome = input("Qual é o seu nome?")
idade = input("Qual a sua idade?")

print(f'Seu nome é: {nome} e Sua idade é: {idade}')
