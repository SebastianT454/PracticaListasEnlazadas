import random

class Paciente:
    def __init__(self, nombre, edad, condicion, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.condicion = condicion
        self.prioridad = prioridad

        # Validar la prioridad
        self.validar_prioridad()

    def validar_prioridad(self):
        if not isinstance(self.prioridad, int) or self.prioridad < 1:
            raise ValueError("La prioridad debe ser un entero mayor o igual a 1")

    def __str__(self):
        return f"Paciente: {self.nombre}, Edad: {self.edad}, Condición: {self.condicion}, Prioridad: {self.prioridad}"


def crear_pacientes_aleatorios(CantidadPacientes):
    Nombres = ["Juan Martinez","Laura Vargas","Alejandro Rojas","Ana Hernandez","Carlos Gonzalez","Sofia Diaz","Pablo Munoz",
    "Valentina Morales","Javier Perez","Andrea Silva","Martin Lopez","Valeria Ramirez","Gabriel Castro","Natalia Gutierrez",
    "Daniel Bravo","Camila Torres","Diego Sanchez","Victoria Ortiz","Lucas Jimenez","Isabela Rios","Tomas Nunez","Renata Flores",
    "Nicolas Cruz","Emilia Alvarez","Sebastian Reyes","Antonella Mendoza","Mateo Guzman","Mariana Peralta","Agustin Romero","Catalina Leon",
    "Matias Herrera","Elena Aguilar","Facundo Medina","Julieta Rojas","Ignacio Castro","Luciana Soto","Ramiro Fernandez","Florencia Montoya",
    "Bruno Miranda","Abril Ortiz","Franco Torres","Emilia Navarro","Juan Pablo Benitez","Martina Salazar","Matias Ramos","Valentina Molina",
    "Santiago Castillo","Carolina Avila","Lucas Rivera","Daniela Herrera"]

    Condiciones = ["Dolor de cabeza", "Fiebre", "Tos", "Dolor abdominal", "Vomitos", "Diarrea", "Dolor de espalda","Dolor articular", "Lesion", "Infeccion"]

    Pacientes = []

    for _ in range(CantidadPacientes):
        Nombre = random.choice(Nombres)
        Edad = random.randint(1, 100)
        Condicion = random.choice(Condiciones)
        Prioridad = random.randint(1, 500)
        Paciente_Objeto = Paciente(Nombre, Edad, Condicion, Prioridad)
        Pacientes.append(Paciente_Objeto)

    return Pacientes
