import math
import random

#Ejericio 1 ----------------------------

# Utilizando unicamente la funcion random de su lenguaje (la funcion que genera un numero aleatorio uniforme entre 0 y 1), implemente una funcion que genere un numero distribuido Bernoulli con
# probabilidad p.

def generar_bernoulli(p):
    if random.random() <= p:
        return 1
    else:
        return 0
    
n = generar_bernoulli(4)
print(n)


#Ejercicio 2 ---------------------------

# Utilizando la funcion del punto anterior, implemente otra que genere un numero binomial con los
# parametros n, p.

def generar_binomial(n, p):
    binomial = 0
    for _ in range(n):
        resultado_bernoulli = generar_bernoulli(p)
        binomial += resultado_bernoulli
    return binomial


#Ejericio 3 ----------------------------

# Utilizando el procedimiento descrito en el capıtulo 6 del Dekking (metodo de la funcion inversa o de
# Monte Carlo), implementar una funcion que permita generar un numero aleatorio con distribucion
# Exp(λ).

def generar_exp(lambda_val):
    U = random.random()
    x = -math.log(U) / lambda_val
    return x

numero_aleatorio = generar_exp(2)
#print(numero_aleatorio)
