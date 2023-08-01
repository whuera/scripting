def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0:
        return 1
    else:
        result = 1
        while n > 0:
            result *= n
            n -= 1
        return result

# Ejemplos de uso
print(factorial(5))  # Salida: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)
print(factorial(0))  # Salida: 1 (0! = 1)
print(factorial(-2)) # Salida: "El factorial no está definido para números negativos."
