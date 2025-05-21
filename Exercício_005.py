numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = "impar"

    if par_impar:
        par_impar_texto= "par"

    print(f"O numero {numero_int} è {par_impar_texto}")
else :
    print("Isso não é um número inteiro")

entrada = input("Digite as horas em números inteiros: ")

try:

    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print("Bom dia Thiago!!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde Thiago!!")
    elif hora >= 18 and hora <= 24:
        print ("Boa noite Thiago!!")
    else:
        print("Não conheço essa hora...")
        
except:
     
     print("Por favor digite somente números inteiros")

nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome >= 1 and tamanho_nome <= 4:
    print("Seu nome é pequeno")
elif tamanho_nome >= 5 and tamanho_nome <= 8:
    print("Seu nome tem um tamanho normal")
elif tamanho_nome >= 9:
    print("Seu nome é muiiito grande!!")
else:
    print("Digite pelo menos uma letra!!!")

