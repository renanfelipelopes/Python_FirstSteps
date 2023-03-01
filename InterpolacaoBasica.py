"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

nome = 'Nintendo'
preco = 2250.300
variavel = 'O preço do %s é de R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d é %04x' % (255, 255))

