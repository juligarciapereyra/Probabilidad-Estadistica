from practica_5 import generar_exp
import matplotlib.pyplot as plt
import numpy as np

#Ejericio 1 -------------------------------------------------------

def esperanza_muestral(lista):
    sumatoria = 0
    for i in lista: 
        sumatoria += i
    
    media = sumatoria / len(lista)
    return media


# def calcular_esperanza_muestral(muestra): # es la media/promedio
#     return sum(muestra)/len(muestra)

def varianza_muestral(lista):
    media = esperanza_muestral(lista)
    suma = 0
    n = len(lista)

    for i in lista: 
        suma += (i - media)**2
    
    s = (1 / (n-1)) * suma 
    return s

# def calcular_varianza_muestral(muestra):
#     n = len(muestra)
#     media = calcular_esperanza_muestral(muestra)
#     suma_diferencias_cuadrado = sum((x - media) ** 2 for x in muestra)
#     varianza_muestral = suma_diferencias_cuadrado / (n - 1)
#     return varianza_muestral

lista = [7.3, 8.6, 10.4, 16.1, 12.2, 15.1, 14.5, 9.3]

# esperanza = esperanza_muestral(lista)
# print("Espernaza:", esperanza)
# varianza = varianza_muestral(lista)
# print("Varianza: ", varianza)


#Ejercicio 2 ------------------------------------------------- 

def generar_muestra(n):
    muestra = []
    
    for _ in range(0, n): 
        muestra.append(generar_exp(0.5))

    return muestra 

def computar(muestra):
    media = esperanza_muestral(muestra)
    varianza = varianza_muestral(muestra)

    return media, varianza


muestra_1 = generar_muestra(10)
muestra_2 = generar_muestra(30)
muestra_3 = generar_muestra(100)
        
# E1, V1 = computar(muestra_1)
# print("E1: ", E1)
# print("V1: ", V1)
# print("\n")

# E2, V2 = computar(muestra_2)
# print("E2: ", E2)
# print("V2: ", V2)
# print("\n")

# E3, V3 = computar(muestra_3)
# print("E3: ", E3)
# print("V3: ", V3)
# print("\n")

# con mayor N mas se acerca al valor teorico donde E =  1/lambda = 2 y V = 1/lambda**2 = 4

#Ejercicio 3 --------------------------------------------------- 

anchos = [0.4, 0.2, 0.1]
muestras = [sorted(muestra_1), sorted(muestra_2), sorted(muestra_3)]

def plot_histograma(data, ancho):
    plt.hist(data, bins=np.arange(min(data), max(data) + ancho, ancho), weights=np.zeros(len(data)) + 1. / len(data))
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia Relativa')
    plt.title(f'Histograma con ancho de banda {ancho}')
    # plt.show()

# for muestra in muestras: 
#         for ancho in anchos:
#             plot_histograma(muestra, ancho)

#Ejercicio 4 --------------------------------------------------------- 

def histograma(muestra, ancho = 1): 
    plt.hist(muestra, bins=np.arange(min(muestra), max(muestra) + ancho, ancho), weights=np.zeros(len(muestra)) + 1. / len(muestra))
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia Relativa')
    plt.title(f'Histograma de Frecuencias Relativas - Muestra')


histograma(lista)
#plt.show()


#Ejercicio 5 ---------------------------- 

lista = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 7, 7, 8]


def funcion_distribucion_empirica(muestra):
    sorted_muestra = np.sort(muestra)
    n = len(muestra)
    l = [0] * n

    for i in range (n): 
        for j in range (n): 
            if(sorted_muestra[i] == sorted_muestra[j]):
                l[i] += 1
        l[i] = l[i] / n

    # print(l)
    # print("\n")

    l2 =[] 

    for i in range(1, n):
        if(l[i] != l[i-1]): 
            l2.append(l[i-1])

    if l[-1] != l[-2]:
        l2.append(l[-1])     

    # print(l2)
    # print("\n")

    count = 0
    for i in range(len(l2)): 
        count += l2[i]
        l2[i] = count
    
    return l2 
        
# funcion = funcion_distribucion_empirica(lista)
# print(funcion)
 
#-------------------------

def dist_empirica(muestra): 
    muestra = sorted(muestra)
    fn = [[f" x < {muestra[0]}", 0]]
    n = len(muestra)
    i = 0
    idx = 1
    while(i < n - 1):
        cont = 0
        elem = muestra[i]
       
        while i < n and muestra[i] == elem:
            i +=1
            cont +=1
        fn.append([f"{muestra[i-1]} <= x < {muestra[i]}", cont/n + fn[idx - 1][1]])
        idx +=1

    fn.append([f" x > {muestra[n-1]}", 1])
    return fn

# print(dist_empirica(lista))

       
#Ejercicio 6 ---------------------------- 

# muestra_normal = np.random.normal(0,1, 100)
# print(funcion_distribucion_empirica(muestra_normal))

# mu = 0
# sigma = 1
# sample = np.random.normal(loc=mu, scale=sigma, size=100)#print(sample)

# fde = dist_empirica(sample)
#print(fde)

def acumulada(datos): 
    def acu_empirica(x):
        cont = 0
        for d in datos: 
            if (d<=x): 
                cont +=1 

        F = cont/ len(datos)
        # F = len([for d in datos if d <= x]) / len(datos)
        return F
    return acu_empirica

datos = [1,2,3,4]
F = acumulada(datos)
print(F(2))


def inversa_Acumulada(I, F): 
        def inversa_acumulada(u):   # u pertenece (0,1)
            for x in I: 
                #imagenes = [F(x) for x in I]
                imagenes = F(x)      # esra ordenadao 
                for i in range (len(imagenes)): 
                    if (u >= imagenes[i]):
                        return imagenes[i]
        return inversa_acumulada
            
            



I = sorted([5,6,3,8,1])