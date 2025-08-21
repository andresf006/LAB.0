import math
def bsa(height_cm, weight_kg):
    """
    BSA = sqrt((height_cm * weight_kg) / 3600)
    """
    return math.sqrt((height_cm * weight_kg) / 3600)

valor = (input("Ingrese Altura (cm) y Peso (kg), separados por una coma: " )).split(",")
h = float(valor[0])
w = float(valor[1])
tupla = (h, w)
area = bsa(*tupla)
print(tupla)
print(f"BSA estimada: {area:.2f} m²")
    
if area <= 0.25:
    print (f"Usted se encuentra en el rango BSA de: Recién nacido")
elif area <= 0.5:
    print (f"Usted se encuentra en el rango BSA de: Lactante")
elif area <= 1.14:
    print (f"Usted se encuentra en el rango BSA de: Niño")
elif area <= 1.6:
    print (f"Usted se encuentra en el rango BSA de: Mujer adulta")
elif area <= 1.9:
    print (f"Usted se encuentra en el rango BSA de: Hombre adulto")
else:
    print(f"Usted se encuentra en el rango BSA de: Adultos muy altos/pesados")
