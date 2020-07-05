####################################################
#  @author: Miguel Mendoza
#  Menu.py:
#       Archivo principal con el menú de opciones.
#####################################################

from collections import OrderedDict
from Opcion1 import Op1 
from Opcion2 import Op2
from Opcion3 import Op3
from Opcion4 import Op4
from Opcion5 import Op5

def menu_1():
    """Recibir cantidad  """   
    print(menu_1.__doc__ + "\n\n")
    Op1()

def menu_2():
    """Transferir monto """    
    print(menu_2.__doc__ + "\n\n")
    Op2()

def menu_3():
    """Mostrar balance una moneda """    
    print(menu_3.__doc__ + "\n\n")
    Op3()

def menu_4():
    """Mostrar balance general  """
    print(menu_4.__doc__ + "\n\n")
    Op4()

def menu_5():
    """Mostrar histórico de transacciones """
    print(menu_5.__doc__ + "\n\n")
    Op5()

def menu_6():
    """Salir del programa """    

if __name__ == '__main__':
    salir = False
    mensaje = "Ingrese la opción deseada"    

    #Creo el menú como una lista ordenada de objetos
    menu = OrderedDict(
        [
            ('1', menu_1),
            ('2', menu_2),
            ('3', menu_3),
            ('4', menu_4),
            ('5', menu_5),
            ('6', menu_6)
        ]
    )

    while not salir:
        
        print('-' * len(mensaje))    
        print(mensaje)
        print('-' * len(mensaje))        

        for opcion, funcion in menu.items():
            #Creo la línea a imprimir aprovechando la descripción de cada función de menú
            mensaje_final='{}. {}'.format(opcion,funcion.__doc__)
            print(mensaje_final)

        respuesta = input('\nOpción: ').lower()
        salir= respuesta == '6'

        funcion = menu.get(respuesta, None)

        if funcion:
            funcion()
    else:
        print("Hasta la proxima")
        input("Presione una tecla para salir")
