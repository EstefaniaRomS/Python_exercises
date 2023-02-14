# Realizar un programa que conste de una clase llamada Automóvil que 
# tenga como atributos el color, modelo, numero de llantas, número de 
# puertas, km/h, crear e instanciar dos objetos, Definir los métodos para 
# inicializar sus atributos (encender, apagar, acelerar, frenar, imprimirlos y 
# mostrar un mensaje con el resultado del encendido, aceleración, frenado 
# y apagar objetos creados.
class Automovil:
    def inicializar (self):
        self.part=Automovil()
        self.part.color=(str(input("Elija el color de su automovil: ")))
        self.part.modelo=(str(input("Elija el modelo de su automovil: ")))
        self.part.llantas=(str(input("Elija el numero de llantas su automovil: ")))
        self.part.puertas=(str(input("Elija el numero de puertas de su automovil: ")))
    def proceso (self):
        self.pro=Automovil()
        self.pro.Km=(int(input("Digite el km de su auto para calibrarlo:")))
        print("...")
        if self.pro.Km<=0:
            print("Esta apagado")
        elif  self.pro.Km>=20 and self.pro.Km<=29:
            print("Modo de frenado")
        elif self.pro.Km>=30:
            print("Modo aceleracion")
        elif self.pro.Km>=1:
            print("Esta encendido")
        
part=Automovil()
part.inicializar()
part.proceso()