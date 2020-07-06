from Funciones import es_moneda, get_precio, actualizar_dato, es_numero
from Funciones import es_mi_codigo, obtener_cantidad_Cripto, insertar_transaccion

def Op5():
    nombre_archivo = "Transacciones.txt"    

    mensaje = "Resumen de transacciones efectuadas a la fecha:"    
        
    print('-' * len(mensaje))
    print(mensaje)
    print('-' * len(mensaje))

    archivo = open(nombre_archivo,"r")    
    texto = archivo.read()

    print ("\n" + texto.replace("!","\n"))
    archivo.close()   
     
    input("\nPresione una tecla para volver al menú principal") 
