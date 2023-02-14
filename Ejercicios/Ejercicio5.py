class banco:
    def inicializar(self,nombre,cedula,edad):
        self.nombre=nombre
        self.cedula=int(cedula)
        self.edad=int(edad)
        
    def registrar(self):
        self.nombre=input("Ingrese su nombre: ")
        self.cedula=int(input("Ingrese su cedula: "))
        self.edad=int(input("Ingrese su edad: "))
        
    def mostrar_registro(self):
        if self.edad>=18:
            print(f"Usted '{self.nombre}', con número de cédula '{self.cedula}':")
            print("Puede sacar una cuenta de banco, cuenta con la edad requerida.")
        else:
            print("No puede sacar una cuenta de banco, no cuenta con la edad requerida.")
banco=banco()
banco.registrar()
banco.mostrar_registro()


