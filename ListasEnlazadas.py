from Paciente import *

class NodoListaDePrioridad:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
    def __repr__(self) -> str:
        return str(self.value)

class ListaDePrioridad:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = -1

    def verify_group_priority(self, NodoActual, Prioridad, CntPacientesIgualPrioridad = 0):
        if not self.tail:
            return
        
        if CntPacientesIgualPrioridad > 2:
            self.update_group_names_to_update(self.tail, Prioridad)
            return
        
        if NodoActual.value.prioridad == Prioridad:
            self.verify_group_priority(NodoActual.prev, Prioridad, CntPacientesIgualPrioridad + 1)

        if not NodoActual.prev:
            return
        
        self.verify_group_priority(NodoActual.prev, Prioridad, CntPacientesIgualPrioridad)

    def update_group_names_to_update(self, NodoActual, Prioridad):

        if NodoActual.value.prioridad == Prioridad:
            NodoActual.value.prioridad += 1

        if not NodoActual.prev:
            return
        
        self.update_group_names_to_update(NodoActual.prev, Prioridad)

    def append(self, NodoActual, Paciente):
        if not self.head:
            self.head = NodoListaDePrioridad(Paciente)
            self.tail = self.head
            self.size += 1
            return
        
        if Paciente.prioridad < self.head.value.prioridad:
            HeadViejo = self.head
            NuevoHead = NodoListaDePrioridad(Paciente)

            HeadViejo.prev = NuevoHead
            NuevoHead.next = HeadViejo

            self.head = NuevoHead
            self.size += 1

            return
        

        if not NodoActual.next:
            if (Paciente.prioridad >= self.tail.value.prioridad):
                TailViejo = self.tail
                NuevoTail = NodoListaDePrioridad(Paciente)

                NuevoTail.prev = TailViejo
                TailViejo.next = NuevoTail

                self.tail = NuevoTail
                self.size += 1

                return
            return
        
        if (Paciente.prioridad >= NodoActual.value.prioridad) and (Paciente.prioridad < NodoActual.next.value.prioridad):
            NuevoNodo = NodoListaDePrioridad(Paciente)
            NodoActualNext = NodoActual.next

            NuevoNodo.prev = NodoActual
            NuevoNodo.next = NodoActualNext

            NodoActual.next = NuevoNodo
            NodoActualNext.prev = NuevoNodo

            self.size += 1

            return
        
     
        self.append(NodoActual.next, Paciente)

    # Funcion para imprimir toda la lista enlazada.
    def traverse(self, NodoActual, Nodo = 0):
        if not self.head:
            return
        
        print(f"Valor Nodo {Nodo}:", NodoActual.value)
        #print("Prev Nodo:", NodoActual.prev)
        #print("Next Nodo:", NodoActual.next)

        if not NodoActual.next:
            return
        
        self.traverse(NodoActual.next, Nodo + 1)

    def delete_tail(self):
        if not self.head:
            return "No existen pacientes"
        
        if self.tail == self.head:
            Tail = self.tail.value

            self.tail = None
            self.head = None

            self.size -= 1

            return Tail
        else:
            Tail = self.tail.value
            Prev_tail = self.tail.prev
            self.tail.prev = None

            Prev_tail.next = None
            self.tail = Prev_tail

            self.size -= 1
            
            return Tail
        
    def delete_head(self):
        if not self.head:
            return "No existen pacientes"
        
        if self.tail == self.head:
            Head = self.head.value

            self.tail = None
            self.head = None

            self.size -= 1

            return Head
        else:
            Head = self.head.value
            Next_head = self.head.next
            self.head.next = None

            Next_head.prev = None
            self.head = Next_head

            self.size -= 1
            
            return Head

    def update_node(self, NodoActual, NombrePaciente, NuevaPrioridad):
        if not self.head:
            return
        
        if NombrePaciente == NodoActual.value.nombre:
            PacienteObjeto = NodoActual.value
            PacienteObjeto.prioridad = NuevaPrioridad

            print(f"Nodo actualizado: {NodoActual.value}")

            # Si es tail actualizarlo.
            if NodoActual.next == None:
                self.delete_tail()
                self.append(self.head, PacienteObjeto)
                return

            # Si es head actualizarlo.
            if NodoActual.prev == None:
                self.delete_head()
                self.append(self.head, PacienteObjeto)
                return

            Prev_NodoActual = NodoActual.prev
            Next_NodoActual = NodoActual.next

            Prev_NodoActual.next = Next_NodoActual
            Next_NodoActual.prev = Prev_NodoActual

            NodoActual.next = None
            NodoActual.prev = None

            self.size -= 1
            
            self.append(self.head, PacienteObjeto)

            return
            
        if not NodoActual.next:
            return
    
        self.update_node(NodoActual.next, NombrePaciente, NuevaPrioridad)


Dll = ListaDePrioridad()

Paciente1 = Paciente("Juan", 16, "Fiebre", 2)
Paciente2 = Paciente("Camila", 20, "Dolor de cabeza", 1)
Paciente3 = Paciente("Mauricio", 32, "Diarrea", 4)
Paciente4 = Paciente("Laura", 22, "Diarrea", 2)
Paciente5 = Paciente("Leon", 14, "Diarrea", 1)

Dll.append(Dll.head, Paciente1)
Dll.append(Dll.head, Paciente2)
#Dll.append(Dll.head, Paciente3)
#Dll.append(Dll.head, Paciente4)
#Dll.append(Dll.head, Paciente5)

Dll.traverse(Dll.head)