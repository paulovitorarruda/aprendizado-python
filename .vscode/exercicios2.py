# EXERCÍCIO 01
# Descrição: Receber idade e classificar:
# < 16: MENOR | 16-18: EMANCIPADO | > 18: MAIOR

idade = int(input("Digite a idade da pessoa: "))

if idade < 16:
    print("MENOR")
elif 16 <= idade <= 18:
    print("EMANCIPADO")
else:
    print("MAIOR")


# EXERCÍCIO 02
# Descrição: Receber idade de um nadador e imprimir categoria:
# 5-7: Infantil A | 8-10: Infantil B | 11-13: Juvenil A | 14-17: Juvenil B

idade_nadador = int(input("\nDigite a idade do nadador: "))

if 5 <= idade_nadador <= 7:
    print("Categoria: Infantil A")
elif 8 <= idade_nadador <= 10:
    print("Categoria: Infantil B")
elif 11 <= idade_nadador <= 13:
    print("Categoria: Juvenil A")
elif 14 <= idade_nadador <= 17:
    print("Categoria: Juvenil B")
else:
    print("Idade fora das categorias listadas.")
