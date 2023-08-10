import numpy as np
import scipy.stats as sps

#Ejercicio 1-------------------------------

# Hacer una funcion que tenga como input el tamano n de muestras independientes de N(100, 5), genere las n muestras independientes.

def generar_muestras_normales(n):
    mu = 100  
    sigma = 5  
    samples = np.random.normal(loc=mu, scale=sigma, size=n)
    return samples

#print(generar_muestras_normales(5))


#Ejercicio 2-------------------------------

# Realizar una funcion que tenga de input la muestra de tamano n de variables aleatorias independientes e identicamente distribuidas,
# su varianza conocida y el nivel de confianza c y devuelva intervalos de confianza del c% para la media de cada muestra

def idc(muestra, sigma, confianza): 
    I = [0,0]
    n = len(muestra)
    alpha = 1 - confianza
    media = np.mean(muestra)

    z = sps.norm.ppf(1 - alpha/2)
    I[0] = media - z * sigma/np.sqrt(n)
    I[1] = media + z * sigma/np.sqrt(n)

    return I

muestra = [1.5, 2.2, 3.7, 2.1, 2.9]
sigma = 1.0
c = 0.95 

# intervalo = idc(muestra, sigma, c)
# print("Intervalo de confianza:", intervalo)



#Ejercicio 3-------------------------------

# Repita el punto anterior pero usando la varianza estimada s2.

def idc2(muestra, confianza): 
    I = [0,0]
    n = len(muestra)
    alpha = 1 - confianza
    media = np.mean(muestra)
    S2 = np.var(muestra, ddof=1)

    t = sps.t.ppf(1 - alpha/2, df=n-1)
    I[0] = media - t * np.sqrt(S2)/np.sqrt(n)
    I[1] = media + t * np.sqrt(S2)/np.sqrt(n)

    return I


#Ejercicio 4-------------------------------

# Generar una muestra de tamano n = 100 independientes de una N(100, 5). Con los datos
# obtenidos, usar las funciones de los items anterior para construir dos intervalos del 95% y del
# 98% de confianza para la media de la muestra suponiendo que sabemos que la varianza es 5 y
# suponiendo varianza desconocida. En ambos casos notar cual intervalo tiene mayor longitud y
# responder a que se debe esto.

muestra = generar_muestras_normales(100)
i1 = idc(muestra, 5, 0.95)
i2 = idc2(muestra, 0.95) 
i3 = idc(muestra, 5, 0.98)
i4 = idc2(muestra, 0.98)
print(i1, abs(i1[1] - i1[0]))
print(i2, abs(i2[1] - i2[0]))
print(i3, abs(i3[1] - i3[0]))
print(i4, abs(i4[1] - i4[0]))

# Los que desconocen la varianza son mucho mas largos xq la desviacion muestral es aleatoria (depende de la muestra)
# y por lo tanto es mucho mas variable e impreciso. Ademas a mayor confianza mayor longitud de intervalo
