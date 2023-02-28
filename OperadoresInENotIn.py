# Operadores in e not in

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f'{encontrar} não está em {nome}')


# nome = 'Renan'
# print(nome[2])
# print(nome[-1])
# print('re' in nome)
# print('lop' in nome)
# print(10 * '-')
# print('re' not in nome)
# print('lop' not in nome)