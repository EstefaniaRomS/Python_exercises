#Desarrollar un programa que cargue los lados de un triángulo e
#implemente los siguientes métodos: inicializar los atributos, imprimir el
#valor del lado mayor y otro método que muestre si es equilátero o no. El
#nombre de la clase llamarla Triangulo.
class Triangulo:
    def __init__(self,side1,side2,side3):
        self.side1=int(side1)
        self.side2=int(side2)
        self.side3=int(side3)
    def imprimir(self):
        if self.side1>self.side2 and self.side1>self.side3:
            print(f"Lado mayor: {self.side1}")
        elif self.side2>self.side1 and self.side2>self.side3:
            print(f"Lado mayor: {self.side2}")
        elif self.side3>self.side1 and self.side3>self.side2:
            print(f"Lado mayor: {self.side3}")
    def mostrar(self):
        if self.side1==self.side2==self.side3:
            print("Es un triángulo equilátero.")
        else:
            ("No es un triángulo equilátero.")
side1=input("Ingrese el primer lado del triángulo: ")
side2=input("Ingrese el segundo lado del triángulo: ")
side3=input("Ingrese el tercer lado del triángulo: ")
triangulo1=Triangulo(side1,side2,side3)
triangulo1.imprimir()
triangulo1.mostrar()