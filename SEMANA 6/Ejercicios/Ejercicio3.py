def division_entera_recursiva(num1, num2):
if num2 == 0:
        return print("No se ppuede dividir entre cero")
    elif num1 < num2:
        return 0
    else:
        return 1 + division_entera_recursiva(num1 - num2 , num2)
    
num1 = int(input("Digite el dividendo "))
num2 = int(input("Digite el divisor "))
print (f"Division entera {num1//num2}")
print(f"La división enterea de {num1}/{num2} es: {division_entera_recursiva(num1,num2)}")

print("Prueba")




        