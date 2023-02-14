#Desarrollar una clase que represente un Cuadrado y tenga los siguientes
#métodos: inicializar el valor del lado llegando como parámetro al método
#__init__ (definir un atributo llamado lado), imprimir su perímetro y su
#superficie.
class Cuadrado:
    def __init__(self,side):
        self.side=int(side)
    def mostrar_perímetro(self):
        perímetro=self.side*4
        print(perímetro)
    def mostrar_superficie(self):
        superficie=self.side*self.side
        print(superficie)
side=input("Ingrese el valor de un lado del cuadrado: ")
cuadrado1=Cuadrado(side)
cuadrado1.mostrar_perímetro()
cuadrado1.mostrar_superficie()