import math

ri = [0.809,0.042,0.432,0.538,0.225,0.88,0.680,0.772,0.036,0.854,
0.397,0.268,0.821,0.897,0.07,0.721,0.087,0.35,0.779,0.482,
0.136,0.855,0.453,0.197,0.444,0.799,0.809,0.691,0.545,0.857,
0.692,0.055,0.348,0.373,0.436,0.26,0.015,0.834,0.599,0.724,0.564,
0.709,0.946,0.754,0.677,0.128,0.012,0.498,0.6,0.913]

bin = []

n = ri.__len__()
n1 = 0
n0 = 0
co = 0

cont = 0
while cont < n:
    if ri[cont] <= 0.50:
        n0 = n0 + 1
        bin.append(0)
    else:
        n1 = n1 + 1
        bin.append(1)
    cont += 1

cont = 0
while cont < n:
    if (bin[cont] == 1 and bin[cont - 1] != 1) or (bin[cont] == 1 and cont == 0):
        co = co + 1
    elif (bin[cont] == 0 and bin[cont - 1] != 0) or (bin[cont] == 0 and cont == 0):
        co = co + 1
        
    cont += 1

print "Numero de Corridas (Co) = ",co
print "Numero de ri (n) = ",n
print "Numeros de 0 (n0) = ",n0
print "Numeros de 1 (n1) = ",n1
print "Conjunto = ",bin,"\n"


#Formula Para sacar valor Esperado (Mco)
Mco = (2*n0*n1/float(n)) + (1/float(2))
print "Valor Esperado (Mco) = ",Mco

#Formula  para sacar la varianza
O2Co = ((float(2*n0*n1))*((float(2*n0*n1))-n))/((math.pow(n,2))*(n-1))
print "Valor de la Varianza (O2Co) = ",O2Co

#formula para sacar la Estadistica
lo = (((co)-(Mco)))/(math.sqrt(O2Co))
print "El valor de la Estadistica (Lo) = ",lo

