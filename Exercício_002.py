nome = "Thiago Assis"
altura = 1.79
peso = 150
imc = peso / (altura * altura)

print(nome, "tem",altura, "de altura, e pesa", peso,)

if imc <= 18.5:
    print("seu IMC é:", imc,"|", "Você está abaixo do peso!")

if imc > 18.5 and imc <= 24.9:
    print("seu IMC é:", imc,"| ", "Você está com peso adequado!")

if imc > 24.9 and imc <= 29.9:
    print("seu IMC é:", imc,"|", "Você está com sobrepeso!")

if imc > 30:
    print("seu IMC é:", imc,"|", "Você está obeso!")