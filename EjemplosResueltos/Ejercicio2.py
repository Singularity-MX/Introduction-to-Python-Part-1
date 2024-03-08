# INSTRUCCIONES:
# Si tienes 3 cajas que contienen 25 chocolates cada una, y 10 bolsas que contienen 32 caramelos cada una, 
# ¿cuántos dulces y chocolates tienes en total? 

# Definir la cantidad de chocolates por caja y el número de cajas
chocolates_por_caja = 25
cajas_chocolates = 3

# Definir la cantidad de caramelos por bolsa y el número de bolsas
caramelos_por_bolsa = 32
bolsas_caramelos = 10

# Calcular el total de chocolates y caramelos
total_chocolates = chocolates_por_caja * cajas_chocolates
total_caramelos = caramelos_por_bolsa * bolsas_caramelos

# Calcular el total de dulces
total_dulces = total_chocolates + total_caramelos

# Imprimir el resultado
print("El total de chocolates es:", total_chocolates)
print("El total de caramelos es:", total_caramelos)
print("El total de dulces es:", total_dulces)
