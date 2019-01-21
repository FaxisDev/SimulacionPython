import math

generador_resultados = [0.809,0.042,0.432,0.538,0.225,0.88,0.680,0.772,0.036,0.854,
0.397,0.268,0.821,0.897,0.07,0.721,0.087,0.35,0.779,0.482,
0.136,0.855,0.453,0.197,0.444,0.799,0.809,0.691,0.545,0.857,
0.692,0.055,0.348,0.373,0.436,0.26,0.015,0.834,0.599,0.724,0.564,
0.709,0.946,0.754,0.677,0.128,0.012,0.498,0.6,0.913]

contador_almacenado = []
contador_n_1 = 0 #Inician en 0
contador_n_0 = 0 #Inician en 0
for valor_obtenido in generador_resultados:
    if valor_obtenido >= 0.50:
        contador_n_1 += 1
        contador_almacenado.append(1)
    else:
        contador_n_0 += 1
        contador_almacenado.append(0)

incremento = 0
corridas = 0

while incremento < generador_resultados.__len__():
    if (contador_almacenado[incremento] == 1 and contador_almacenado[incremento - 1] != 1) or (contador_almacenado[incremento] == 1 and incremento == 0):
        corridas += 1
    elif (contador_almacenado[incremento] == 0 and contador_almacenado[incremento - 1] != 0) or (contador_almacenado[incremento] == 0 and incremento == 0):
        corridas += 1
        
    incremento += 1
print "Conjuntos de 0/1: ",contador_almacenado
print "\nCorridas: {}, Cantidad: {}, N Ceros: {}, N Unos: {}".format(corridas,generador_resultados.__len__(),contador_n_0,contador_n_1)


cantidad_esperada = (2*contador_n_0*contador_n_1/float(generador_resultados.__len__())) + (1/float(2))
valor_varianza = ((float(2*contador_n_0*contador_n_1))*((float(2*contador_n_0*contador_n_1))-generador_resultados.__len__()))/((math.pow(generador_resultados.__len__(),2))*(generador_resultados.__len__()-1))
valor_estadistica = (((corridas)-(cantidad_esperada)))/(math.sqrt(valor_varianza))

print "Cantidad Esperada: {}, Varianza: {}, Estadistica: {}".format(cantidad_esperada,valor_varianza,valor_estadistica)
