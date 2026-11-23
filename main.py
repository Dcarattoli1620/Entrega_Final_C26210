################################################################################################
#                                  Programa Principal - Código Principal
#
# Autor: Diego Carattoli
# Curso:Iniciación a la Programación con Python
# Comisión: C26210
# Entrega Final
#################################################################################################

import funciones
from conexion import crear_tabla

# Inicialización del Colorama
from colorama import Back, Fore, Style, init
init(autoreset=True)

while True:
    funciones.mostrar_menu()                                    # Función de opciones de menú

    opcion = input("Ingrese la opción deseada: ").strip()

    ## Valida que la opcion elegida sea un número del 1 al 5

    if opcion.isdigit():
    ### Acorde a la opcion elegida ejecuta lo solicitado
         match opcion:
             
            case "1":
                # Agrego Producto
                funciones.agregar_productos()    # LLamada a la función de Agregar Producto
                
            case "2":
                # Muestro Producto
                funciones.mostrar_todos_los_productos()     # LLamada a la función de Mostrar Producto
   
            case "3":
                # Busco Producto por ID
                funciones.buscar_producto_por_id()                  # Llamada a la función de Buscar Producto x ID
                
            case "4":
                # Actualizar Producto                   # Llamada a la función de Actualizar Producto
                funciones.actualizar_producto_id()

            case "5":
                # Elimino Producto                      # Llamada a la función de Eliminar Producto
                funciones.eliminar_producto()

            case "6":
                # Reporte de stock mínimo
                funciones.reporte_stock_minimo()        # Llamada a la función de Reporte de Stock Mínimo
                
            case "7":
                # Salida del sistema
                funciones.salida()                      # Llamada a la función de Salida del Sistema
                break
             
            case _:     
                # ES PARA TODOS LOS OTRAS OPCIONES NO CONTEMPLADAS
                funciones.espacio()
                print(Fore.RED + "\n ---- Opción no válida, intente nuevamente ----")
                continue

    else:
      funciones.espacio()
      print(Fore.RED + "\n ---- El dato ingresado es inválido ----")
