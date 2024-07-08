print("""
¿Que desea realizar?

1) Retornar todo el texto en mayúsculas
2) Retornar todo el texto en minúsculas
3) Retornar los dos primeros caracteres del texto
4) Retornar los dos últimos caracteres del texto
5) Retornar la cantidad de veces que se repite el último caracter
6) Retornar el texto invertido

""")
opcion = int(input("Escoja una opcion: "))
n = input("Ingrese su texto: ")

if opcion == 1:
    print("El texto en mayúsculas es: ", n.upper())
elif opcion == 2:
    print("El texto en minúsculas es: ", n.lower())
elif opcion == 3:
    print("Los dos primeros caracteres del texto son: ", n[0:2])
elif opcion == 4:
    print("Los dos últimos caracteres del texto son: ", n[-2:])
elif opcion == 5:
    n1 = n[-1]
    count = 0
    for i in n:
        if i == n1:
            count += 1
    print(f"La cantidad de veces que se repite el ultimo caracter es: {count}")
elif opcion == 6:
    print("El texto invertido es: ", n[::-1])
