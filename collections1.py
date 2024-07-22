##boleano,bool##
#tipo de dato primitivos 
#son valores de true o false

comer = True
dormir = False
a = ("comer", "Comer")
b = ("dormir", "Dormir")

print(f"La variable comer tiene el valor {comer} y es de tipo {type(comer)}")


res = input("¿Qué desea hacer, comer o dormir? ")

if res in a:
    print("Puedes comer")
elif res in b:
    print("No puedes dormir")
else:
    print("Opción no válida")
"""
#Tipos de datos compuestos
#Colecciones
"""
###########################
#### LISTA ################
###########################

"""
#Es una colección ordenada de valores
#* Se define con [] y separa sus elementos con ,
#* Los elementos pueden ser de cualquier tipo de dato
#personas = ["Anahi", "David", "Ariel", 34, True, False]
#* Mantiene un orden (Vale la pena aclarar)
"""

personas = ["Anahi", "David", "Ariel"]
numeros = [100, 95, 82]
myFruitList = ["apple", "banana", "cherry"]

print(f"La lista de frutas es {myFruitList}")
print(f"El tipo de dato es {type(myFruitList)}")

# Si quiero imprimir un elemento (banana) debo hacerlo por su índice
print(f"El segundo elemento es {myFruitList[2]}")
# Un error típico es intentar acceder a un índice que no existe
#print(myFruitList[5])
# IndexError: list index out of range

# Puedo cambiar el valor de los elementos
# Quiero cambiar banana por coco (indice 1)
myFruitList[1] = input("con cual desea cambiar: ")

print(f"La nueva lista es {myFruitList}")

##tupla
#creando una tupla
Mytupla = (1, 2, 3, "hola", True)

#accediendo a elementos
print(f"En mi lista tupla el ubicado en primera posicion es * {Mytupla[0]} *")  # Salida: 1
print(f"y el ubicado en cuarta posicion es * {Mytupla[3]} *")  # Salida: hola

#longitud de la tupla
print(f"la lista Tupla es de un largo de {len(Mytupla)}")  # Salida: 5
##la tupla no se puede cambiar

"""
#Diccionarios
#Colección de valores guardados con un modelo llave valor
#El diccionario se define con {} y elementos separados por ,
#Cada elemento se ve llave : valor
#La llave podría ser un string o entero
#El valor podría ser de cualquier tipo de dato
"""

persona={"Nombre": "Julian Vasquez", "Ciudad": "Santiago", "Edad": 26}

print(persona)
print(type(persona))
print(persona["Ciudad"])
persona["Ciudad"]="viña del Mar"
print(persona["Ciudad"])
persona["Ciudad"] = input("Cuál es tu ciudad? ")
print(persona["Ciudad"])

"""
#Ejercicio 1
#Genera una lista de tu top 5 de canciones favoritas
#e imprime la primera y última canción

#Ejercicio 2
#Imprime un diccionario que contenga los colores de su ropa
#* polera azul
#* pantalón azul
#* zapatos negros
"""
ListaDeCanciones=("Something About Us - Daft Punk","Blinding Lights - The Weeknd","Chop Suey! - System of a Down","Holy Diver - Dio","Numb - Linkin Park")
print (f"en el top 5 la primera cancion es {ListaDeCanciones[0]} y la que remonto a 5to lugar es {ListaDeCanciones[4]}")

ColRop={"Polera": "Naranja", "Pantalon": "bermellón", "Zapatos": "Eburnean"}
print ("la polera es de color") 
print(ColRop["Polera"])
print ("el pantalon es de color") 
print(ColRop["Pantalon"])
print ("los zapatos son de color") 
print(ColRop["Zapatos"])