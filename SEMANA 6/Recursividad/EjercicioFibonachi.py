def fibonacci(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    a, b = 0, 1  
    for I in range(2, n + 1):
        a, b = b, a + b 
    return b

def fibonacci_recursivo(num):
    if num == 1 or num == 2:
        return 1
    elif num == 0:
        return 0 
    else:
        return (fibonacci_recursivo(num - 1) + fibonacci_recursivo(num - 2))
    
num = input(" Digite el numero del cual desea saber el fibonacci ")
num = int(num)    
print(f"Fibonacci Recursivo {fibonacci_recursivo(num)}")
print(f"Fibonacci Interactivo {fibonacci(num)}")