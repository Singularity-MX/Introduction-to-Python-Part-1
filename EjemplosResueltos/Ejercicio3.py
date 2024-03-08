# INSTRUCCIONES:

#Crea variables para almacenar tu nombre y tus apellidos. 
#Después crea una cadena con un texto que quieras e incluye marcadores para a˜nadir tu nombre y apellidos. 
#Imprime el resultado para verlo en la consola de Python. 

# Crear variables para almacenar nombre y apellidos
nombre = "Luis"
apellido_paterno = "González"
apellido_materno = "Pérez"

# Crear una cadena con marcadores para añadir nombre y apellidos
texto_personalizado = "¡Hola, mi nombre completo es {} {} {}!".format(nombre, apellido_paterno, apellido_materno)

# Imprimir el resultado
print(texto_personalizado)
