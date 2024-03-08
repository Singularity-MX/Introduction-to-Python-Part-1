#INTSTRUCCIONES:

#Define una función que calcule el volumen de un cubo.
#Volumen = L x L x L

def volumen_cubo(lado):
    volumen = lado ** 3
    return volumen

# Ejemplo de uso
lado = 4
volumen = volumen_cubo(lado)
print(f"El volumen del cubo con lado {lado} es: {volumen}")
