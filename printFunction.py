#Leer un número entero n y luego imprimir los números del 1 al n en una sola línea, sin espacios entre ellos
#lee un entero n
n = int(input("escriba un numero entero"))
#Se recorre la secuencia de números del 1 al n con un ciclo for
for i in range(1, n+1):
    #En cada vuelta, se imprime el número, pero con end = '' para que no haya salto de línea ni espacios
    print(i,end = "")