#coding: utf-8
#coding: utf-8
num1=input("¿Cuantos valores vas a introducir:?")
while (num1<=0):
    print ("¡Le he pedido un numero entero mayor que "+str(num1)+"!")
    num1= input("introduce un numero entero mayor "+str(num1)+":")

num2=input("Escriba un numero:")

for i in range ( 1,num1+1):
    sup = input("introduce un numero mas grande que "+str(num2)+":")
    if ( sup<= num2):
       print " no es mayor"

print "Programa terminado"
