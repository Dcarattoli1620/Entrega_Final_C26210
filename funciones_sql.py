#################################################################################################
#       Funciones SQL
#################################################################################################

# Conexión a la BBDD
from conexion import conectar

# Inicialización del Colorama
from colorama import Back, Fore, Style, init
init(autoreset=True)


# Función para Registrar Producto
def registrar_producto(nombre,descripcion,categoria,cantidad,precio):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO productos (nombre,descripcion,categoria,cantidad,precio)
            VALUES (?,?,?,?,?)       
        """,(nombre,descripcion,categoria,cantidad,precio))

        conexion.commit()

    except Exception as error:
        print(Fore.RED + f"Error al registrar el producto: {error}")
    finally:
        conexion.close()

# Función para Obteneer producto por ID
def obtener_producto_por_id(id_producto):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM productos WHERE id = ?",(id_producto,))      #Al ser una tupla se coloca "," al final
        
        return cursor.fetchone()                                           # Captura un solo dato o el primero que encuentra
    except Exception as error:
        print(Fore.RED + f" Error al buscar el producto: {error}")                    # Guarda el error e indica cual es
        return None
    finally:
        conexion.close()

# Función para obteneer todos los productos
def obtener_todos_los_productos():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM productos")      
        return cursor.fetchall()                                           # Captura un todos los datos que encuentra
    except Exception as error:
        print(Fore.RED + f" Error al mostrar los productos: {error}")                    # Guarda el error e indica cual es
        return None
    finally:
        conexion.close()

# Función para Actualizar Nombre del Producto
def actualizar_nombre(id_producto,nombre_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos 
            SET nombre = ? 
            WHERE id = ?
        """,(nombre_nuevo,id_producto))

        conexion.commit()
    except Exception as error:
        print(Fore.RED + f" Error al actualizar el producto: {error}") # Guarda el error e indica cual es
    finally:
        conexion.close()    

# Función para Actualizar Descripción del Producto
def actualizar_descripcion(id_producto,descripcion_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE productos 
            SET descripcion = ? 
            WHERE id = ?
        """,(descripcion_nuevo,id_producto))

        conexion.commit()
    except Exception as error:
        print(Fore.RED + f" Error al actualizar el producto: {error} ") # Guarda el error e indica cual es
    finally:
        conexion.close()  

# Función para Actualizar Categoría del Producto
def actualizar_categoria(id_producto,categoria_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos 
            SET categoria = ? 
            WHERE id = ?
        """,(categoria_nuevo,id_producto))

        conexion.commit()
    except Exception as error:
        print(Fore.RED + f" Error al actualizar el producto: {error}") # Guarda el error e indica cual es
    finally:
        conexion.close()  

# Función para Actualizar Cantidad del Producto
def actualizar_cantidad(id_producto,cantidad_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos 
            SET cantidad = ? 
            WHERE id = ?
        """,(cantidad_nuevo,id_producto))

        conexion.commit()
    except Exception as error:
        print(Fore.RED + f" Error al actualizar el producto: {error}") # Guarda el error e indica cual es
        return None
    finally:
        conexion.close()  

# Función para Actualizar Precio del Producto
def actualizar_precio(id_producto,precio_nuevo):
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos 
            SET precio = ? 
            WHERE id = ?
        """,(precio_nuevo,id_producto))

        conexion.commit()
    except Exception as error:
        print(Fore.RED + f" Error al actualizar el producto {error} ") # Guarda el error e indica cual es   
    finally:
        conexion.close()  

# Función para Eliminar Producto por ID
def eliminar_producto_por_id(id_producto):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM productos WHERE id = ?",(id_producto,))
        conexion.commit()
        return cursor.rowcount > 0                  # Si se encontró y eliminó el elemento, cursor es mayor a 0 retorna True
    except Exception as error:
        print(Fore.RED + f"Error al eliminar el producto: {error}")
        return False
    finally:
        conexion.close() 

# Función para Obtener productos con Stock mínimo          
def obtener_productos_bajo_stock(limite):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        # Ordena por cantidad y en forma ascendente. Como 2° criterio por Nombre
        cursor.execute("""
            SELECT * FROM productos
            WHERE cantidad <= ?
            ORDER BY cantidad ASC, nombre ASC         
        """,(limite,))
        return cursor.fetchall()
    except Exception as error:
        print(Fore.RED + f"Error al generar el reporte de stock: {error}")
        return []                                 # Retorna la lista de lo encontrado o la lista vacía
    finally:
        conexion.close()