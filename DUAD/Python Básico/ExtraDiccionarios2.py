employees = [
    {"name": "Carlos", "email": "Carlos@empresa.com", "departament": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "departament": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "departament": "Ventas"},
    {"name": "Sofia", "email": "sofia@emoresa.com", "departament": "RRHH"},                 
]

result = {}

for emp in employees:
    dept = emp["departament"]
    
# 1. Crear la lista si no existe
    if dept not in result:
        result[dept] = []
    
# 2. Agregar siempre el empleado
    result[dept].append(emp)

print(result)

