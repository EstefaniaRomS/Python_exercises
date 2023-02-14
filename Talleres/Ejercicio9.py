#Crear programa que contenga una clase denominada Número de ficha, 
#crear los objetos (aprendices ficha), crear atributos y métodos 
#relacionados a la clase y objeto creado (datos_básicos)
class Numero_ficha:
    def inicializar(self,name,celular,correo):
        self.nombre=name
        self.celular=celular
        self.correo=correo
    def imprimir(self):
        print(f"Nombre: {self.nombre}, Celular: {self.celular}, Correo: {self.correo}")
        print("-------------------------------------------------------------------------")

print("*************************************************************************")
print("                       Aprendices ficha 2450238")
print("*************************************************************************")

aprendiz1=Numero_ficha()
aprendiz1.inicializar('Estefanya','3054218550','estefania@gmail.com')
aprendiz1.imprimir()

aprendiz2=Numero_ficha()
aprendiz2.inicializar('Cristian','3054218550','Cristian@gmail.com')
aprendiz2.imprimir()

aprendiz3=Numero_ficha()
aprendiz3.inicializar('Anderson','3054218550','Anderson.com')
aprendiz3.imprimir()

aprendiz4=Numero_ficha()
aprendiz4.inicializar('Rafael','3054218550','Rafael.com')
aprendiz4.imprimir()