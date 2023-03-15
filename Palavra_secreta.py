palavra_secreta = input('Digite a palavra secreta: ')
letras_acertadas = ''

while True:
    letra_digitada = input('Letra digitada: ')

    if len(letra_digitada > 1):
        print('Digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            print('*')