#Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
#Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""
entrada=str(input("Digite una oracion o frase: "))#Entrada
def espacios(cadena): 
    contador = 0
    for i in range(0, len(cadena)):#Bucle desde 0 hasta la longitud de la cadena
        if cadena[i] == " ":
            contador += 1 #Contador de espacios
    return contador 
cadena = entrada
print("Numero de espacios: ",espacios(cadena))#Salida