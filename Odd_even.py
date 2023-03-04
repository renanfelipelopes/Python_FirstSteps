number = input("Digite um numero: ")

def odd_even(n):
    num = validar_input(n)

    if num % 2 == 0: 
        print(f"O número {num} é par!")
    else:
        print(f"O número {num} é ímpar!")


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

print(odd_even(number))