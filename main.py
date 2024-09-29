'''
Desafío 1: Sistema de Gestión de Productos
Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:

Crear una clase base Producto con atributos como producto, precio, cantidad en stock, etc.
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos
y métodos específicos.
Implementar operaciones CRUD para gestionar productos del inventario.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.'''

'''
Laboratorio 2:
Objetivo: Mediante la creación de repositorios en GitHub que implemente la solución propuesta en el laboratorio
anterior con persistencia en una base de datos SQL.

Descripción: En este laboratorio, deberás implementar la solución utilizando Python en el paradigma
de programación orientada a objetos. La persistencia de los datos deberá realizarse en una base de
datos SQL. Una vez completada la solución, deberás subir el código a un repositorio público en GitHub
y proporcionar el enlace correspondiente para su evaluación'''

import os
import platform
from datetime import datetime


from sgp import (
    ProductoAlimenticio,
    ProductoElectronico,
    GestionProductos,
)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo / windows es diferente a los demas'''
    if platform.system() == 'Windows': #windows 
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print("========== Menú de Gestión de Productos ==========")
    print("1: Agregar un producto electrónico")
    print("2: Agregar un producto alimenticio")
    print("3: Buscar producto por código")
    print('4. Actualizar stock del producto')
    print('5. Eliminar producto por código')
    print('6. Mostrar todos los productos')
    print('7. Salir')
    print('======================================================')

#Pra evitar cargar todos los datos, quier primero verificar el codigo del producto

#Para cargar productos
def agregar_producto(gestion, tipo_producto):
    try:
        codigo_producto = input('Ingrese código del producto: ')

        
        # si el código no existe sigue por aca
        nombre_producto = input('Ingrese el nombre del producto: ')
        precio = float(input(f'Ingrese el precio de {nombre_producto}: '))
        cantidad_stock = int(input(f'Ingrese el stock de {nombre_producto}: '))
        marca = input(f'Ingrese la marca del {nombre_producto}: ')

        if tipo_producto == '1':
            modelo = input(f'Ingrese el modelo del {nombre_producto}: ')
            producto = ProductoElectronico(codigo_producto, nombre_producto, precio, cantidad_stock, marca, modelo)
        elif tipo_producto == '2':
            peso = int(input(f'Ingrese el peso del {nombre_producto}: '))
            producto = ProductoAlimenticio(codigo_producto, nombre_producto, precio, cantidad_stock, marca, peso)
        else:
            print('Opción inválida')
            return
        
        gestion.crear_producto(producto)
        print('Producto agregado exitosamente.')
        input('Presione enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
        input('Presione enter para continuar...')
    except Exception as e:
        print(f'Error inesperado: {e}')
        input('Presione enter para continuar...')

def buscar_producto_por_codigo(gestion):
    codigo_producto = input('Ingrese el código del producto a buscar: ')
    
    # Puedo usar la funcion buscar y aca despliego los detalles
    producto = gestion.buscar_producto(codigo_producto)
    
    if producto:
        # ver  valores del producto y mostrarlos
        nombre_producto, cantidad_stock = producto
        print(f'Datos del producto encontrado:\n'
              f'Nombre del Producto: {nombre_producto}\n'
              f'Cantidad en Stock: {cantidad_stock}')
    else:
        print(f'No se encontró ningún producto con el código {codigo_producto}.')
    
    input('Presione enter para continuar...')

def actualizar_stock_producto(gestion):
    codigo_producto = input('Ingrese el código del producto a modificar stock: ')
    actualiza_cantidad_stock=int(input('Ingresa la cantidad de stock del producto'))
    gestion.actualizar_producto(codigo_producto,actualiza_cantidad_stock)
    input('Presione enter para continuar...')

def eliminar_producto_por_codigo(gestion):
    codigo_producto = input('Ingrese el código del producto a eliminar: ')
    gestion.eliminar_producto(codigo_producto)
    input('Presione enter para continuar...')

def mostrar_todos_los_productos(gestion):
    print('========================================================')    
    try:
        productos = gestion.leer_todos_los_productos()  # Supongamos que esto devuelve una lista de productos
        for producto in productos:
            if isinstance(producto, ProductoElectronico):  # Verifica si el producto es electrónico
                print(f'{producto.codigo_producto} - {producto.producto} (Electrónico)')
            elif isinstance(producto, ProductoAlimenticio):  # Verifica si el producto es alimenticio
                print(f'{producto.codigo_producto} - {producto.producto} (Alimenticio)')
            else:
                print(f'{producto.codigo_producto} - {producto.producto} (Otro tipo)')
    except Exception as e:
        print(f'Error al mostrar productos: {e}')
    print('========================================================')
    input('Presione enter para continuar...')


if __name__ == "__main__":

    gestion_productos=GestionProductos()
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción para continuar: ') 
        
        if opcion == '1' or opcion == '2':
            agregar_producto(gestion_productos,opcion)
        elif opcion == '3':
            buscar_producto_por_codigo(gestion_productos)
        elif opcion == '4':
            actualizar_stock_producto(gestion_productos)
        elif opcion == '5':
            eliminar_producto_por_codigo(gestion_productos)
        elif opcion == '6':
            mostrar_todos_los_productos(gestion_productos)
        elif opcion == '7':
            print('Saliendo del programa')
            input('Presione enter para continuar...')
            break
        else:
            print('Opción no válida, ingrese una opción del 1 al 7.')

# Revisar: Cuando agrego un producto, el nro de codigo me agrega sin ceros, y despues no lo puedo listar.