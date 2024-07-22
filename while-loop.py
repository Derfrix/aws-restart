import random

print("Bienvenido! Este es el azombroso programa adivinador!!")
print("Las reglas son simples. pensare un numero y tu tienes que adivinarlo!.")
print("Eso es todo!")
print("...🧙️")
print("Ya tengo un numero 👀✨")

Mn = random.randint(1, 100)
Adivino = False
intento = 0
max_intento = 7
max_intentoFallas = 3

while not Adivino and intento < max_intento:
    intentoF = 0
    while intentoF < max_intentoFallas:
        try:
            Yn = int(input("Ahora, bien, dinos tu numero: "))
            break
        except ValueError:
            print("Por favor, ingresa un numero valido.")
        intentoF += 1

    intento += 1

    if intentoF == max_intentoFallas:
        print("Creo que has fallado a proposito 😕")
        break

    if Yn == Mn:
        print(f"Lo has logrado! Tu numero {Yn} es el mismo que pensaba!")
        print("🎉🎊 Has Ganado! 🎉🎊")
        print(f"Lo has logrado en tan solo {intento} intentos")
        Adivino = True
    elif Yn > Mn:
        print("Más abajo.")
    elif Yn < Mn:
        print("Más arriba.")

if not Adivino and intentoF < max_intentoFallas:
    print(f"Lo siento 😢")
    print(f"Has agotado tus {max_intento} intentos.")
    print(f"El numero era {Mn}.")
elif not Adivino and intentoF == max_intentoFallas:
    print(f"Lo siento 😢")
    print(f"Has agotado tus {max_intentoFallas} intentos de fallas.")
    print(f"El numero era {Mn}.")