#Realizar un programa que conste de una clase llamada Aprendiz que 
#tenga como atributos el nombre y la nota del aprendiz. Definir los 
#métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje 
#con el resultado de la nota y si ha aprobado o no.
class Aprendiz:
    def __init__(self,name,grade):
        self.name=name
        self.grade=float(grade)
    def imprimir(self):
        print(f"Nombre: {self.name}")
    def mostrar(self):
        print(f"Calificación: {self.grade}")
        if self.grade>=3:
            print("Aprobado")
        elif self.grade>5:
            print("Calificación incorrecta")
        else:
            print("No aprobado")
name=input("Ingrese el nombre del aprendiz: ")
grade=input("Ingrese la nota del aprendiz: ")
aprendiz1=Aprendiz(name,grade)
aprendiz1.imprimir()
aprendiz1.mostrar()