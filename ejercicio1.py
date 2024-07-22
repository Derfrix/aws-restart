"""
Calculadora automatica de 2 numeros 

realizar todas las opreciones posibles 
(+,-,*,**,/,//,%)
mostrandolo de forma clara
"""
num = int(input("Ingresa el primer número: ")) # 5
num2 = int(input("Ingresa el segundo número: ")) # 2

# al ser strings se concatenarán (unen)
suma = num + num2
resta = num - num2
multip = num * num2
elevado = num ** num2
division = num / num2
divsion_entera = num // num2
porcen = ((num*num2)/(100))
resultadoPor = (((100-num2)*num)/(100))
NewRes=porcen+resultadoPor

print(f"La suma de {num} y {num2} es {suma}")
print(f"La resta de {num} y {num2} es {resta}")
print(f"La multiplicacion de {num} y {num2} es {multip}")
print(f"cuando se eleva {num} a {num2} es {elevado}")
print(f"La division de {num} y {num2} es {division}")
print(f"La division con numeros enteros de {num} y {num2} es {divsion_entera}")
print(f"El %{num2} de {num} es {porcen}")
print(f"El {num} si le descontamos {num2}% es {resultadoPor}")
print(f"el resultado de {porcen} mas {resultadoPor} es igual a {NewRes}")