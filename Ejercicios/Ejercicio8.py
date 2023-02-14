class aula:
    def __intil__(self):
        self.nombre=str(nombre)
        self.cantidad=int(cantidad)
    def contar(self):
        print(f"{nombre}:{cantidad}")

nombre=str(input("Ingrese el nombre del artículo: "))
cantidad=int(input("Ingrese la cantidad existente en el aula: "))

aula = aula()
aula.contar()