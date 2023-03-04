# Calculadora com while
import operator

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

def validar_input(inp):
    if inp == '':
        i = 1
        while i < 4:
            print(f"Digite um número válido! Você tem {4 - i} tentativas!")
            n = input("Digite um numero: ")
            i += 1
            if i == 4 and n == '':
                print("Fim de tentativas.")
                exit()

    if inp.isdigit():
        number_input = int(inp)
    else:
        number_input = float(inp)
    
    return number_input

while True:
    num_1 = input("Digite o primeiro número: ")
    num_2 = input("Digite o segundo número: ")
    operador = input("Digite um operador (+-*/): ")

    numero_1 = validar_input(num_1)
    numero_2 = validar_input(num_2)

    operadores_permitidos = "+-*/"

    if operador not in operadores_permitidos:
        print("Operador inválido!")
        continue
    
    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print(f'{numero_1} {operador} {numero_2} =', operators[operador](numero_1, numero_2))

    sair = input("Quer sair? [s]im: ").lower().startswith("s")
    
    if sair is True:
        break