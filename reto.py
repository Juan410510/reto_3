def calcular_altitud(presion_hpa):
    altitud = 44330 * (1 - (presion_hpa / 1013.25) ** 0.1903)
    return altitud
def determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion):
    if altitud_actual > altitud_previa:
        estado = "1: Ascenso"
    elif aceleracion < 0:
        estado = "2: Apogeo / Caída libre"
    else:
        estado = "3: Despliegue de Paracaídas"
    return estado
def evaluar_alerta_temperatura(temp_celsius):
    if temp_celsius > 100:
        alerta = True
    else:
        alerta = False
    return alerta
tiempo = 0
altitud = 0.0
altitud_previa = 0.0
altitud_maxima = 0.0
aceleracion_maxima = 0.0
suma_temperatura = 0.0
apogeo = False
continuar = 1
while continuar == 1:
    print("\n--- Lectura del segundo t =", tiempo, "---")
    presion = float(input("Ingrese la presion (hPa): "))
    temperatura = float(input("Ingrese la temperatura (C): "))
    aceleracion = float(input("Ingrese la aceleracion (m/s^2): "))
    altitud = calcular_altitud(presion)
    estado_vuelo = determinar_estado_vuelo(altitud, altitud_previa, aceleracion)
    evaluacion_temperatura = evaluar_alerta_temperatura(temperatura)
    if altitud > altitud_maxima:
        altitud_maxima = altitud
    if altitud < altitud_previa and apogeo == False and tiempo > 0:
        apogeo = True
        alerta_apogeo = "ALERTA: Apogeo detectado, el cohete comienza el descenso"
        print(alerta_apogeo)
    suma_temperatura = suma_temperatura + temperatura
    if aceleracion > aceleracion_maxima or tiempo == 0:
        aceleracion_maxima = aceleracion
    print("Altitud actual:", round(altitud, 2), "m")
    print("Estado del vuelo:", estado_vuelo)
    if evaluacion_temperatura == True:
        alerta_temperatura = "ALERTA: Temperatura critica superada"
        print(alerta_temperatura)
    altitud_previa = altitud
    tiempo = tiempo + 1
    if altitud <= 0 and tiempo > 1:
        print("\nEl cohete ha aterrizado (altitud <= 0).")
        continuar = 0
    else:
        continuar = int(input("¿Desea ingresar el siguiente segundo? (1 = Si, 0 = Finalizar): "))

temperatura_promedio = suma_temperatura / tiempo
print("\n=== ESTADISTICAS FINALES DEL VUELO ===")
print("Altitud maxima alcanzada:", round(altitud_maxima, 2), "m")
print("Temperatura promedio:", round(temperatura_promedio, 2), "C")
print("Aceleracion maxima:", round(aceleracion_maxima, 2), "m/s^2")