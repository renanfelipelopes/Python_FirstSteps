nome = input('Diga qual é seu nome: ')
altura = input('Qual é sua altura? ')
peso = input('Quanto você pesa? ')
imc = int(peso) / (float(altura) ** 2)

print(f'\n{nome} tem {float(altura):.2f} de altura,\npesa {int(peso)} quilos e seu imc é \n{imc:.2f}')