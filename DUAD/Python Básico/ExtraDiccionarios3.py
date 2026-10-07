products = [
    {"name": "Monitor", "category": "Electronica", "price": 200},
    {"name": "Teclado", "category": "Electronica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electronica", "price": 25},
]

result = {}

for product in products:
    category = product["category"]
    price = product["price"]

    if category in result:
        result[category] += price
    else:
        result[category] = price
print(result)