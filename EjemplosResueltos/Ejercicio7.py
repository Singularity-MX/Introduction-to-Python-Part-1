#INTSTRUCCIONES:

#Escribe una función que tome un número como argumento y determine si es par o impar. 
#Luego, utiliza un condicional if para imprimir un mensaje indicando si el número es par o impar.

def par_o_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

# Ejemplo de uso
numero = 15
par_o_impar(numero)
