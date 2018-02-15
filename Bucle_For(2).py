#coding: utf-8
num1=input("indique su numero entero mayor que cero aqui:")

while (num1<=0):
	print ("¡Le he pedido un numero entero mayor que "+str(num1)+"!")
	num1= input("introduce un numero entero mayor "+str(num1)+":")

for i in range (1,num1):
	if num1%i==0:
	  print i 
print " fin de programa."
	
