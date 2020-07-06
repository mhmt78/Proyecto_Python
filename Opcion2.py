from Funciones import es_moneda, get_precio, actualizar_dato, es_numero
from Funciones import es_mi_codigo, obtener_cantidad_Cripto, insertar_transaccion

def Op2():
       
    nombre_archivo = "Criptomonedas.txt"
    
    crypto = input("Ingrese el nombre de la criptomoneda: ")
    if es_moneda(crypto):
        
        cantCrypto = ""
        while not es_numero(cantCrypto):            
            cantCrypto = input("Indique la cantidad de " + crypto + " a transferir: ")
        
        codigo_vendedor = input("Ingrese el código del destinatario: ")

        if not es_mi_codigo(codigo_vendedor):
            print("Codigo validado")

            cantCryptoOriginal = obtener_cantidad_Cripto(nombre_archivo, crypto)

            if  float(cantCryptoOriginal) > float(cantCrypto):
                data = get_precio(crypto+"USDT").json()
                cotiUSD = data["price"]
                total = float(cantCrypto) * float(cotiUSD)

                print("\nResumen de datos:\n")
        
                print("Moneda: " + crypto)
                print("Cantidad a transferir: " + cantCrypto)
                print("El precio de la moneda " + crypto + " en dólares es: USD " + data["price"])
                print("Total a transferir en: USD " + str(total))            

                nuevoMonto = float(cantCryptoOriginal) - float(cantCrypto)

                actualizar_dato(nombre_archivo, crypto + ':' + cantCryptoOriginal, crypto + ':' + str(nuevoMonto))    

                insertar_transaccion(crypto, 'Envío Criptomoneda',codigo_vendedor, cantCrypto, cotiUSD)

                input("\nPresione una tecla para volver al menú principal") 

                return
            else:
                print("La cantidad a transferir supera el monto en la billetera, no se puede realizar la operación")
                Op2()
        else:
            print("El código utilizado es igual al código de la billetera personal, función inválida")
            Op2()        

    else:
        print("La moneda ingresada no es válida.")
        Op2()    
     
    input("\nPresione una tecla para volver al menú principal") 
