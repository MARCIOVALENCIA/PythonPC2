def factorial(n):
    """Función que calcula el factorial de un número no negativo."""
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es: {factorial(numero)}")
