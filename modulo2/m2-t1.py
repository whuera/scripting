import math
print("RESOLUCIÓN DE ECUACIÓN DE SEGUNDO GRADO")
# Ingreso de variables
# mostramos en pantalla y realizamos un set a la s variables definidas
# seteamos en la variable valor_a, el primer ingreso en consola
# seteamos en la variable valor_b, el segundo ingreso en consola
# seteamos en la variable valor_c, el tercer ingreso en consola

valor_a = int(input("Ingrese el primer valor: "))
valor_b = int(input("Ingrese el segundo valor: "))
valor_c = int(input("Ingrese el tercer valor: "))

# cálculo de componente en la variable aux vamos almacenar el calculo (b^2 - 4ac)
# utilizamos la función pow para elevar al cuadrado el valor de la variable: valor_b 
aux = (pow(valor_b, 2) - (4 * (valor_a * valor_c)))
print("valor de aux: ",aux)

# calulo valor raiz de aux
# para este caso utilizamos el operador sqr que nos devuelve el 
# valor de la raiz cuadrada de un número 
aux2 = math.sqrt(aux)
print("calulo valor raiz de aux: ",aux2)

# calculo (-b + aux2)
# en la variable temp1 vamos almacenar los valores obtenidos del calculo de: (-b + aux2)
temp1 = ((valor_b * -1) + aux2)
print("valor temp: ",temp1)

## calcular el valor de (temp1 / 2a)
## para este cason utilizamos el operador división
x1 = (temp1 / (2 * valor_a))
print("valor x1: ",x1)

## tipos de datos:
print(f"tipo de dato variable valor_a: {type(valor_a)}")
print(f"tipo de dato variable valor_b: {type(valor_b)}")
print(f"tipo de dato variable valor_c: {type(valor_c)}")
print(f"tipo de dato variable aux: {type(aux)}")
print(f"tipo de dato variable aux2: {type(aux2)}")
print(f"tipo de dato variable temp1: {type(temp1)}")
print(f"tipo de dato variable x1: {type(x1)}")

# Operadores matemáticos usados:
# división, suma, resta, multiplicación, elevación al cuadrado
# raiz cuadrada
