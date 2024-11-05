#HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def suma_vector_recursivo(vec):
    if len(vec) == 0:
        return 0
    else:
        return vec[0] + suma_vector_recursivo(vec[1:])
    
def suma_vector(vec):
    suma = 0
    for num in vec:
        suma += num
    return suma

vector = [1,2,3,4,5]
print(f"la suma del vector {vector} es {suma_vector(vector)}")
print(f"RECURSIVO la suma del vector {vector} es {suma_vector_recursivo(vector)}")