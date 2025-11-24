productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "categoria": "Computo", "precio": 25000, "descuento": 0.10, "stock": 5},
    {"id": 2, "nombre": "Mouse Gamer X", "categoria": "Accesorios", "precio": 1200, "descuento": 0.15, "stock": 20},
    {"id": 3, "nombre": "Teclado Mecánico K1", "categoria": "Accesorios", "precio": 2200, "descuento": 0.05, "stock": 10},
    {"id": 4, "nombre": "Monitor 27'' 4K", "categoria": "Computo", "precio": 8000, "descuento": 0.20, "stock": 7},
    {"id": 5, "nombre": "Audífonos Bluetooth Z", "categoria": "Audio", "precio": 1500, "descuento": 0.0, "stock": 15},
]

ventas = [
    {"venta_id": 101, "producto_id": 1, "cantidad": 1, "cliente": "Ana"},
    {"venta_id": 102, "producto_id": 2, "cantidad": 2, "cliente": "Luis"},
    {"venta_id": 103, "producto_id": 4, "cantidad": 1, "cliente": "Sofía"},
    {"venta_id": 104, "producto_id": 2, "cantidad": 1, "cliente": "Carlos"},
    {"venta_id": 105, "producto_id": 5, "cantidad": 3, "cliente": "Ana"},
]

tienda_info = ("TechieStore", "Santiago", 2025)

#! Retos:
print("==========================================================================")

#✅ 1. Mensaje de bienvenida
print(f"¡Bienvenido a {tienda_info[0]} en {tienda_info[1]}!")

#✅ 2. Mostrar cuántos productos existen
print(f"Actualmente tenemos {len(productos)} productos disponibles.")


#✅ 3. Precio final con descuento (sin loops)

'''
Para cada producto (a mano, uno por uno), calcula:
    precio_final = precio - (precio * descuento)
Y muestra:
    Laptop Pro 14 → $22500.0
    Mouse Gamer X → $1020.0
    
'''
print("==========================================================================")
print("Valores de productos con sus descuentos aplicados")


#Como en el ejercicio más adelante usaremos de nuevo el valor con descuento , para este caso preferí agregarlo al diccionario

productos[0]["precio_final"] = productos[0]['precio'] - (productos[0]['precio'] * productos[0]['descuento'])
productos[1]["precio_final"] = productos[1]['precio'] - (productos[1]['precio'] * productos[1]['descuento'])
productos[2]["precio_final"] = productos[2]['precio'] - (productos[2]['precio'] * productos[2]['descuento'])
productos[3]["precio_final"] = productos[3]['precio'] - (productos[3]['precio'] * productos[3]['descuento'])
productos[4]["precio_final"] = productos[4]['precio'] - (productos[4]['precio'] * productos[4]['descuento'])


print(f"{productos[0]['nombre']} -> {productos[0]['precio_final']}")
print(f"{productos[1]['nombre']} -> {productos[1]['precio_final']}")
print(f"{productos[2]['nombre']} -> {productos[2]['precio_final']}")
print(f"{productos[3]['nombre']} -> {productos[3]['precio_final']}")
print(f"{productos[4]['nombre']} -> {productos[4]['precio_final']}")



#✅ 4. Total de cada venta (sin loo)

'''Para cada venta:

1.  Identifica el producto correspondiente\
2.  Usa el precio final calculado\
3.  Multiplica por la cantidad

Ejemplo para la venta 101:

    Venta 101: Ana compró 1 Laptop Pro 14 y pagó 22500.0'''

print("==========================================================================")

print(f" Venta {ventas[0]["venta_id"]} : {ventas[0]["cliente"]} compró {ventas[0]["cantidad"]} {productos[0]["nombre"]} y pagó {ventas[0]["cantidad"] * productos[0]["precio_final"]} ")
print(f" Venta {ventas[1]["venta_id"]} : {ventas[1]["cliente"]} compró {ventas[1]["cantidad"]} {productos[1]["nombre"]} y pagó {ventas[1]["cantidad"] * productos[1]["precio_final"]} ")
print(f" Venta {ventas[2]["venta_id"]} : {ventas[2]["cliente"]} compró {ventas[2]["cantidad"]} {productos[3]["nombre"]} y pagó {ventas[2]["cantidad"] * productos[3]["precio_final"]} ")
print(f" Venta {ventas[3]["venta_id"]} : {ventas[3]["cliente"]} compró {ventas[3]["cantidad"]} {productos[1]["nombre"]} y pagó {ventas[3]["cantidad"] * productos[1]["precio_final"]} ")
print(f" Venta {ventas[4]["venta_id"]} : {ventas[4]["cliente"]} compró {ventas[4]["cantidad"]} {productos[4]["nombre"]} y pagó {ventas[4]["cantidad"] * productos[4]["precio_final"]} ")



## ✅ 5. Ingreso total de la tienda

'''Suma manualmente:
    ingreso_total = total_venta_101 + total_venta_102 + ...
Luego imprime:
    Ingreso total: XXXXX'''


print("==========================================================================")

ingreso_total = {
 (ventas[0]["cantidad"] * productos[0]["precio_final"]) +
 (ventas[1]["cantidad"] * productos[1]["precio_final"]) +
 (ventas[2]["cantidad"] * productos[3]["precio_final"]) +
 (ventas[3]["cantidad"] * productos[1]["precio_final"]) +
 (ventas[4]["cantidad"] * productos[4]["precio_final"]) 
}

print(f"El ingreso total de {tienda_info[0]} fue de {ingreso_total} ")




