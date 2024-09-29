def eliminar_vocales(texto):
    """Función que elimina las vocales de una cadena de texto."""
    vocales = "aeiouAEIOU"
    
    resultado = ''.join([letra for letra in texto if letra not in vocales])
    
    return resultado

entrada = input("Ingrese una cadena de texto: ")

salida = eliminar_vocales(entrada)
print(f"Resultado sin vocales: {salida}")
