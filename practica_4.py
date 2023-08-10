#Ejercicio 1-----------------------------

# Hacer una funcion que calcule la funcion de distribucion acumulada de una variable aleatoria Hipergeometrica. Los inputs son los parametros N, n, k y el output es un dataframe con 2 columnas, en una
# los rangos de x y en la otra FX(x) para los x en ese rango.
# Hint: primero hacer una funcion que calcule las probabilidades puntuales.

import pandas as pd
import math

def comb(n, k):
    """
    Calcula el coeficiente binomial "n choose k".
    
    Args:
        n (int): Tamaño del conjunto.
        k (int): Número de elementos a elegir.
        
    Returns:
        int: Coeficiente binomial "n choose k".
    """
    return math.comb(n, k)


def hipergeometrica_pmf(N, n, k, x):
    """
    Calcula la función de masa de probabilidad (PMF) de una variable aleatoria hipergeométrica.
    
    Args:
        N (int): Tamaño de la población.
        n (int): Tamaño de la muestra.
        k (int): Número de éxitos en la población.
        x (int): Valor para el cual se desea calcular la PMF.
        
    Returns:
        float: Valor de la PMF en el punto x.
    """
    if x < max(0, n - (N - k)) or x > min(n, k):
        return 0.0
    else:
        return (comb(k, x) * comb(N - k, n - x)) / comb(N, n)

def hipergeometrica_cdf(N, n, k):
    """
    Calcula la función de distribución acumulada (CDF) de una variable aleatoria hipergeométrica.
    
    Args:
        N (int): Tamaño de la población.
        n (int): Tamaño de la muestra.
        k (int): Número de éxitos en la población.
        
    Returns:
        pd.DataFrame: DataFrame con las columnas 'x' (rango de valores) y 'CDF' (valores de la CDF en cada punto).
    """
    values = []
    cdf = []
    for x in range(0, k+1):
        values.append(x)
        cdf.append(sum(hipergeometrica_pmf(N, n, k, i) for i in range(0, x+1)))
    
    df = pd.DataFrame({'x': values, 'CDF': cdf})
    return df


N = 100  # Tamaño de la población
n = 20   # Tamaño de la muestra
k = 10   # Número de éxitos en la población

df = hipergeometrica_cdf(N, n, k)
print(df)

#------------------------

def factorial_iter(n):
    res = 1
    for num in range(1, n + 1):
        res = res*num
    return res

def C(n, k): #combinatoria
    if (k == 0  or k == n):
        return 1
    return factorial_iter(n)/ (factorial_iter(n- k) * factorial_iter(k))

def hipergeometrica_puntual(N, n, k, x):
    return (C(k, x)*C(N - k, n - x))/C(N, n)

def hipergeometrica_acumulada(N, n, k):
    df = []
    df.append([0, hipergeometrica_puntual(N, n, k, 0)])
    for x in range(1, k + 1):
        anterior = df[-1][1]
        df.append([x, anterior + hipergeometrica_puntual(N, n, k, x)])
        
    return df


df = hipergeometrica_acumulada(100, 20, 10)
#print(df)