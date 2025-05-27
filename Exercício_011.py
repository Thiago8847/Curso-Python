import os

lista = []
while True:
    print("Selecione uma opção")
    opcao = input("[I]nserir [A]pagar [L]istar: ")

    if opcao == "i":
        os.system("cls")
        valor = input("Valor: ")
        lista.append(valor)

    elif opcao == "a":
        indice_str = input("Escolha o índice para apagar: ")

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print("Não foi possível apagar este índice")
        
    elif opcao == "l":
        os.system("cls")

        if len(lista) == 0:
            print("Nada para listar")

        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print("Por favor, escolha i, a ou l. ")