from Funciones import es_moneda, get_precio, actualizar_dato, es_numero
from Funciones import es_mi_codigo, obtener_cantidad_Cripto, insertar_transaccion

def Op1():
    
    nombre_archivo = "Criptomonedas.txt"
    
    crypto = input("Ingrese el nombre de la criptomoneda: ")
    
    if es_moneda(crypto):
        
        cantCrypto = ""
        while not es_numero(cantCrypto):            
            cantCrypto = input("Indique la cantidad de " + crypto + " a recibir: ")
        
        codigo_vendedor = input("Ingrese el código del vendedor: ")

        if not es_mi_codigo(codigo_vendedor):
            print("Codigo validado")

            data = get_precio(crypto+"USDT").json()
            cotiUSD = data["price"]
            total = float(cantCrypto) * float(cotiUSD)

            print("\nResumen de datos:\n")
    
            print("Moneda: " + crypto)
            print("Cantidad a recibir: " + cantCrypto)
            print("El precio de la moneda " + crypto + " en dólares es: USD " + data["price"])
            print("Total a recibir en: USD " + str(total))
            
            cantCryptoOriginal = obtener_cantidad_Cripto(nombre_archivo, crypto)

            nuevoMonto = float(cantCryptoOriginal) + float(cantCrypto)

            actualizar_dato(nombre_archivo, crypto + ':' + cantCryptoOriginal, crypto + ':' + str(nuevoMonto))    

            insertar_transaccion(crypto, 'Recepción Criptomoneda',codigo_vendedor, cantCrypto, cotiUSD)

            input("\nPresione una tecla para volver al menú principal") 

            return
        else:
            print("El código utilizado es igual al código de la billetera personal, función inválida")
            Op1()        

    else:
        print("La moneda ingresada no es válida.")
        Op1()    
     
    input("\nPresione una tecla para volver al menú principal") 
