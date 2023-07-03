print("Ibtroduzca su peso en Kilos")
peso = input()
peso = int(peso)
peso = peso / 100
print("Introduzca su alktura en centimetros")
altura = input()
altura = int(altura)
altura = altura / 100

IMC = peso / altura ** 2
IMC = IMC * 100
print("IMC ", IMC)

if IMC <= 18.0:
    print ("Peso demasiado Bajo")
elif IMC <= 24.9:
    print ("Peso normal")
elif IMC <= 29.9:
    print ("tiene sobrepeso")
elif IMC > 29.9:
    print ("Tiene obecidad") 
 
