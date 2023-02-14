#Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con 
#valor iguales o superiores a 7.
string=[]
for i in range (1,6):#Bucle para la asignacion de 5 enteros
    x=int(input("Digite un numero entero: "))#Entrada
    if x >= 7:
        string.append(x)#Ingreso de valores mayores o iguales a 7 en la cadena
    else:
        FileNotFoundError
print(f"Los elementos con valores superiores a 6 son: {string}")