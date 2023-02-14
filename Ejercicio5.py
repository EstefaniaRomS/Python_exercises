#Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar 
#la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para que 
#sea más fácil disponer la condición que verifica que es una vocal.
entry=str(input("Digite una oracion o frase: ")).lower()#Entrada
def vowel(string): 
    count = 0
    for i in range(0, len(string)): #Bucle desde 0 hasta la longitud de la cadena
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u": 
            count += 1#Contador de vocales
    return count
string = entry
print("Cantidad de vocales: ",vowel(string))