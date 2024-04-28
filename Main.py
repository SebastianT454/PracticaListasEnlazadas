from Paciente import *
from ListasEnlazadas import *

def mostrar_menu():
    print("\n----- Menú de Operaciones -----")
    print("1. Inserción manual de paciente")
    print("2. Inserción automatica de pacientes")
    print("3. Atención del paciente con mayor prioridad")
    print("4. Mostrar todos los pacientes")
    print("5. Actualizar la prioridad de un paciente")
    print("6. Terminar el programa")
    print("-----------------------------------")

Dll_Prioritaria = ListaDePrioridad()

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        edad = int(input("Ingrese la edad del paciente: "))
        condicion = input("Ingrese la condición del paciente: ")
        prioridad = int(input("Ingrese el nivel de prioridad del paciente: "))
        paciente = Paciente(nombre, edad, condicion, prioridad)
        Dll_Prioritaria.append(Dll_Prioritaria.head, paciente)
        print(f"Paciente agregado: {paciente}")

    elif opcion == "2":
        Cnt_Pacientes = int(input("Ingrese la cantidad de pacientes que desea: "))
        Pacientes = crear_pacientes_aleatorios(Cnt_Pacientes)

        for paciente in Pacientes:
            Dll_Prioritaria.append(Dll_Prioritaria.head, paciente)

        Dll_Prioritaria.traverse(Dll_Prioritaria.head)

    elif opcion == "3":
        Paciente_con_mayor_prioridad = Dll_Prioritaria.delete_head()
        print(f"Paciente con mayor prioridad atendido: {Paciente_con_mayor_prioridad}")

    elif opcion == "4":
        Dll_Prioritaria.traverse(Dll_Prioritaria.head)

    elif opcion == "5":
        Nombre = input("Ingrese el nombre del paciente cuya prioridad desea actualizar: ")
        Nueva_prioridad = int(input("Ingrese la nueva prioridad: "))

        Dll_Prioritaria.update_node(Dll_Prioritaria.head, Nombre, Nueva_prioridad)

    elif opcion == "6":
        print("¡Programa terminado!")
        break

    else:
        print("Opción inválida. Por favor, ingrese un número válido del menú.")

