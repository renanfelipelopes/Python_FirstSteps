# Qual letra apareceu mais vezes na frase?
frase = "Python é uma linguagem de programação de alto nível, " \
    "interpretada de script, imperativa, orientada a objetos, funcional, " \
    "de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991."

i = 0
letra_mais_utilizada = ''
qtd_de_vezes_que_apareceu = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if (qtd_de_vezes_que_apareceu < qtd_atual):
        qtd_de_vezes_que_apareceu = qtd_atual
        letra_mais_utilizada = letra_atual

    i += 1

print(
    'A letra usada mais vezes, foi '
    f'"{letra_mais_utilizada}" que apareceu '
    f'{qtd_de_vezes_que_apareceu}x'
)