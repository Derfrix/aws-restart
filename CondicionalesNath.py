saltoL="-------------------------"
########################
edad8=int(input("Cuantos años tienes? "))
if edad8>=65:
    print("tienes descuento por edad, adelante por favor")
elif edad8>=30:
    print("eres mayor de edad, adelante, pronto tendras descuento")
elif edad8>=19:
    print("eres mayor de edad, adelante")
elif edad8>=18:
    print("un recien iniciado, ya eres mayor de edad, adelante")
else:
    print("eres muy chico, vayase")
#########################
print(saltoL)
#########################
edad=int(input("Cuantos años tienes? "))
if edad>=18:
    print("puede votar")
else:
    print("eres muy chico, vayase")
#########################
print(saltoL)
#########################
TempA=int(input("Ingrese la temperatura ºC: "))
if TempA>=100:
    print("su agua esta gaseosa")
elif TempA>=1:
    print("su agua esta liquida")
else:
    print("su agua es solido")
print(saltoL)
Num2=int(input("Ingrese su numero entero: "))
if Num2>=1:
    print("su unmero es positivo")
elif Num2>=0:
    print("su numero es 0")
else:
    print("su numero es negativo")
#########################
print(saltoL)
#########################
print("vamos a evaluar sus dos numeros 👀")
numb1=int(input("ingrese su primer numero: "))
numb2=int(input("ingrese su segundo numero: "))
print(" ")
if numb1>=0 and numb2>=0:
    print(f"ambos numeros {numb1} y {numb2} son positivos")
elif numb1>=0 and numb2<=-1:
    print(f"solo tu primer numero {numb1} es positivo")
elif numb1<=-1 and numb2>=0:
    print(f"solo tu segundo numero {numb2} es positivo")
else:
    print(f"ninguno de tus numero {numb1} y {numb2} es positivo!")
#########################
print(saltoL)
#########################
edadv=int(input("cual es tu edad? "))
credencials=input("credenciales para votar? (si/no):")
a = ("SI", "si","sI","Si")
if edadv>=18 and credencials in a:
    print("puedes votar")
elif edadv<=17 and credencials in a:
    print("no puedes votar y estas detenido 🚨🚓🚨")
else:
    print("no puedes votar")
#########################
print(saltoL)
#########################
print("solo responda si o no")
cc=input("cuando estabas en la playa ¿comiste? :")
blq=input("y te pusiste bloqueador? :")
res=input("y descansaste tambie? :")
a = ("SI", "si","sI","Si")
if cc in a or blq in a or res in a:
    print("ahhh entonces si tuviste vacaciones y no me invito")
else:
    print("no tuviste vacaciones")