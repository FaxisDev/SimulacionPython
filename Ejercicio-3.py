#Semillas
x0 = input("Ingresa Semilla 1: ")
a = input("Constante de multiplicacion: ")

#digitos a agarrar
digitos = input("Total de digitos a tomar: ")

#Ciclos
ciclos = input("Total de ciclos: ")

xi = x0 * a
contador = str(xi)
#Para mantener el valor
reemplazo = 0
j = 1
#Constante
constante = a
while j <= ciclos:
    texto_union = ""
    i = 0

    #Algunas mierdas
    xi = x0 * a
    contador = str(xi)

    for ver in contador:
        i += 1

    reemplazo = constante
    if (i - digitos) % 2 == 0:
        espacios = (i - digitos) / 2
        llegada = espacios + digitos
        while espacios < llegada:
            texto_union = texto_union + contador[espacios]
            espacios += 1
        a = int(texto_union)
    else :
        xi = "{}{}".format(0,xi)
        espacios = ((i - digitos) / 2) 
        llegada = espacios + digitos
        while espacios < llegada:
            texto_union = texto_union + contador[espacios]
            espacios += 1
        a = int(texto_union)

    print "{} - {} x {} = {} r{} = 0.{}".format(j,x0,reemplazo,contador,j,a)
    x0 = reemplazo

    j += 1
