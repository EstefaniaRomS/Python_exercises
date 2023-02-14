#Diseñar una clase para describir un artículo con los siguientes atributos:
# Código
# Cantidad.
# Precio
class Articulo:
    def __init__(self,code,quantity,price,name):
        self.name=str(name)
        self.code=int(code)
        self.quantity=int(quantity)
        self.price=int(price)
    def describir(self):
        print("***********************************")
        print(f"Artículo: {self.name}")
        print("***********************************")
        print(f"Código: {self.code}")
        print(f"Cantidad: {self.name}")
        print(f"Precio: {self.name}")
        print("***********************************")
name=input("Ingrese el nombre del artículo: ")
code=input("Digite el código: ")
quantity=input("Digite la cantidad disponible: ")
price=input("Digite el precio unitario: ")
articulo1=Articulo(code,quantity,price,name)
articulo1.describir()