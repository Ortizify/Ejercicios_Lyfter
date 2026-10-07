list_a = ['first_name', 'last name', 'role']
list_b = ['Alex', 'Castillo', 'software Engineer']
#Crear el diccionario 
resultado = {}
for i in range (len(list_a)):
    resultado[list_a[i]] = list_b[i]                                              
print(resultado)                                                     