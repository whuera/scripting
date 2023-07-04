import math

# Definición de una función para calcular una ecuación de segundo grado
# variables de entrada: a, b, c
print("RESOLUCIÓN DE ECUACIÓN DE SEGUNDO GRADO")
def calcular_ecuacion_segundo_grado(a, b, c):
    aux = b**2 - 4*a*c

    if aux > 0:
        x1 = (-b + math.sqrt(aux)) / (2*a)
        x2 = (-b - math.sqrt(aux)) / (2*a)
        return x1, x2
    elif aux == 0:
        x = -b / (2*a)
        return x
    else:
        return "La ecuación no tiene respuesta reales."

# Ejemplo de uso
respuesta = calcular_ecuacion_segundo_grado(int(input("Ingrese el primer valor: ")), 
                                            int(input("Ingrese el segundo valor: ")), 
                                            int(input("Ingrese el tercer valor: ")))
print(respuesta)
