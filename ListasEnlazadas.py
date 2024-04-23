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

    def append(self, NodoActual, Paciente):
        if not self.head:
            self.head = NodoListaDePrioridad(Paciente)
            self.tail = self.head
            self.size += 1
            return
        
        if NodoActual.prev == None:
            if Paciente.prioridad > NodoActual.value.prioridad:
                head_viejo = self.head
                self.head = NodoListaDePrioridad(Paciente)
                self.head.next = head_viejo

                head_viejo.prev = self.head
                self.size += 1
                
                return
            
        if Paciente.prioridad < NodoActual.value.prioridad:
            if Paciente.prioridad < self.tail.value.prioridad:
                tail_viejo = self.tail
                self.tail = NodoListaDePrioridad(Paciente)
                self.tail.prev = tail_viejo

                tail_viejo.next = self.tail
                self.size += 1

                return
            
            NuevoNodo = NodoListaDePrioridad(Paciente)
            NodoActual_Next = NodoActual.next

            NodoActual.next = NuevoNodo
            NodoActual_Next.prev = NuevoNodo
            
            NuevoNodo.next = NodoActual_Next
            NuevoNodo.prev = NodoActual

            self.size += 1

            return
     
        self.append(NodoActual.prev, Paciente)

    # Funcion para imprimir toda la lista enlazada.
    def traverse(self, NodoActual, Nodo = 0):
        if not self.tail:
            return
        
        print(f"Valor Nodo {Nodo}:", NodoActual.value)
        #print("Prev Nodo:", NodoActual.prev)
        #print("Next Nodo:", NodoActual.next)

        if not NodoActual.prev:
            return
        
        self.traverse(NodoActual.prev, Nodo + 1)

    def delete_tail(self):
        if not self.tail:
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
        if not self.tail:
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
        if not self.tail:
            return
        
        if NombrePaciente == NodoActual.value.nombre:
            PacienteObjeto = NodoActual.value
            PacienteObjeto.prioridad = NuevaPrioridad

            print(f"Nodo actualizado: {NodoActual.value}")

            # Si es tail actualizarlo.
            if NodoActual.next == None:
                self.delete_tail()
                self.append(self.tail, PacienteObjeto)
                return

            # Si es head actualizarlo.
            if NodoActual.prev == None:
                self.delete_head()
                self.append(self.tail, PacienteObjeto)
                return

            Prev_NodoActual = NodoActual.prev
            Next_NodoActual = NodoActual.next

            Prev_NodoActual.next = Next_NodoActual
            Next_NodoActual.prev = Prev_NodoActual

            NodoActual.next = None
            NodoActual.prev = None

            self.append(self.tail, PacienteObjeto)
            return
            
        if not NodoActual.prev:
            return
    
        self.update_node(NodoActual.prev, NombrePaciente, NuevaPrioridad)