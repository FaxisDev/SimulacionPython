#Variables
x0 = input("Ingresa la semilla: ")
a = input("Ingresa la constante a: ")
m = input("Ingresa el modulo m: ")

#funciones
i = 1
x1 = 0
llegada = x0

while not llegada == x1:
    x1 = ((x0)*(a)) % m
    r = float(x1) / m
    print "x{} = (({})*({})) / {}   r{} = {}".format(i,x0,a,m,i,r)
    x0 = x1
    i += 1
x1 = ((x0)*(a)) % m
r = float(x1) / m
print "x{} = (({})*({})) / {}   r{} = {}".format(i,x0,a,m,i,r)