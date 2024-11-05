#HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def es_palindrome_recursivo(palabra):
    palabra = palabra.lower().strip()  
    # caso base
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False  
    return es_palindrome_recursivo(palabra[1:-1])

def es_palindrome(palabra):
    wordBackWards = ""
    for caracter in palabra:
        wordBackWards = caracter + wordBackWards
    return wordBackWards.lower()  # Retorna la palabra al revés

palabra = input("Ingrese una palabra: ")
palabra2 = es_palindrome(palabra)  # Palabra invertida
palabra3 = es_palindrome_recursivo(palabra)  # Verificación recursiva

# Aquí es donde se realiza la comparación correcta
if palabra.lower().strip() == palabra2.lower().strip():  
    print(f"La palabra {palabra} es palíndromo: {palabra2} ")
    print(f"RECURSIVO: La palabra {palabra} es palíndromo: {palabra3} ")
else:
    print(f"La palabra {palabra} no es palíndromo: {palabra2} ")
    print(f"RECURSIVO: La palabra {palabra} no es palíndromo: {palabra3} ")
    
print("Sigo haciendo pruebas")
print("Sigo haciendo pruebas para la rama")
     
