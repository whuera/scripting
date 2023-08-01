import math

def ingresar_notas(n):
    notas = []
    for i in range(n):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    return notas

def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    sumatoria = sum(notas)
    return sumatoria / len(notas)

def calcular_desviacion_estandar(notas, promedio):
    if len(notas) == 0:
        return 0
    sumatoria_cuadrados = sum((nota - promedio) ** 2 for nota in notas)
    return math.sqrt(sumatoria_cuadrados / len(notas))

if __name__ == "__main__":
    n = 0
    while n <= 0:
        n = int(input("Ingrese la cantidad de notas (debe ser mayor a 0): "))

    lista_notas = ingresar_notas(n)
    lista_notas_sin_cero = [nota for nota in lista_notas if nota != 0]

    promedio = calcular_promedio(lista_notas_sin_cero)
    desviacion_estandar = calcular_desviacion_estandar(lista_notas_sin_cero, promedio)

    print(f"\nNotas ingresadas: {lista_notas}")
    print(f"Notas consideradas para cálculo: {lista_notas_sin_cero}")
    print(f"Promedio de notas: {promedio:.2f}")
    print(f"Desviación estándar: {desviacion_estandar:.2f}")
