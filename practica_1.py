
#Ejercicio 1

def factorial(n: int) -> int: 
     result = 1
     for i in range(1, n+1):
        result *= i 
        



def factorial_2(n: int) -> int: 
    if (n == 0): 
        return 1
    
    return n * factorial_2(n-1) 

    
def main(): 

    result = factorial_2(0)
    print(result)

if __name__ == "__main__": 
    main()