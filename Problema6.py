def fibonacci_hasta_50():
    """Genera la serie de Fibonacci desde 0 hasta 50."""
    a, b = 0, 1
    fibonacci = []
    
    while a <= 50:
        fibonacci.append(a)
        a, b = b, a + b
    
    return fibonacci

# Llamada a la función y mostrar el resultado
resultado = fibonacci_hasta_50()
print("Serie de Fibonacci entre 0 y 50:")
print(resultado)
