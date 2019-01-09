import math

#Nuestras listas de almacenamiento de datos :3 Perra
lista = [0.78,0.04,0.96,0.61,0.43,0.82,0.83,0.22,0.83,0.51,0.98,0.29,0.26,0.14,0.67,0.94,0.88,0.50,0.79,0.07,0.24,0.68,0.91,0.38,0.62,0.19,0.18,0.16,0.65,0.18,0.73,
0.77,0.55,0.12,0.32,0.98,0.21,0.11,0.28,0.94,0.43,0.16,0.75,0.40,0.53,0.41,0.50,0.18,0.78,0.50,0.16,0.03,0.55,0.74,0.54,1.00,0.13,0.89,0.49,0.22,0.78,0.79,0.64,0.78,0.24,0.74,
0.43,0.80,0.36,0.66,0.47,0.22,0.39,0.98,0.29,0.92,0.69,0.42,0.86,0.91,0.18,0.37,0.53,0.27,0.18,0.14,0.08,0.29,0.87,0.48,0.55,0.80,0.45,0.60,0.08,0.43,0.12,0.87,0.64,0.24]
oi = [0]

#Comenzar a obtener valores

n = lista.__len__()
m = round(math.sqrt(n))

print "n = ",n
print "raiz m = ",m

#Formulas! Perra
intervalo = 1/m
ei = (n/m)

#Declaracoin de variables
rectas = 0

#Procedimiento <> Algoritmo > Zadot
while rectas <= 1:
    identificador_oi = 0
    conta = 0

    while conta < n:
        if (lista[conta] >= rectas) and (lista[conta] <= (rectas + intervalo)):
            identificador_oi += 1
        conta += 1

    if not (rectas + intervalo) > 1:
        oi.append(identificador_oi)
    rectas = rectas + intervalo
    
#Una vez mas pero para visualizar mi tabla
rectas = 0
conta = 1
x_suma = 0

print "\tIntervalos  \tOi Cantidad \tEi = (n/m) \tX!"
while rectas + intervalo <= 1:

    xri = (pow((ei - oi[conta]),2)) / ei
    x_suma = x_suma + xri

    print "\t{} > {} - {} \t    {} \t\t {} \t\t{}".format(conta,rectas,(rectas + intervalo),oi[conta],ei,xri)
    conta += 1
    rectas = rectas + intervalo

print "Suma total de X! es: ",x_suma