import numpy as np
ventas_clientes_2021 = np.array([100,120,110,90,150,80,70,100,100,110,90,100]) 
print(ventas_clientes_2021)

max_value = None

for num in ventas_clientes_2021:
    if (max_value is None or num > max_value):
        max_value = num

print('Máximo valor:', max_value)

min_value = None

for num in ventas_clientes_2021:
    if (min_value is None or num < min_value):
        min_value = num

print('Min valor:', min_value)

ventaMaxima = max_value
ventaMinima = min_value

diferenciaVentaMaxMin = ventaMaxima - ventaMinima
print(f"la diferencia enytre la venta máxima y la mínima es: {diferenciaVentaMaxMin}")

suma = 0
for valor in ventas_clientes_2021:
    suma = suma + valor

print(f"La suma total es: {suma}")
cantidad_elementos = len(ventas_clientes_2021)
promedio = suma / cantidad_elementos
print(f"El promedio de venta es {promedio}")