#Semillas
x0 = input("Ingresa Semilla 1: ")
x1 = input("Ingresa Semilla 2: ")

#digitos a agarrar
digitos = input("Total de digitos a tomar: ")

#Ciclos
ciclos = input("Total de ciclos: ")

xi = x0 * x1
contador = str(xi)
#Para mantener el valor
reemplazo = 0
j = 1
while j <= ciclos:
    texto_union = ""
    i = 0

    #Algunas mierdas
    xi = x0 * x1
    contador = str(xi)

    for ver in contador:
        i += 1

    reemplazo = x1
    if (i - digitos) % 2 == 0:
        espacios = (i - digitos) / 2
        llegada = espacios + digitos
        while espacios < llegada:
            texto_union = texto_union + contador[espacios]
            espacios += 1
        x1 = int(texto_union)
    else :
        xi = "{}{}".format(0,xi)
        espacios = ((i - digitos) / 2) 
        llegada = espacios + digitos
        while espacios < llegada:
            texto_union = texto_union + contador[espacios]
            espacios += 1
        x1 = int(texto_union)

    print "{} - {} x {} = {} r{} = 0.{}".format(j,x0,reemplazo,contador,j,x1)
    x0 = reemplazo

    j += 1