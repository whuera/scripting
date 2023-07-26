# script ingreso de notas de alumnos
# descripcion: script para ingreso de notas de alumnos con estructura clave-valor: {nombre, notas}
import math

# función para calcular el promedio
def calcularPromedio(notas):
    suma = sum(notas)
    return suma / len(notas)

# funcion para desviacion standar
def calcularDesviacionStandar(notas):
    # calculo del promedio
   promedio = calcularPromedio(notas) 
   varianza = sum((nota - promedio)**2 for nota in notas) /len(notas)
   # calculo de raiz cuadrada de la varianza para obtener desviacion standar
   return math.sqrt(varianza)

# funcion main
def main():
    # input datos de alumnos
    alumnos = {} 
    for i in range(1,11):
        nombre = input(f"Ingrese el nombre del alumno{i}: ")
        notas = list(map(float, input(f"Ingrese las notas del alumno {nombre}, separadas por espacio: ").split()))
        # asignar notas al key del alumno
        alumnos[nombre] = notas
        
    for nombre, notas in alumnos.items():
        promedio = calcularPromedio(notas)
        desviacion_standar = calcularDesviacionStandar(notas)
        print(f"Alumno: {nombre}")
        print(f"Promedio: {promedio}")
        print(f"Desviacion standar: {desviacion_standar}")
        
if __name__=="__main__":
    main()