import random

print("Bienvenido! Este es el azombroso programa adivinador!!")
print("Las reglas son simples. pensare un numero y tu tienes que adivinarlo!.")
print("Eso es todo!")
print("...🧙️")
print("Ya tengo un numero 👀✨")

Mn=random.randint(1, 100)
Adivino=False
intento=0
max_intento=8

while not Adivino and intento < max_intento:
    Yn=int(input("Ahora, bien, dinos tu numero: "))
    intento += 1

    if Yn == Mn:
        print(f"Lo has logrado! Tu numero {Yn} es el mismo que pensaba!")
        print("🎉🎊 Has Ganado! 🎉🎊")
        print(f"Lo has logrado en tan solo {intento} intentos")
        Adivino = True
    elif Yn > Mn:
        print("Más abajo.")
    elif Yn < Mn:
        print("Más arriba.")

if not Adivino:
    print(f"Lo siento 😢")  
    print(f"Has agotado tus {max_intento} intentos.")
    print(f"El numero era {Mn}.")