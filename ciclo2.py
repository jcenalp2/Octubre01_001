#ingresar n números donde n es un numero ingresado por el teclado (utilice ciclo while). 
#Mostrar cuantos son positivos, cuantos son negativos y cuantos son iguales a cero

veces=int(imput("Cuántos numeros desea ingresar ?: "))
x=1
while(x<=veces):
    num=int(imput("Digite un numero: "))
    if(num>0):
        pos=pos+1
    elif (num<0):
        neg=neg+1
    else:
        ceros=ceros+1
    x=x+1
print("La cantidad de numeros positivos es: "+ str(pos)+ 
"\nLa cantidad de numeros negativos es: "+ str(neg) + 
"\nLa cantidad de numeros iguales a ceros es: "+ str(ceros))
