#HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def palabra_al_reves(palabra):
    wordBackWards = ""
    for caracter in palabra:
        wordBackWards = caracter + wordBackWards
    return wordBackWards

def palabra_al_reves2(palabra):
    return palabra[::-1]

def palabra_al_reves_recursivo(palabra):
    # Caso base: si la palabra está vacía o tiene solo una letra
    if len(palabra) == 0:
        return palabra
    else:
        # Tomamos la primera letra y hacemos una llamada recursiva con el resto de la palabra
        return  palabra[0] +palabra_al_reves_recursivo(palabra[1:]) 

palabra = "Carro"
print(f"La palabra {palabra} al reves es {palabra_al_reves(palabra)}")
print(f"La palabra {palabra} al reves es {palabra_al_reves2(palabra)}")
print(f"RECURSIVO La palabra {palabra} al reves es {palabra_al_reves_recursivo(palabra)}")
