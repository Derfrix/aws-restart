saltoL="-------------------------"
#########################
print(saltoL)
#########################
print ("usando for")
for i in range(1,11):
    print(i, end=" ")
print(" ")
#########################
print(saltoL)
#########################
print("usando while")
contador = 1
while contador <= 5:
    print(contador, end=" ")
    contador += 1
print(" ")
#########################
print(saltoL)
#########################
milistadetipos = [99, 33, 66.6, True, "Hola", "369"]
for item in milistadetipos:
    print("{} esto es del tipo de dato {}".format(item,type(item)))
#########################
print(saltoL)
#########################