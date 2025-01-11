def factorial(num):
    fact = 1
    if not type(num) is int:
        raise TypeError(f"{num} It's not an integer")
    elif type(num) is int and num <= 0:
        raise TypeError(f"{num} It's equal to or lower than 0")
    
    for element in range(num, 1, -1):
        fact = fact * element
        print(num)
    
    return fact    
    
__name__=='__main__'
try:
    print(factorial(5))
    print(factorial(7))
    print(factorial(8))
    print(factorial(-2))
except TypeError as error:
    print(error)
    
try:
    print(factorial("a"))
except TypeError as error:
    print(error)