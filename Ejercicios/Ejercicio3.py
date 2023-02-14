class numeros:
    def __init__(self,num1,num2):
        self.num1=int(num1)
        self.num2=int(num2)
    def comparar(self):
        if self.num1>self.num2:
            real=self.num1
            print(self.num1,"es el número mayor")
        elif self.num1<self.num2:
            real=self.num1
            print(self.num2,"es el número mayor")
        elif self.num1==self.num2:
            print("Ambos son iguales")
            
num1=int(input("Digite un número: "))
num2=int(input("Digite otro número: "))

numeros=numeros(num1,num2)
numeros.comparar()