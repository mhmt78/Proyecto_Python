import requests
from Funciones import es_moneda, get_precio

def Op4():
    totalGeneral = 0.0
    nombre_archivo = "Criptomonedas.txt"
    archivo = open(nombre_archivo,"r")
    
    texto = archivo.read()
    archivo.close()
    lineas = texto.splitlines()    
    
    print("\nResumen de datos:\n")
        
    for linea in lineas:
        termino = linea.split(":")

        crypto = termino[0]
        cantCrypto = termino[1]
        data = get_precio(crypto+"USDT").json()
        cotiUSD = data["price"]
        totalMoneda = float(cantCrypto) * float(cotiUSD)
        totalGeneral += totalMoneda
    
        print("Moneda: " + crypto)
        print("Cantidad en billetera: " + cantCrypto)
        print("El precio de la moneda " + crypto + " en dólares es: USD " + data["price"])
        print("Total acumulado es: USD " + str(totalMoneda) + "\n\n")    
        
    print("El total general que tienes acumulado es: USD " + str(totalGeneral))
    input("\nPresione una tecla para volver al menú principal") 