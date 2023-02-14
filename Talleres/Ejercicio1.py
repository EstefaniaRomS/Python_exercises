#Confeccionar una clase que permita carga el nombre y la edad de una
#persona. Mostrar los datos cargados. Imprimir un mensaje si es mayor 
#de edad (edad>=18)
class Persona:
    def __init__(self,name,age):
        self.name=str(name)
        self.age=int(age)
    def mostrar(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
    def imprimir(self):
        if self.age>=18:
            print("Sí es mayor de edad.")
        else:
            print("No es mayor de edad.")
            
name=input("Ingrese su nombre: ")
age=input("Ingrese su edad: ")

persona1=Persona(name,age)
persona1.mostrar()
persona1.imprimir()