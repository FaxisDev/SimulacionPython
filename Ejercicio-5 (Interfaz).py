import sys
import math
from Tkinter import *
 
def MiEvento_Boton1():
    try:
        intervalos_generados = [0]
        lista = []

        x0 = int(entrada_texto.get())
        a = int(entrada_texto2.get())
        m = int(entrada_texto3.get())

        #funciones
        i = 1
        x1 = 0
        llegada = x0
        over = ""

        while not llegada == x1:
            x1 = ((x0)*(a)) % m
            r = float(x1) / m
            lista.append(r)
            over = "x{} = (({})*({})) / {}   r{} = {}".format(i,x0,a,m,i,r)
            lis = Label(ventana, text=over)
            lis.grid(column=2+i, row=2, sticky=(W,E))
            x0 = x1
            i += 1
        x1 = ((x0)*(a)) % m
        r = float(x1) / m

        conjunto_lista.config(text=lista)
        ##### Aqui comienza la Chi cuadrada o esa mierda
        #Comenzar a obtener valores
        n = lista.__len__()
        m = round(math.sqrt(n))
        ##Imprimir N
        m2 = Label(ventana, text="El valor de N = ")
        m2.grid(column=1, row=7, sticky=(W,E))
        m1 = Label(ventana, text=n)
        m1.grid(column=2, row=7, sticky=(W,E))
        ##Imprimrir Raiz M
        m3 = Label(ventana, text="Raiz de M = ")
        m3.grid(column=1, row=8, sticky=(W,E))
        m4 = Label(ventana, text=m)
        m4.grid(column=2, row=8, sticky=(W,E))
        #Formulas!
        intervalo = 1/m
        ei = (n/m)
        rectas = 0

        #Procedimiento <> Algoritmo > Zadot
        while rectas <= 1:
            identificador_intervalos_generados = 0
            conta = 0
            while conta < n:
                if (lista[conta] >= rectas) and (lista[conta] <= (rectas + intervalo)):
                    identificador_intervalos_generados += 1
                conta += 1
            if not (rectas + intervalo) > 1:
                intervalos_generados.append(identificador_intervalos_generados)
            rectas = rectas + intervalo
        
        #Una vez mas pero para visualizar mi tabla
        rectas = 0
        conta = 1
        x_suma = 0

        l1 = Label(ventana, text="InterValos")
        l1.grid(column=1, row=10, sticky=(W,E))
        
        l2 = Label(ventana, text="Io Cantidad")
        l2.grid(column=2, row=10, sticky=(W,E))

        l3 = Label(ventana, text="Ei = (n/m)")
        l3.grid(column=3, row=10, sticky=(W,E))

        l4 = Label(ventana, text="X!")
        l4.grid(column=4, row=10, sticky=(W,E))

        while rectas + intervalo <= 1:
            xri = (pow((ei - intervalos_generados[conta]),2)) / ei
            x_suma = x_suma + xri

            inter = " {} - {}".format(rectas,(rectas + intervalo))
            l1 = Label(ventana, text=inter)
            l1.grid(column=1, row=(10+conta), sticky=(W,E))

            io_var = intervalos_generados[conta]
            print io_var
            l2 = Label(ventana, text=io_var)
            l2.grid(column=2, row=(10+conta), sticky=(W,E))

            l3 = Label(ventana, text=ei)
            l3.grid(column=3, row=(10+conta), sticky=(W,E))

            l4 = Label(ventana, text=xri)
            l4.grid(column=4, row=(10+conta), sticky=(W,E))

            conta += 1
            rectas = rectas + intervalo

        l5 = Label(ventana, text="Suma total de X! es {} ".format(x_suma))
        l5.grid(column=1, row=(10+conta+1), sticky=(W,E))

    except ValueError:
        conjunto_lista.config(text="Introduce un numero!")
 
 
app = Tk()
app.title("Generador de N SeudoAleatorios >< Con una variable (Ejercicio 5)")
 
#Ventana Principal
ventana = Frame(app)
ventana.grid(column=0, row=0, padx=(250,250), pady=(20,20))
ventana.columnconfigure(0, weight=2)
ventana.rowconfigure(0, weight=2)
 
conjunto_lista = Label(ventana, text="")
conjunto_lista.grid(column=1, row=3, sticky=(W,E))
 
boton = Button(ventana, text="Correr", command=MiEvento_Boton1)
boton.grid(column=2, row=5)
 
men1 = Label(ventana, text="Ingresa valor x0: ")
men1.grid(column=1, row=1, sticky=(W,E))
valor = ""
entrada_texto = Entry(ventana, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)

men2 = Label(ventana, text="Ingresa constante A: ")
men2.grid(column=3, row=1, sticky=(W,E))
valor2 = ""
entrada_texto2 = Entry(ventana, width=10, textvariable=valor2)
entrada_texto2.grid(column=4, row=1)

men3 = Label(ventana, text="Ingresa Modulo M: ")
men3.grid(column=5, row=1, sticky=(W,E))
valor3 = ""
entrada_texto3 = Entry(ventana, width=10, textvariable=valor3)
entrada_texto3.grid(column=6, row=1)
app.mainloop()