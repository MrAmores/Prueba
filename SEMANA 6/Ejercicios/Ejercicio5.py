#HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def compara_vectores(vec1, vec2):
    if len(vec1) != len(vec2):
        return False  
    else:
        for i in range(len(vec1)):
            if vec1[i] != vec2[i]:
                return False 
        return True
    
def compara_vectores_recursiva(vec1, vec2):
    # Caso base
    if len(vec1) != len(vec2):
        return False  
    # Caso base
    elif len(vec1) == 0 and len(vec2) == 0:
        return True  # Son iguales

    # Comparar los elementos
    if vec1[0] != vec2[0]:
        return False  # Encontró un elemento diferente

    return compara_vectores_recursiva(vec1[1:], vec2[1:])

vector1 = [1, 2, 3, 4, 5]
vector2 = [1, 2, 3, 4, 5]
vector3 = [1, 2, 3, 4, 1]

print(f"El vector {vector1} es igual al vector {vector2} {compara_vectores(vector1, vector2)}")
print(f"El vector {vector1} es igual al vector {vector3} {compara_vectores(vector1, vector3)}")
print(f"RECURSIVO El vector {vector1} es igual al vector {vector2} {compara_vectores_recursiva(vector1, vector2)}") 
print(f"RECURSIVO El vector {vector1} es igual al vector {vector3} {compara_vectores_recursiva(vector1, vector3)}")  

#HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        