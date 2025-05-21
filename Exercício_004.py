nome = input("Digite seu nome:")
idade = input("Digite sua idade:")

if nome and idade == "":
    print("Seu nome é", nome)
    print("Seu nome invertido é:",nome[::-1])

if " " in nome:
    print("Contem espaços em seu nome")
else:
    print("Não contem espaços em seu nome")

print("Seu nome contem",len(nome[0:]),"letras")
print("A primeira letra do seu nome é:",nome[0])
print("A ultima letra do seu nome é:", nome[-1])