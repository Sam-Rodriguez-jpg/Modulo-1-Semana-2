#1. Ingresa una lista de calificaciones y calculo para ver si el estudiante aprobo o reprobo
calificacion = []

while True:
    try:
        notas = float(input("Dame un número del 0 - 100: "))
        if notas < 0 or notas > 100:
            print("Número inválido.")
        else:
            calificacion.append(notas)
            resultado = "Ganaste!" if notas >= 60 else "Reprobaste."
            print(resultado)
        
#2. Preguntar si quiere agregar más notas
        pregunta = input("¿Deseas agregar otra nota? (Si/No): ").lower()
        if pregunta != "si":
            break
    
    except ValueError:
        print("Caracter inválido.")

promedio = 0

while True:
    try:
        pregunta = input("La nota se agrego, desea agregar otra nota? (Si/No): ").lower()
        if pregunta != "Si":
            break
        else:
            notas = float(input("Dame un numero del 0 - 100: "))
        if notas < 0 or notas > 100:
            print("Numero invalido.")
        elif notas >= 0 and notas < 60:
            print("Reprobaste.")
            calificacion.append(notas)
            break
        else:
            print("Ganaste!")
            calificacion.append(notas)
            break
    
    except ValueError:
        print("Caracter invalido.")


#3. Calcular el promedio
    for number in calificacion:
        promedio += number
    resultado = round(promedio / len(calificacion, 1))

print(f"Así quedaron las calificaciones: {calificacion}")
print(f"Este es el promedio de la lista {resultado}") 

#4. Preguntar al usuario por un valor
while True:
    valor = float(input("Introduce un valor de la lista: "))
    if valor <= 0 or valor > 100:
        print ("Tu numero no es válido, intentalo de nuevo.")
    if valor not in calificacion:
            print("Tu valor ingresado no está en las calificaciones, intenta de nuevo")
    else :
        break

#5. Decirle al usuario cuantas notas en la lista son mayores que ese valor
contador = 0

for number in calificacion:
    if number > valor:
        contador += 1
print(f"La cantidad de {contador} mayores que {valor}.")


#6. Preguntar al usuario por una nota y decirle cuantas veces aparece
while True:
    cantidad_de_veces = float(input("Dime una nota: "))
    if cantidad_de_veces <= 0 or cantidad_de_veces > 100:
        print("Numero invalido, intentalo de nuevo.")
    if cantidad_de_veces not in calificacion:
        print("Esta nota no se encuentra las calificaciones, intentalo de nuevo.")
    else: 
        break

if cantidad_de_veces in calificacion:
    contar = calificacion.count(cantidad_de_veces)
print(f"Tu nota aparece {contar} veces en la lista.")