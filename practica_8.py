# #Ejercicio 1 ---------------------------- 
'''
Supongamos que tenemos dos variables aleatorias discretas X y Y , con Im(X) = {1, 2, . . . , n} e
Im(Y) = {1, 2, . . . , m}. Hacer un programa que tenga de input una tabla con la distribucion conjunta
(X, Y) y devuelva
(a) P(X + Y ≤ k) para k = 1, 2, . . . , n + m.
(b) E(X|Y = y) para y = 1, 2, . . . , m.
Usar los primeros ejercicios para verificar que el programa esta devolviendo los valores correctos

FORMATO TABLA
                            x
        f(x, y)     1     2      3

        1        0.05   0.05   0.1
    y   2        0.05   0.1    0.35
        3         0     0.2    0.1
'''

# def llenar_matriz(): 

#     f = int(input('Insertar numero de filas:'))
#     c = int(input('Insertra numero de columnas:'))

#     matriz = []
#     total = 0

#     for i in range(f): 
#         fila = []
#         for j in range(c): 
#             elemento = int(input('Ingrese numero:'))
#             total += elemento
#             fila.append(elemento)
#         matriz.append(fila)
    
#     return matriz, f, c, total

# matriz, f, c, total = llenar_matriz()
# print(matriz)
# print(total)

matriz = [[0.05, 0.05, 0.1], [0.05, 0.1, 0.35], [0, 0.2, 0.1]]
f = 3
c = 3
total = 1


def distribucion_conjunta(matriz, f, c, total): 
    dic = {}

    for i in range(f): 
        for j in range(c):
            dic[(i+1, j+1)] = matriz[i][j] / total 
    
    return dic

dic = distribucion_conjunta(matriz, f, c , total)
print(dic)


def prob_suma(): 
    n = int(input('Ingrese n:'))
    prob = 0

    for i in range(1, f): 
        for j in range(1, c): 
            if(i+j <= n): 
                prob += dic[(i, j)]
    return prob

# prob = prob_suma()
# print(prob)


def marginal_y():
    y = int(input('Ingrese y:')) 
    marginal = 0 

    for i in range(1, c+1): 
        marginal +=  dic[(y, i)]
        print(dic[(y, i)])
    
    return marginal, y

marginal, y = marginal_y()
print(marginal)
print("\n")

def prob_dado_que():
    probabilidad = [0]*c

    for i in range(1 , c+1): 
        prob = dic[(i, y)]
        probabilidad[i-1] += (prob / marginal) 
        
    
    return probabilidad

proba_dado_que = prob_dado_que()
print(proba_dado_que)
print("\n")


def esperanza():
    esperanza = 0

    for i in range(1, c+1): 
        esperanza += i * proba_dado_que[i-1]
        print(i,esperanza)
    return esperanza

e = esperanza()
print(e)
print("\n")

#--------------------------

def f_a(tabla, n, m):
    lista = [[0, 0]]  
    for k in range(2, n + m + 1): #porque x + y >= 2 siempre
        prob_acumulada = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i + j <= k:
                    prob_acumulada += tabla[j-1][i-1] # porque tengo x en cada columna e y en cada fila
                    
        lista.append([k, prob_acumulada])

    return lista


def f_b(tabla, n, m):
    lista = []
    for y in range(1, m+1):
        esperanza = 0
        for x in range(1, n + 1):
            py = 0
            for elem in tabla[y - 1]:
                py += elem
            esperanza += x*(tabla[y-1][x-1]/py)
        lista.append([f'E(X | y = {y})', esperanza])
    return lista
        

tabla_distribucion = [
    [0.05, 0.05, 0.1],
    [0.05, 0.1, 0.35],
    [0, 0.2, 0.1]
]

n = 3
m = 3

resultado = f_a(tabla_distribucion, n, m)
#print(resultado)

e = f_b(tabla_distribucion, n , m)
#print(e)


