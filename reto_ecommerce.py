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

#Mensaje de bienvenida
print(f"Bienvenido a {tienda_info[0]} en {tienda_info[1]} ({tienda_info[2]})")

#Mostrar cuántos productos existen
print(f"Total de productos: {len(productos)}")

#Precios finales con descuento
#Producto 1
prod1 = productos[0]
prod1_desc = prod1["precio"] - (prod1["precio"] * prod1["descuento"])
print(f"{prod1['nombre']} -> ${prod1_desc}")

#Producto 2
prod2 = productos[1]
prod2_desc = prod2["precio"] - (prod2["precio"] * prod2["descuento"])
print(f"{prod2['nombre']} -> ${prod2_desc}")

#Producto 3
prod3 = productos[2]
prod3_desc = prod3["precio"] - (prod3["precio"] * prod3["descuento"])
print(f"{prod3['nombre']} -> ${prod3_desc}")

#Producto 4
prod4 = productos[3]
prod4_desc = prod4["precio"] - (prod4["precio"] * prod4["descuento"])
print(f"{prod4['nombre']} -> ${prod4_desc}")

#Producto 5
prod5 = productos[4]
prod5_desc = prod5["precio"] - (prod5["precio"] * prod5["descuento"])
print(f"{prod5['nombre']} -> ${prod5_desc}")

#Total de cada venta
#Venta 101
venta_101_total = prod1_desc * 1
print(f"Venta 101: {ventas[0]['cliente']} compró {ventas[0]['cantidad']} {prod1['nombre']} y pagó {venta_101_total}")

#Venta 102
venta_102_total = prod2_desc * 2
print(f"Venta 102: {ventas[1]['cliente']} compró {ventas[1]['cantidad']} {prod2['nombre']} y pagó {venta_102_total}")

#Venta 103
venta_103_total = prod4_desc * 1
print(f"Venta 103: {ventas[2]['cliente']} compró {ventas[2]['cantidad']} {prod4['nombre']} y pagó {venta_103_total}")

#Venta 104
venta_104_total = prod2_desc * 1
print(f"Venta 104: {ventas[3]['cliente']} compró {ventas[3]['cantidad']} {prod2['nombre']} y pagó {venta_104_total}")

#Venta 105
venta_105_total = prod5_desc * 3
print(f"Venta 105: {ventas[4]['cliente']} compró {ventas[4]['cantidad']} {prod5['nombre']} y pagó {venta_105_total}")

#Ingreso total de la tienda
ingreso_total = venta_101_total + venta_102_total + venta_103_total + venta_104_total + venta_105_total
print(f"Ingreso total: {ingreso_total}")