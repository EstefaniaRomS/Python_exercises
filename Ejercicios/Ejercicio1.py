class listas:
    def mostrar_meses(self):
        self.months=['Enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
        print (self.months)

    def mostrar_dias(self):
        self.days=['Lunes','martes','miercoles','jueves','viernes','sabado',]
        print (self.days)
listas=listas()
i=0
while i==0:
    print("Mostrar: ")
    print("1. Nombre de los meses")
    print("2. Nombre de los dias")
    print("3. Salir")
    opcion=int(input(" "))
    if opcion==1:
        listas.mostrar_meses()
    elif opcion==2:
        listas.mostrar_dias()
    elif opcion==3:
        break
    else: 
        print("...")
        i=0