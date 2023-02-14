class calculadora:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)
    def sumar(self):
        suma = self.num1 + self.num2
        print("El resultado de la suma es: ", suma)
    def restar(self):
        resta = self.num1 - self.num2
        print("El resultado de la resta es: ", resta)
    def multiplicar(self):
        multi = self.num1 * self.num2
        print("El resultado de la multiplicación es: ", multi)
    def dividir(self):
        divi = self.num1 / self.num2
        print("El resultado de la división es: ", divi)

num1 = input("Ingrese un número: ")
num2 = input("Ingrese otro número: ")

calculadora = calculadora(num1,num2)
calculadora.sumar()
calculadora.restar()
calculadora.multiplicar()
calculadora.dividir()