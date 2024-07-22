MyString = "Hola! Soy Optimus Prime"
print (f"el valor de mi string es {MyString} y es de tipo {type(MyString)}")

##operador
#no se pueden hacer operaciones aritmetica

nombre = "Optimus"
apellido = "Prime"

nombre_completo = nombre + " " + apellido #es una concatenacion

print(f"mi nombre completo es {nombre_completo}")


##función de entrada por teclado
# input()
# frena el programa y espera que el usuario ingrese algo por teclado
# por defecto el valor que se recibe es de tipo string

nombre2 = input("Ingresa el nombre: ")

apellido2 = input("Ingresa tu apellido: ")

nombre_completo2 = nombre2 + " " + apellido2

print(f"Hola, tu nombre es: {nombre_completo2}")

print(f"Tu nombre es: {nombre2}")

# CONVERSIÓN DE TIPOS DE VARIABLE
# CASTING o CASTEO

# Puedo convertir un string a int o float así

variable = "2"
numero_convertido = int(variable)

print(f"La variable era de tipo {type(variable)} y ahora es {type(numero_convertido)}")


"""
Conversiones

int()
float()
complex()
str()

"""

# Voy a sumar dos números
# Si no convierto lo que recibo en input será string
# convierto la entrada de input a int
num = int(input("Ingresa un número: ")) # 5
num2 = int(input("Ingresa otro número: ")) # 2

# al ser strings se concatenarán (unen)
resultado = num + num2

print(f"La suma de {num} y {num2} es {resultado}")

