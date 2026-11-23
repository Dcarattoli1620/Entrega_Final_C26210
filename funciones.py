#################################################################################################
#       Funciones
#################################################################################################


import funciones_sql

# Inicialización del Colorama
from colorama import Back, Fore, Style, init
init(autoreset=True)

# Función para Mostrar Menú Principal
def mostrar_menu():
    
    print("\n --- Sistema de Gestión Básica de Productos ---")
    
    print("1 - Agregar producto")
    print("2 - Mostrar producto")
    print("3 - Buscar producto")
    print("4 - Actualizar Producto")
    print("5 - Elminar Producto")
    print("6 - Reporte de stock mínimo")
    print("7 - Salir")

# Función para Espaciar Mensajes
def espacio():
   
    print("")

# Función para Validar Texto no vacío
def valida_texto(mensaje):
    while True:
        texto = input(mensaje).lower().strip()
        if texto:
            return texto
        espacio()
        print(Fore.RED + "\n El campo no debe estar vacío")

# Función para Validar Números Enteros
def valida_entero(mensaje):

    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print(Fore.RED + "El valor ingresado no debe ser un número negativo")
                continue
            return valor
        except ValueError:
            print(Fore.RED + "Error: debe ingresar un número entero")

# Función para Agregar Producto
def agregar_productos():

# Agrega el Nombre de Producto a ingresar

    print("\n---- Ingresó a Agregar Producto ----")
        
    nombre = valida_texto("Ingrese nombre producto: ").lower().strip()
    
# Agrega la descripción del Producto a ingresar
    
    descripcion = input("Ingrese la descripción del producto: ").lower().strip()

# Agrega la Categoria del Producto a ingresar
    
    categoria = valida_texto("Ingrese categoría del producto: ").lower().strip()
        
# Agrega la cantidad del nuevo producto
    
    cantidad=valida_entero("Ingrese la cantidad del producto: ")
                 
# Agrega el Precio del Producto a ingresar
    
    precio=valida_entero("Ingrese el precio del producto: ")

# Agrega los campos a la BBDD

    funciones_sql.registrar_producto(nombre,descripcion,categoria,cantidad,precio)
    espacio()
    print(Fore.GREEN + f"El producto {nombre} ha sido agregado correctamente.")
    espacio()

# Función para Mostrar Producto    
def mostrar_producto(lista_producto):
    """
    Función para Mostrar Producto

    Parametros
        Lista de Productos en la variable --> lista
        
    Retorno:
        Muestra los Productos de la base de datos
    """
    espacio()
    
    if len(lista_producto) == 0:
            print(Fore.RED + "No hay productos registrados.")
    else:
        print(Fore.GREEN + "-- PRODUCTO/S --")
        espacio()
    
        for indice in range(len(lista_producto)):
                producto = lista_producto[indice]
        
                print(f"ID: {producto[0]}. Nombre: {producto[1]}")
                print(f"   Descripcion: {producto[2]}")
                print(f"   Categoria: {producto[3]}")
                print(f"   Cantidad: {producto[4]}")
                print(f"   Precio: {producto[5]}")
                print("\n")
      
# Función para Mostrar Todos los Productos
def mostrar_todos_los_productos():
    lista_productos= funciones_sql.obtener_todos_los_productos()
    mostrar_producto(lista_productos)

# Función para Buscar Producto por ID
def buscar_producto_por_id():
    #Busco Producto
    print("\n ---- Busco Producto ----") 
    try:
        id_producto = int(input("Ingrese el ID del producto: "))
        print(id_producto)
        producto = funciones_sql.obtener_producto_por_id(id_producto)

        if producto:
            print(" Producto Encontrado ")
            mostrar_producto([producto])
            return producto
        else:
            espacio()
            print(Fore.RED + " El producto no existe ")
            return None
        
    except ValueError:
        print(Fore.RED + " El id debe ser un número entero ")

