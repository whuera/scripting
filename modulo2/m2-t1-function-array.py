# Definición de una función para calcular una ecuación de segundo grado
# variables de entrada: a, b, c
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
    
# Crear un arreglo vacío
valores = []  

# Pedir al usuario que ingrese los valores
for i in range(5):
    valor = input(f"Ingrese un valor {i}: ")
    valores.append(valor)  # Agregar el valor al arreglo
    array_order = sorted(valores)
    valor_a = array_order[0]
    valor_b = array_order.pop()
    
print("Los valores ingresados son:", array_order)
valor_c = array_order[1]
print("valor_c ", valor_c)
respuesta = calcular_ecuacion_segundo_grado(int(valor_a),
                                            int(valor_b),
                                            int(valor_c))
print(f"respuesta ecuación: {respuesta}")