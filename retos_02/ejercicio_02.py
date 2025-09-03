luz_solar = input("¿Hay luz solar?: ")
humedad = int(input("Ingrese el nivel de humedad de 0 a 100: "))

hay_luz = luz_solar == "True"
humedad_baja = humedad < 30

activa = not ((hay_luz and humedad_baja) or (not hay_luz and not humedad_baja))

(not activa) and print("El sistema de riego no se activa")
(activa) and print("El sistema de riego se activa")