# Función para Actualizar Producto por ID
def actualizar_producto_id():
    producto = buscar_producto_por_id()

    if producto:
        print(" Campos para actualizar ")
        espacio()
        print(" 1 - Nombre ")
        print(" 2 - Descripción ")
        print(" 3 - Categoría ")
        print(" 4 - Cantidad ")
        print(" 5 - Precio ")

        opcion = input(" Ingrese la opción deseada: ")

        match opcion:
            case "1":
                # actualizar nombre
                
                nombre = valida_texto("Ingrese nombre producto: ").lower().strip()
                
                funciones_sql.actualizar_nombre(producto[0],nombre)
                espacio()
                print(Fore.GREEN + f" El nombre del producto '{producto[1]}' ha sido actualizado ")
                
            case "2":
                # actualizar descripcion
                descripcion = input("Ingrese la descripción del producto: ").lower().strip()

                funciones_sql.actualizar_descripcion(producto[0],descripcion)  
                espacio()
                print(Fore.GREEN + f"La descripcion del producto '{producto[1]}' ha sido actualizada ")

            case "3":
                # actualizar categoria
                categoria = valida_texto("Ingrese la categoria del producto: ").lower().strip()

                funciones_sql.actualizar_categoria(producto[0],categoria)
                espacio()
                print(Fore.GREEN + f"La categoría del producto '{producto[1]}' ha sido actualizada")
                
            case "4":
                # actualizar cantidad
                cantidad=valida_entero("Ingrese la cantidad del producto: ")
                
                funciones_sql.actualizar_cantidad(producto[0],cantidad)
                espacio()
                print(Fore.GREEN + f"La cantidad del producto '{producto[1]}' ha sido actualizada")

            case "5":
            # actualizar precio
                precio = valida_entero("Ingrese el precio del producto: ")
                  
                funciones_sql.actualizar_precio(producto[0],precio)
                espacio()
                print(Fore.GREEN + f" El precio del producto '{producto[1]}' ha sido actualizado ")    
            
            case _:
                espacio()
                print(Fore.RED + " La opcion ingresada no es valida ")

# Función para Eliminar Producto
def eliminar_producto():

   try:
        id_producto = int(input("Ingrese el id del producto que desea eliminar: ")) 
        
        if id_producto <= 0:
            print(Fore.RED + "Error: el ID debe ser numero entero positivo") 
            return None                                                  # finaliza la función y vuelve al menú ppal
        
        producto = funciones_sql.obtener_producto_por_id(id_producto)
        
        if not producto:
            espacio()
            print(Fore.RED + "El producto no existe")
            espacio()
            return None                                                 # finaliza la función y vuelve al menú ppal
        
        confirmacion = input(f"Confirma eliminar {producto[1]} (s/n): ").lower().strip()
        
        if confirmacion != "s":                                         # Si confirmación distinta de "S" vuelve al menú ppal
            espacio()
            print(Fore.RED + "Eliminacion cancelada")
            espacio()
            return None
        
        if funciones_sql.eliminar_producto_por_id(id_producto):
            espacio()
            print(Fore.GREEN + f"El producto {producto[1]} ha sido eliminado")
            espacio()
        else:
            espacio()
            print(Fore.RED + "No se pudo eliminar el producto")
            espacio()
   except Exception as ValueError:
       espacio()
       print(Fore.RED + "Error: el ID debe ser un numero entero")
       espacio()

# Función para Generar Reporte de stock mínimo de productos
def reporte_stock_minimo():
   
# Validacion de la variable limite
    espacio()
    limite = valida_entero("Ingrese el límite de cantidad: ")
    espacio()
                
    productos = funciones_sql.obtener_productos_bajo_stock(limite)
    
    if not productos:                                               #Si no hay productos con el cantidad = o inferior a limite
        print(f"No hay productos con cantidad igual o inferior a {limite}")
    else:
        espacio()
        print(Fore.GREEN + f"REPORTE DE STOCK (CANTIDAD <= {limite})")
        espacio()
        mostrar_producto(productos)

# Función para Salir del Sistema
def salida():
    
    espacio()
    print(Fore.GREEN + "\n ---- Saliendo del programa ----") 
    espacio()