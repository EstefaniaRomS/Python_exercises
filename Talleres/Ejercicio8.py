#Elaborar un programa que conste de una clase llamada FDSIM, crear los
#objetos (formaciones de fdsim), crear atributos y métodos relacionados 
#con el ambiente de formación
class FDSIM:
    def inicializar(self,name,ficha,salon,instructor,jornada):
        self.nombre=name
        self.ficha=ficha
        self.salon=salon
        self.instructor=instructor
        self.jornada=jornada
    def mostrar(self):
        print("***********************************")
        print(self.nombre)
        print("-----------------------------------")
        print(f"Ficha: {self.ficha}")
        print(f"Ambiente: {self.salon}")
        print(f"Instructor(a): {self.instructor}")
        print(f"Jornada: {self.jornada}")
        
print("***********************************")
print("           Formaciones")
formacion1=FDSIM()
formacion1.inicializar('ADSO','000001','4103','James Morales','mañana')
formacion1.mostrar()

formacion2=FDSIM()
formacion2.inicializar('Telecomunicaciones','000002','4102','Andrea Gonza','mañana')
formacion2.mostrar()

formacion3=FDSIM()
formacion3.inicializar('ADSI','000003','4111','Jorge Yesid Vasquez','mañana')
formacion3.mostrar()

formacion4=FDSIM()
formacion4.inicializar('ADSI','000003','4111','Mauricio Mahecha','tarde')
formacion4.mostrar()