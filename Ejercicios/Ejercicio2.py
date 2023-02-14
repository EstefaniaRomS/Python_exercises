class persona:
    def __init__(self,name,lastname,age):
        self.name = name
        self.lastname = lastname
        self.age = age
    def concatenar(self):
        fullname = self.name+(" ")+self.lastname
        print("Su nombre completo es",fullname)
    def calcular(self):
        edad = self.age
        if edad<100 and edad>5:
            print("y usted tiene",edad,"años")
        elif edad>=100:
            print("Usted es demasiado joven")
        elif edad<=5:
            print("Usted es tal vez muy anciano(a)")

name = str(input("Ingrese su nombre: "))
lastname = str(input("Ingrese su apellido: ")) 
age = int(input("Digite su edad: "))

Persona = persona(name,lastname,age)
Persona.concatenar()
Persona.calcular()