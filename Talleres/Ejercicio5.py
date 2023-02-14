#Realizar un programa en el cual se declaren dos valores enteros por 
#teclado utilizando el método __init__. Calcular después la suma, resta, 
#multiplicación y división. Utilizar un método para cada una e imprimir los 
#resultados obtenidos. Llamar a la clase Calculadora.
class Calculadora:
    def __init__(self,num1,num2):
        self.num1=float(num1)
        self.num2=float(num2)
    def sumar(self):
        suma=self.num1+self.num2
        print(f"Suma: {suma}")
    def restar(self):
        resta=self.num1-self.num2
        print(f"Resta: {resta}")
    def multiplicar(self):
        multi=self.num1*self.num2
        print(f"Multiplicación: {multi}")
    def dividir(self):
        div=self.num1/self.num2
        print(f"División: {div}")
num1=input("Digite un número: ")
num2=input("Digite otro número: ")
calculadora1=Calculadora(num1,num2)
calculadora1.sumar()
calculadora1.restar()
calculadora1.multiplicar()
calculadora1.dividir()