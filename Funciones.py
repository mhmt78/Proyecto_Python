import requests
import time

def get_precio(cryptoMoneda):
    '''Funcion que se conecta a la API de Binance para buscar el valor de una criptomoneda en USD'''
    return requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+cryptoMoneda)

def es_numero(numero): 
    '''Funcion que verifica que el valor ingresado sea un número'''
    return numero.replace('.','',1).isdigit()

def es_moneda(cryptoMoneda):
    '''Funcion que verifica que el valor ingresado sea una criptomoneda '''
    criptos = ["BTC","LTC","ETH"]
    if cryptoMoneda in criptos:
        return True
    else:        
        return False

def es_mi_codigo(codigo):
    '''Funcion que valida si el código ingresado pertenece al usuario '''
    mi_codigo = ["1kJmKcDTE2"]
    return codigo in mi_codigo

def actualizar_dato(archivo,buscar,reemplazar):
	"""
	Función cambia una linea entera de un archivo
	Tiene que recibir el nombre del archivo, la cadena a buscar,
    y la cadena a reemplazar si la linea coincide con buscar
	"""
 
	with open(archivo, "r") as f:
		lines = (line.rstrip() for line in f)
 
		altered_lines = [reemplazar if line==buscar else line for line in lines]
 
	with open(archivo, "w") as f:
		f.write('\n'.join(altered_lines) + '\n')

def obtener_cantidad_Cripto(nombre_archivo,crypto):
    
    archivo = open(nombre_archivo,"r")    
    texto = archivo.read()
    archivo.close()
    
    lineas = texto.splitlines()    
    
    diccionario={}
    for linea in lineas:
        termino = linea.split(":")        
        diccionario[termino[0]]=termino[1]
      
    return diccionario.get(crypto) 

def insertar_transaccion(cripto, operacion, codigo_user, cantCripto, cotiUSD):
    
    nombre_archivo = "Transacciones.txt"
    
    archivo = open(nombre_archivo,"a")
    archivo.write("\n" + "Fecha: " + time.strftime("%c") + " ! Moneda: " + cripto + " ! Operación: " + operacion + " ! Código de usuario: " + codigo_user + " ! Cantidad: " + cantCripto + " ! Monto en USD: " + cotiUSD + " !" )        
    archivo.close()