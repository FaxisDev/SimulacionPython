#Numero Aleatorio
#x0 = 5735
x0 = input("Ingresa x0 para generar numero aleatorio: ")
#Total de Ciclos

ciclo = input("Ingresa la cantidad de ciclos: ")

contador = str(x0)

i = 0
for x in contador:
    i += 1

print "\n"

xi = 0
j = 1
while j <= ciclo:
    texto_union = ""
    xi = str(pow(x0,2))
    k = 0
    for cont in xi:
        k += 1
    #Comprobara los espacios
    if (k - i) % 2 == 0:
        espacios = (k - i) / 2
        llegada = i + espacios
        while espacios < llegada:
            texto_union = texto_union + xi[espacios]
            espacios += 1
        x0 = int(texto_union)
    else:
        xi = "{}{}".format(0,xi)
        espacios = ((k - i) / 2) + 1
        llegada = i + espacios
        while espacios < llegada:
            texto_union = texto_union + xi[espacios]
            espacios += 1
        x0 = int(texto_union)

    print "{} - {} -- r{} = 0.{}".format(j,xi,j,x0)
    j += 1

