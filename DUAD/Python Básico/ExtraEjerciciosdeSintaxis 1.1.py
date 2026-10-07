# Pedimos el precio al usuario 
precio = float(input("Ingrese el precio del producto: "))
# Verificamos la condicion 
if precio < 100:
    descuento = precio * 0.02
else:
    descuento = precio * 0.10
# Calculamo el precio final 
precio_final = precio - descuento 
# Mostramos el resultado 
print("El precio final es:", precio_final)
