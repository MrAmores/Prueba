def suma_num(num):
    if num == 0:
        return 0
    else:
        suma = 0
        for digito in str(num):
            suma += int(digito)
        return suma
    
num = int(input("Digite un numero "))
print(f"La suma de cada uno de los digitos del numero {num} es: {suma_num(num)} ")

