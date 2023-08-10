import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

#Ejercicio 1----------------------------------

# Simular N variables aleatorias independientes con distribucion exponencial de parametro λ = 2 para
# N = 100, 200, 400, 600, 800. Calcular los intervalos de confianza del 90%, 95% y 99% para µ con
# varianza desconocida. Graficar los intervalos para cada confianza, en funcion de N.

def calcular_intervalo(muestra, c):
    n = len(muestra)
    S = np.std(muestra, ddof=1)
    media = np.mean(muestra) 
    alpha = 1 - c

    t = sps.t.ppf(1 - alpha/2, df=n-1)

    return [media - t * S/np.sqrt(n), media + t * S/np.sqrt(n)]

# N_values = [100, 200, 400, 600, 800]
# confianza_values = [0.9, 0.95, 0.99]

# for confianza in confianza_values:
#     intervalos = []
#     for N in N_values:
#         muestra = np.random.exponential(scale=1/2, size=N)
#         intervalo = calcular_intervalo(muestra, confianza)
#         intervalos.append(intervalo)

#     plt.plot(N_values, intervalos, label=f'Confianza {confianza}')

# plt.xlabel('N')
# plt.ylabel('Intervalo de Confianza para µ')
# plt.legend()
# plt.show()


#Ejercicio 2----------------------------------

# Simular 400 variables aleatorias independientes con distribucion exponencial de paraametro λ = 2.
# Considerando la muestra calcular el intervalo de confianza del 95% para µ asumiendo varianza desconocida. Volver a hacer esta simulacion y este intervalo 100 veces. Para cada simulacion fijarse si el
# verdadero valor de µ esta o no en el intervalo, mostrar esta informacion con algun grafico.

cont_ok = 0 
cont_no = 0 

for i in range(100): 
    lambd = 2 
    mu = 1/lambd
    muestra = np.random.exponential(scale= mu, size=400)
    I = calcular_intervalo(muestra, 0.95)
    
    if(I[0] <= mu <= I[1]): 
        cont_ok += 1 
    else: 
        cont_no += 1

print(cont_ok, cont_no)
# plt.bar(['acertados', 'no acertados'], [cont_ok/100, cont_no/100])
# plt.show()


#Ejercicio 3----------------------------------

# Simular N (con N = 100, 200, 300, 400) v.a.i.i.d. con distribucion Poisson de parametro λ = 1/2. Para
# cada valor de N hacer los histogramas de frecuencias relativas sabiendo que la distribucion es discreta
# y conociendo su rango. ¿Importa el ancho de banda?

N = [100, 200, 300, 400]

for n in N: 
    muestra = np.random.poisson(lam=1/2, size=n)
    rango = [min(muestra), max(muestra)]
    bw = 0.5 
    plt.xlabel(r'$Y$', fontsize = 15)
    plt.ylabel(r'Frecuencia relativa', fontsize = 15)
#   plt.hist(muestra, bins=np.arange(rango[0], rango[1] + bw, bw), weights=np.zeros(len(muestra)) + 1. / len(muestra))
#   plt.show()

# #El ancho de banda no me cambia la altura pero si los anchos y es importante para que se pueda visualizar bien ya que sino quedan mucho espacio en blanco




#Ejercicio 4----------------------------------

# Simular N (con N = 100, 200, 300, 400) v.a.i.i.d. con distribucion Uniforme en el intervalo [2, 5]. Para
# cada valor de N hacer los histogramas de probabilidad con anchos de banda 2, 1 y 0.5

for n in N:
    muestra = np.random.uniform(low=2, high=5, size = n)
    bw = 1 
    plt.hist(muestra, bins=np.arange(min(muestra), max(muestra) + bw, bw), density=True)  
    #plt.show()

#las areas suman 1


#Ejercicio 5----------------------------------

# Simular N = 400 v.a.i.i.d. con distribuci´on normal µ = 2, σ2 = 1/2 y N v.a.i.i.d. con distribucion
# normal µ = −1 y σ2 = 1/4. Considerar los datos que vienen de sumar lugar a lugar cada una de estas
# simulaciones. De estos nuevos datos, calcular la media y la varianza muestral. Interpretar. Graficar
# el histograma de probabilidad con ancho de banda 0.5, 1 y 4. ¿Qu´e observa?

mu1 = 2 
sigma1 = np.sqrt(1/2)
muestra1 = np.random.normal(mu1, scale= sigma1, size= 400)

mu2 = -1 
sigma2 = np.sqrt(1/4)
muestra2 = np.random.normal(mu2, scale= sigma2, size= 400)

muestra = muestra1 + muestra2
media_muestral = np.mean(muestra)
s = np.std(muestra, ddof=1)
bws = [0.25, 0.5, 1, 4]

for bw in bws:
    plt.hist(muestra, bins=np.arange(min(muestra), max(muestra) + bw, bw), density=True)  
    #plt.show()


#Ejercicio 6----------------------------------

# Simular 20 variables aleatorias independientes llamadas Xi, i = 1, 2, . . . , 20 cada una con distribucion
# normal de parametros µi = i y σ^2 = 1/i, i = 1, 2, . . . , 20. Sean U = P20 i=1 Xi y Z = U−E(U)/√ Var(U)
# Volver a realizar este procedimiento de manera independiente para obtener 100 muestras de la variable aleatoria
# Z. Utilizando la muestra de Z graficar el histograma de probabilidad. Hint: Recordar la formula para
# la esperanza y la varianza de suma de normales, la cual esta en la clase de distribuciones especiales.

Z_muestra = []
for i in range(100):
    U = 0
    E = 0
    V = 0
    for i in range(1, 21):
        Xi = np.random.normal(i, scale=np.sqrt(1/i))
        U += Xi
        E += i
        V +=1/i
    Z = (U - E)/np.sqrt(V)   
    Z_muestra.append(Z)

bw = 0.5
plt.hist(Z_muestra, bins=np.arange(min(Z_muestra), max(Z_muestra) + bw, bw), weights = np.zeros(len(Z_muestra)) + 1. / (len(Z_muestra)*bw), density=True)  
plt.show()


#Ejercicio 7----------------------------------

# Simular N = 200 v.a.i.i.d. una con distribucion normal de parametros µ = 2 y σ2 = 3. Usar estos datos
# para calcular un intervalo de confianza de nivel 90%, 95% y 99% para la varianza. ¿Cual intervalo es
# mas grande y cual mas chico? ¿A que se debe esto?.

mu = 2
sigma = np.sqrt(3)
muestra = np.random.normal(mu, scale=sigma, size=200)

def calcular_intervalo_var(muestra, c):
    n = len(muestra)
    alpha = 1 - c
    S = np.std(muestra, ddof = 1)
    chi_sup = sps.chi2.ppf(alpha/2, df=n-1)
    chi_inf = sps.chi2.ppf(1 - alpha/2, df = n-1)
    return [((n-1)*S**2)/chi_inf, ((n-1)*S**2)/chi_sup]

conf =  [0.9, 0.95, 0.99]

for c in conf:
    print(calcular_intervalo_var(muestra, c))

