sales = [
    {
        'date':'27/03/23',
        'customer_email':'Joe@gmail.com',
        'items': [
            {'name':'lava_lamp', 'upc': 'ITEM-453', 'unit_price': 65.76},
            {'name':'Iron', 'upc': 'ITEM-324', 'unit_price': 32.45},
            {'name':'Basketball', 'upc': 'ITEM-432', 'unit_price': 12.54},
        ],
    },
    {
        'date':'27/02/23',
        'customer':'David@gmail.com',
        'items': [
            {'name': 'Lava Lamp', 'upc':'ITEM-453', 'unit_price': 65.76},
            {'name':'Key holder', 'upc':'ITEM-23', 'unit_price': 5.42},
        ],
    },
    {
        'date': '26/02/23',
        'customer_email':'amanda@gmail.com',
        'items': [
            {'name':'Key Holder', 'upc':'ITEM-23', 'unit_price': 3.42},
            {'name':'Basketball','upc':'ITEM-432', 'unit_price': 17.54,}
        ],
    },
]
result = {}
for sale in sales:
    for item in sale['items']:
        upc = item['upc']   
        price = item['unit_price']

        if upc in result:
            result[upc] += price
        else:
            result[upc] = price
print(result)