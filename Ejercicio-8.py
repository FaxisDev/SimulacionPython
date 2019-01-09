import math

conj_ri= [0.8797,0.3884,0.6289,0.8750,0.5999,0.8589,0.9996,0.2415,0.3808,0.9606,
       0.9848,0.3496,0.7977,0.5844,0.8147,0.6431,0.7387,0.5613,0.0318,0.7401,
       0.4557,0.1592,0.8536,0.8846,0.3410,0.1492,0.8681,0.5291,0.3188,0.5992,
       0.9170,0.2204,0.5991,0.5461,0.5739,0.3254,0.0856,0.2258,0.4603,0.5027,
       0.8376,0.6235,0.3581,0.0288,0.1525,0.2006,0.2420,0.4272,0.6360,0.0954]

confi_90 = {
	1:2.706,2:4.605,3:6.251,4:7.779,5:9.236,6:10.645,7:12.017,8:13.362,9:14.684,10:15.987,
	11:17.275,12:18.549,13:19.812,14:21.064,15:22.307,16:23.542,17:24.769,18:25.989,19:27.204,20:28.412,
	21:29.615,22:30.813,23:32.007,24:33.196,25:34.382,26:35.563,27:36.741,28:37.916,29:39.087,30:40.256,
	40:51.805,50:63.167,60:74.397,70:85.527,80:96.578,90:107.565,100:118.498
	       }
confi_95 = {
	1:3.841,2:5.991,3:7.815,4:9.488,5:11.070,6:12.592,7:14.067,8:15.507,9:16.919,10:18.307,
	11:19.675,12:21.026,13:22.362,14:23.685,15:24.996,16:26.296,17:27.587,18:28.869,19:30.144,20:31.410,
	21:32.671,22:33.924,23:35.172,24:36.415,25:37.652,26:38.885,27:40.113,28:41.337,29:42.557,30:43.773,
	40:55.758,50:67.505,60:79.082,70:90.531,80:101.879,90:113.145,100:124.342
	       }

num_Poker4 = [0.5040,0.4320,0.0270,0.0360,0.0010]

def pruebaChi_independencia(estadistico,m):
  xa = m - 1
  print('\nEstadistico: '+str(estadistico))
  print('\nm - 1 = '+str(xa))
  confi = int(input('Nivel de connfiaza para independencia[%]: '))
  valor_chi = 0
  if(confi == 95):
	  valor_chi = confi_95[xa]
	  print('\nValor chi: '+str(valor_chi))
	  if(confi_95[xa] > estadistico):
		  print('\n'+str(confi_95[xa])+' > '+str(estadistico))
		  print('\nSe acepta que el conjunto ri es independiente')
	  else:
		  print('\n'+str(confi_95[xa])+' < '+str(estadistico))
		  print('\nNo se acepta que el conjunto ri es independiente')
  if(confi == 90):
	  valor_chi = confi_90[xa]
	  print('\nValor chi: '+str(valor_chi))
	  if(confi_90[xa] > estadistico):
		  print('\n'+str(confi_90[xa])+' > '+str(estadistico))
		  print('\nSe acepta que el conjunto ri es independiente')
	  else:
		  print('\n'+str(confi_90[xa])+' < '+str(estadistico))
		  print('\nNo se acepta que el conjunto ri es independiente')


print(conj_ri)

#funcion que convierte la cadena en una lista de caracteres separados, organizandolos y de menor a mayor. 
def Ale(num_str):
    arm = ''+str(num_str)
    while (len(arm) < 4):
        arm = arm + '0'
    i,k = 0,[]
    while(i < len(arm)):
        k.append(int(arm[i]))
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

#funcion que reorganiza la lista de caracteres y acomoda los caracteres en pares, triadas y diferentes.
def Ingrit(os):
    mmo, exo,dt = '',0,''
    for al in os:
        mmo = mmo + str(al)
    while exo < len(os):
        if int(mmo[exo-1]) != int(mmo[exo]):
            dt = dt + ' '
        dt = dt + mmo[exo]
        exo = exo + 1
    return dt.split()

#funcion que asigna la clasificasion a la lista de caracteres
def Asigna_clasific(li):
 nn = ''
 if len(li) == 4:
  nn = 'TD'
 elif len(li) == 3:
  nn = '1P'
 elif len(li) == 2:
  per1,per2 = str(li[0]),str(li[1])
  if len(per1) == 2 and len(per2) == 2:
    nn = '2P'
  else:
    nn = 'T'
 elif len(li) == 1:
  nn = 'PK'
 return nn

#funcion que manda a llamar las funciones: Ale, Ingrit y Asigna_clasific.
def Casos(num):
    az = Ale(num)
    ver = Ingrit(az)
    tx = Asigna_clasific(ver)
    return tx

#funcion que convierte el numero en cadena tomando los digitos despues
#de punto decimal y manda a llamar la funcion Casos.
def Convertir_string(ri):
    conj_str,conj_casif = [],[]
    for i in ri:
        string = str(i)
        conj_str.append(string[2:6])
    for letra in conj_str:
        conj_casif.append(Casos(letra))
    print('\n')
    print(conj_casif)    
    return conj_casif

#funcion que contaviliza los casos
def conteo_casos(emm):
    TD,P,P2,T,PK = 0,0,0,0,0
    for k in emm:
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
#funcion que realiza el calculo para obtener el estadistico
def calculo(valores,conteo,num_datos):
    print('\n'+str(conteo))
    est,chi,j,i = [],[],0,0
    while (i < len(conteo)):
        ei = round(float(valores[i] * num_datos),4)
        x = round(float(pow(ei-conteo[j],2)/ei),4)
        est.append(ei)
        chi.append(x)
        j += 1
        i += 1
    print('\n'+str(chi))
    print('\n'+str(est))
    suma = 0
    for val in chi:
        suma = suma + val
    pruebaChi_independencia(suma,len(chi))
#funcion que da inicio a la prueba mandadno a llamar a las funciones
#Comvertir_string, conteo_casosy calculo.
def inicio_poker(datos):
    a = Convertir_string(datos)
    b = conteo_casos(a)
    c = num_Poker4
    d = len(datos)
    e = calculo(c,b,d)



inicio_poker(conj_ri)



