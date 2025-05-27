frase = "Mais que uma razão pra se viver, Uma verdadeira causa pela qual morrer, Seja o prólogo de quem viveu a preparar o seu epílogo, E dito, deu fé"

i = 1
qtd_apareceu_mais_vezes = 0
Letra_apareceu_mais_vezes = " "


while i < len(frase):
    letrea_atual = frase[1]

    if letrea_atual == " ":
        i +- 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letrea_atual)

    if qtd_apareceu_mais_vezes <= qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        Letra_apareceu_mais_vezes = letrea_atual


    i += 1

    print(
        "A letra que apareceu mais vezes foi"
        f'"{Letra_apareceu_mais_vezes}" que apareceu'
        f"{qtd_apareceu_mais_vezes}x"
    )