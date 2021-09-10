import time, os
from .crobject import CRObject
from .dbobjects import DBObjects

db = DBObjects()

def print_options():
    print('Proyecto 1 \n')
    print('Selecciona una opción:')
    print('1. Crear objeto')
    print('2. Listar objetos')
    print('3. Modificar objeto')
    print('4. Eliminar objeto')
    print('5. Buscar objeto')
    print('6. Salir')

def run():
    print_options()

    print('Que desea hacer?')
    command = input('Escriba aqui el numero de la opcion: ')

    if command == '1':
        create_crobject()
    elif command == '2':
        list_crobject()
    elif command == '3':
        edit_crobject()
    elif command == '4':
        delete_crobject()
    elif command == '5':
        search_crobject()
    elif command == '6':
        os._exit(1)
    else:
        print('Comando inválido')
        time.sleep(1)
        run()

def create_crobject():
    print('\n Crear objeto')
    while True:
       key = input("Escribe un numero entero como key: ")
       try:
           key = int(key)
           return key
       except ValueError:
           print("La key es incorrecta: escribe un numero entero")
    
    while True:
       value = input("Escribe el valor que deseas almacenar: ")
       try:
           value = str(value)
           return value
       except ValueError:
           print("El valor es incorrecto escribelo de nuevo")

    crobject = CRObject(None, key, value)
    if db.save_contact(crobject):
        print('Objeto insertado con éxito')
    else:
        print('Error al guardar el objeto')

def list_crobject():


def edit_crobject():

def delete_crobject():

if __name__ == "__main__":
    run()
