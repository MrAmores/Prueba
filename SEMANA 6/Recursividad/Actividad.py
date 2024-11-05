def algo(x):
    if x > 100:
        return (x*5)
    else:
        return (algo(x+10))
    
print("Algo 90 " , algo(90))
print("Algo 100 " , algo(100))
print("Algo 110 " , algo(110))
