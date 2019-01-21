import math
import LibreriaPoker as datos_p

ri_generados = [0.8797,0.3884,0.6289] ## Variable igualda

Nivel_de_Confianza__90,Nivel_de_Confianza__95,poker_5 = datos_p.Nivel_de_Confianza__90,datos_p.Nivel_de_Confianza__95,datos_p.poker_5

def pruebaChi_independencia(estadistico,m):
    nivel_independiente = m - 1
    valor_chi = 0
    print "Estadistico: ",estadistico
    print "M - 1: ",nivel_independiente
    Nivel_de_Confianza_ = int(input('Nivel de Confianza [1 - 90% || 2 - 95%]: '))
    confirmar = True
    while confirmar == True and (Nivel_de_Confianza_ != 1 or Nivel_de_Confianza_ != 2):

        if(Nivel_de_Confianza_ == 1):
            valor_chi = Nivel_de_Confianza__95[nivel_independiente]
            print "Valor Generado de Chi: ",valor_chi
            if(Nivel_de_Confianza__95[nivel_independiente] > estadistico):
                print "{} > {} ".format(Nivel_de_Confianza__95[nivel_independiente],estadistico)
                print "Se acepta que el conjunto ri es independiente"
                break
            else:
                print "{} < {} ".format(Nivel_de_Confianza__95[nivel_independiente],estadistico)
                print "No Se acepta que el conjunto ri es independiente"
                break

        elif(Nivel_de_Confianza_ == 2):
            valor_chi = Nivel_de_Confianza__90[nivel_independiente]
            print "Valor Generado de Chi: ",valor_chi
            if(Nivel_de_Confianza__90[nivel_independiente] > estadistico):
                print('\n'+str(Nivel_de_Confianza__90[nivel_independiente])+' > '+str(estadistico))
                print('\nSe acepta que el conjunto ri es independiente')
                break
            else:
                print('\n'+str(Nivel_de_Confianza__90[nivel_independiente])+' < '+str(estadistico))
                print('\nNo se acepta que el conjunto ri es independiente')
                break
        else:
            print "Esa opcion no existe"
            confirmar = False
        
        if confirmar == False:
            Nivel_de_Confianza_ = int(input('Ingresa Nuevamente Nivel de Confianza [1 - 90% || 2 - 95%]: '))
            confirmar = True


def conversor_de_cadena(num_str):
    conversor_parlante = ''+str(num_str)
    while (len(conversor_parlante) < 4):
        conversor_parlante = conversor_parlante + '0'
    i,k = 0,[]
    while(i < len(conversor_parlante)):
        k.append(int(conversor_parlante[i]))
        i = i + 1
    l,n = 0,0
    while(l < len(k)):
        n = 0
        while(n < len(k)):
            if(k[l] < k[n]):
                aux = k[l]
                no = k[n]
                k[n] = aux
                k[l] = no
            n = n + 1
        l = l + 1
    return k

def Singularidad_generada(os):
    singularidad,regreso,retorno_valor = "",0,""
    for al in os:
        singularidad = singularidad + str(al)
    while regreso < len(os):
        if int(singularidad[regreso-1]) != int(singularidad[regreso]):
            retorno_valor = retorno_valor + " "
        retorno_valor = retorno_valor + singularidad[regreso]
        regreso = regreso + 1
    return retorno_valor.split()

def Asigna_clasific(li):
    poker_variable_almacenada = ''
    if len(li) == 4:
        poker_variable_almacenada = 'TD'
    elif len(li) == 3:
        poker_variable_almacenada = '1P'
    elif len(li) == 2:
        per1,per2 = str(li[0]),str(li[1])
        if len(per1) == 2 and len(per2) == 2:
            poker_variable_almacenada = '2P'
        else:
            poker_variable_almacenada = 'T'
    elif len(li) == 1:
        poker_variable_almacenada = 'PK'
    return poker_variable_almacenada

def Casos(numero):
    return Asigna_clasific(Singularidad_generada(conversor_de_cadena(numero)))

def Convertir_string(ri):
    conj_str,conj_casif = [],[]
    for i in ri:
        string = str(i)
        conj_str.append(string[2:6])
    for letra in conj_str:
        conj_casif.append(Casos(letra))
    print "Poker Generado: ",conj_casif
    return conj_casif

#funcion que contaviliza los casos
def conteo_casos(dato_obtenido):
    TD,P,P2,T,PK = 0,0,0,0,0
    for k in dato_obtenido:
        if 'TD' == k:
            TD = TD + 1
        elif '1P' == k:
            P = P + 1
        elif 'T' == k:
            T = T + 1
        elif '2P' == k:
            P2 = P2 + 1
        elif 'PK' == k:
            PK = PK + 1
    return [TD,P,P2,T,PK]


def calculo(valores,conteo,num_datos):
    print "Sistema de conteo: ",conteo
    estadisticas,Chi_Generado_poker,j,i = [],[],0,0
    while (i < len(conteo)):
        ei = round(float(valores[i] * num_datos),4)
        x = round(float(pow(ei-conteo[j],2)/ei),4)
        estadisticas.append(ei)
        Chi_Generado_poker.append(x)
        j += 1
        i += 1
    print "Chi Generado poker: ",Chi_Generado_poker
    print "Estadistica: ",estadisticas
    suma = 0
    for val in Chi_Generado_poker:
        suma = suma + val
    pruebaChi_independencia(suma,len(Chi_Generado_poker))

def inicio_poker(datos):
    calculo(poker_5,conteo_casos(Convertir_string(datos)),len(datos))

inicio_poker(ri_generados)