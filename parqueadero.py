import datetime # este datetime pemite usar una libreria para poner la hora y fecha real que tiene el computador
import math # este match ayuda a redondear las horas y asi despues saber cuantas horas se cobran
# se crea vectores de 11 espacios vacios, indices del 0 al 10
parqueadero = [" "] * 11
tipos = [" "] * 11
horas = [" "] * 11

total_vehiculos = 0
ganancias = 0
# el while true ayuda a que el menu no se cierre
while True:
    print("\n--- MENU ---")
    print("1. Ingresar vehiculo")
    print("2. Mostrar ubicacion")
    print("3. Sacar vehiculo")
    print("4. Cierre facturacion")
    print("5. Salir del programa")

    opcion = input("que desea hacer? : ")
#aqui en la variable opcion se guarda lo que escribe el usuario y tambien pedimos al usuario en que puesto desea estacionar el vehiculo 
    if opcion == "1":
        print("\n---Puestos disponibles---")
        for i,p in enumerate(parqueadero): # recorre todo el vector para que se muestre completo
            if p == " ":
                print(f"puesto {i}: Vacio")
            else:
                print(f"puesto {i}: Ocupado por {p}")

        try:
            puesto_elegido = int(input("\n¿En que puesto desea parquear? (0 al 10): "))
        except:
            print("Debe ingresar un numero del 0 al 10")
            continue

        if puesto_elegido < 0 or puesto_elegido > 10: # valida que el puesto exista
            print("Puesto no valido, solo del 0 al 10")
        elif parqueadero[puesto_elegido]!= " ": # valida que no este ocupado
            print(f"El puesto {puesto_elegido} ya esta ocupado por {parqueadero[puesto_elegido]}")
        else:
            placa = input("ingrese numero de placa: ").upper()
            if placa in parqueadero: # valida que la placa no este repetida
                print(f"Esa placa ya esta en el puesto {parqueadero.index(placa)}")
            else:
                print("1. carro")
                print("2. moto")
                print("3. patineta")
                tipo_opcion = input("seleccione un tipo (1-3): ")
    # se lanza los 3 tipos de vehiculo en caso de que se elija la opcion uno de ingresar vehiculo
                if tipo_opcion == "1":
                    tipo = "carro"
                elif tipo_opcion == "2":
                    tipo = "moto"
                else:
                    tipo = "patineta"
    #la funcion datetime como se menciono antes ayuda a que se pueda dar una fecha y hora real que tiene el computador, se importo en la primera linea
                hora_ingreso = datetime.datetime.now()
                parqueadero[puesto_elegido] = placa
                tipos[puesto_elegido] = tipo
                horas[puesto_elegido] = hora_ingreso
                total_vehiculos += 1
                print(f"\nvehiculo {placa} en puesto {puesto_elegido} a las {hora_ingreso.strftime('%d/%m/%Y %H:%M:%S')}")

# con el elif preguntamos cuando en la anterior no se cumplio un requisito esto hace que no se tenga que escribir un if dentro de otro if
    elif opcion == "2": # mostramos ubicacion
        print("\n---Parqueadero---")
        for i,p in enumerate(parqueadero):# recorre todo el vector para que se muestre completo
            if p == " ":
                print(f"puesto {i}: Vacio")
            else: # si esta ocupado entonces
                print(f"puesto {i}: {tipos[i]} - {p} - {horas[i].strftime('%d/%m/%Y %H:%M:%S')}")# se muestra fecha y hora de manera ordenado

    elif opcion == "3": # sacar vehiculo
        placa = input("placa a sacar: ").upper() # se pide placa ingresada en el parqueadero para poder sacarla
        if placa in parqueadero:
            pos = parqueadero.index(placa)# el index permite la pocision donde esta la placa
            horas_salida = datetime.datetime.now()
            diferencia = (horas_salida - horas[pos]).total_seconds() / 3600
            horas_cobradas = math.ceil(diferencia) or 1

            tarifa = 3000 if tipos[pos] == "carro" else 2000 if tipos[pos] == "moto" else 1000 # se saca los tipos para saber que se cobra
            total_pago = horas_cobradas * tarifa
            ganancias += total_pago # se suma ganancias totales

            print(f"\nTotal a pagar {placa}: ${total_pago} por {horas_cobradas} hora(s)") # se muestran datos

            parqueadero[pos] = " "
            tipos[pos] = " "
            horas[pos] = " "
        else:
            print("no se encontro vehiculo")

    elif opcion == "4":
        print(f"\n---Cierre--- Ganancias: ${ganancias} - Total ingresados: {total_vehiculos}")#total de el historial

    elif opcion == "5":
        print("\nSaliendo del programa...")
        print(f"Ganancia final del dia: ${ganancias}")# se muestra las ganancias del dia en el momento en el que se cierra el programa
        break # cierra los ciclos para poder salir

    else:
        print("opcion no valida")