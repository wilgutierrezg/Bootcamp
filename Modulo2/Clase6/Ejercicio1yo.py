# 1. Crear lista de diccionarios con productos
productos = [
    {"nombre": "Manzanas", "stock": 3, "precio": 0.5},
    {"nombre": "Naranjas", "stock": 10, "precio": 0.7},
    {"nombre": "Leche", "stock": 2, "precio": 1.2},
    {"nombre": "Pan", "stock": 6, "precio": 1.0},
    {"nombre": "Huevos", "stock": 4, "precio": 0.2}
]

# 2. Recorrer productos e imprimir los que tienen stock < 5
print("Productos con stock menor a 5:")
for producto in productos:
    if producto["stock"] < 5:
        print(f"{producto['nombre']} - Stock: {producto['stock']} - Precio: {producto['precio']}")

# 3. List comprehension para crear lista de productos a reponer
reposicion = [producto["nombre"] for producto in productos if producto["stock"] < 5]

# 4. Imprimir total de productos en bajo stock y su valor total
total_bajo_stock = len(reposicion)
valor_total = sum(producto["stock"] * producto["precio"] for producto in productos if producto["stock"] < 5)

print(f"\nTotal de productos en bajo stock: {total_bajo_stock}")
print(f"Valor total de los productos en bajo stock: ${valor_total:.2f}")

# 5. While para ingresar productos al sistema
print("\nIngreso de productos (escribe 'salir' para terminar):")
while True:
    nombre = input("Nombre del producto: ")
    if nombre.lower() == "salir":
        break
    try:
        stock = int(input("Stock: "))
        precio = float(input("Precio: "))
        productos.append({"nombre": nombre, "stock": stock, "precio": precio})
        print(f"Producto {nombre} agregado.\n")
    except ValueError:
        print("Error: ingresa un número válido para stock y precio.\n")

# Mostrar lista final de productos
print("\nLista final de productos:")
for p in productos:
    print(p)