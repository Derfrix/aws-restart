#un comentario que se va a ignorar se hace con gato/hashtag/numeral
# este es ek simbolo que hace que todo sea un comentario #######
"""
comnetario multilinea 
esto se ignora por tener 
3 comiillas abiertar 
y cerradas
"""
### tipos de datos ###
## int/entero/integral/integer
## un numero natural que puede estar entre -n a n
## debemos almacenar en una variable
## la variable es la representacion de un valor
## que necesita identificacion
"""
la variable es la representacion de un valor 
el nombre es un identificador

No puedo
*No puedo llamar a una variable incumpliendo
*No puede llamar a una variable con un numero/ no puede iniciar con un numero
ejem: 2Var / esta prohibido
*No puede tener caracteres especiales
ejem: var#$%le
*No puede contener espacio
ejem: Vari able
*No puede llamar una variable con una palabra reservada
#(buscar ista de palabras reservadas/ for, while, or, try, except, buscar mas...)

Si puedo:
*utilizar numeros en medio o al final de las variables
ejem: vari4bl3
*si puedo utilizar guion bajo:
ejem: Vari_Able
*si puede llarmase solo guion bajo
ejem: _
*Puedo difertenciar las mayusculas y las minusculas
ejem: Var =! var
"""
# python intuye el tipo de dato
## para nombrar una variable debo asignarle un valor asi:
# identificador = valor

num=2
num_entero=5
n=10
N=20
NUM=7

print(n)
print(N) #son diferentes

# vemo el tipo de dato con type()
print(type(num)) # <class 'int'>
print(num)

resultado=num+N-n-num_entero+NUM

print(resultado)

Resultado22=num+NUM

print(Resultado22)

#Formna practica de imprimir variables 
# uso del f-string 

print(f"hola, la suma de {num} y el valor {NUM} dando como resultado {Resultado22}")

## float son numeros decimales 
# se separa el entero del decimal con punto

num=4.5
num2=3.2

RR=num*num2

print(type(num))
print(num)

print(f"hola, la suma de {num} y el valor {num2} dando como resultado {RR}")

## complex : Complejo o imaginario
# se representa con una j al final del numero
# vienen del problema de raiz de menos 1

num=4j
num2=2j

resultado44=num-num2

print(f"Hola, reste el valor {num} y el valor {num2} dando como resultado {resultado44}")
print(f"El tipo de dato de {num} es {type(num)}")

## ejemplos

num=10
num2=5

suma=num+num2
restarr=num-num2
multi=num*num2
division=num/num2 ##esto sera un float como resultado

# hacer una division entera (omitiendo los decimales) con //
division_entera=num//num2

print(
    suma,
    restarr,
    multi,
    division,
    division_entera
    )
## Residuo
# Se realizara una división, pero el resultado fuera lo que sobró
# de la división entera

modulo=num%2

print(f"modulo: {num}  % 2 es {modulo}")

## Exponente: elevado **

elevado=3**2 

print(f"3 elevado a la 2 es {elevado}")

c=5

print (c ** c) 