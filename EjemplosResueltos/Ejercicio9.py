# INSTRUCCIONES:

#Crea una función que convierta una temperatura en grados Celsius a grados Fahrenheit. 
#La fórmula de conversión es: F = (C * 9/5) + 32 

def celsius_a_fahrenheit(grados_celsius):
    fahrenheit = (grados_celsius * 9/5) + 32
    return fahrenheit

# Ejemplo de uso
grados_celsius = 30
fahrenheit = celsius_a_fahrenheit(grados_celsius)
print(f"{grados_celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
