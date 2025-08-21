import math

# Función para calcular BSA con fórmula de Mosteller
def bsa(height_cm, weight_kg):
    return math.sqrt((height_cm * weight_kg) / 3600)

# Función que devuelve los límites del rango clínico normal de BSA
def rango_normal_bsa():
    return 1.5, 2.0  # Valores de referencia típicos en adultos

# Función que genera el mensaje según el rango normal
def interpretar_bsa(area):
    bajo, alto = rango_normal_bsa()
    if area < bajo:
        return f"Su BSA ({area:.2f} m²) está por DEBAJO del rango normal ({bajo} - {alto} m²)."
    elif area > alto:
        return f"Su BSA ({area:.2f} m²) está por ENCIMA del rango normal ({bajo} - {alto} m²)."
    else:
        return f"Su BSA ({area:.2f} m²) está DENTRO del rango normal ({bajo} - {alto} m²)."

# Programa principal
n = int(input("Ingrese el número de personas: "))
for i in range(n):
    print(f"\nPersona {i+1}:")
    h, w = map(float, input("Ingrese altura (cm) y peso (kg), separados por coma: ").split(","))
    area = bsa(h, w)
    mensaje = interpretar_bsa(area)
    print(mensaje)