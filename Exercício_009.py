import os

palavra_secreta = "cachorro"
letras_acertadas = ""
numeros_tentativas = 0

while True:

    letra_digitada = input("Digite sua letra: ")

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue

    numeros_tentativas += 1

    if numeros_tentativas > 10:
        print("Acabou suas tentativas")
        break

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
            
    print("Palavra formada: ", palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("Voce ganhou! Parabéns!!")

letras_acertadas = ""
numeros_tentativas = 0