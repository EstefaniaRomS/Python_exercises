class notas:
    def __intil__(self,titulo,contenido):
        self.titulo=titulo
        self.contenido=contenido
    def ingresar(self):
        titulo=str(input("Ingrese el título: "))
        contenido=str(input("Ingrese el contenido: "))
        print("¿Desea ver la nota?")
        cond=str(input("Si/no: "))
        if cond=="si":
            print("***********************")
            print("Titulo: ",titulo)
            print("***********************")
            print("Contenido: ")
            print("***********************")
            print(contenido)
        else:
            breakpoint
nota=notas()
nota=nota.ingresar()