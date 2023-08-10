
#Ejericio 1 ----------------------

'''
x 0 1 2 3 4 5 6 7 8 9 10
p(x) 0.002 0.001 0.002 0.005 0.02 0.04 0.18 0.37 0.25 0.12 0.01
'''
df = [[0, 0.002], [1, 0.001], [2, 0.002], [3, 0.005], [4, 0.02], [5, 0.04], [6, 0.18], [7, 0.37], [8,0.25 ], [9, 0.12], [10, 0.01]]

def esperanza(df):
    cantidad = len(df)
    E = 0
    for i in range(cantidad):
        E += df[i][0]*df[i][1] #sumatoria(x*p(x))
    return E 

def varianza(df): 
    cantidad = len(df)
    V = 0
    for i in range(cantidad):
        V += (df[i][0]**2)*df[i][1] #E(X**2)
    return V - (esperanza(df))**2 #E(X**2) - E(X)**2
    
#print(esperanza(df), varianza(df))


#---------------------

def calcular_esperanza_varianza(x, px):
    """
    Calcula el valor esperado (E(X)) y la varianza (V(X)) de una variable aleatoria discreta.

    Args:
        x (list): Lista de valores posibles de la variable aleatoria.
        px (list): Lista de probabilidades correspondientes a cada valor de x.

    Returns:
        tuple: Tupla que contiene el valor esperado (E(X)) y la varianza (V(X)).
    """
    esperanza = sum(x[i] * px[i] for i in range(len(x)))
    varianza = sum((x[i] - esperanza) ** 2 * px[i] for i in range(len(x)))
    return esperanza, varianza



x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
px = [0.002, 0.001, 0.002, 0.005, 0.02, 0.04, 0.18, 0.37, 0.25, 0.12, 0.01]
esperanza, varianza = calcular_esperanza_varianza(x, px)
print("Valor Esperado (E(X)): ", esperanza)
print("Varianza (V(X)): ", varianza)
