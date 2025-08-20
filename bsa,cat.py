import math
def bsa(height_cm, weight_kg):
    """
    BSA = sqrt((height_cm * weight_kg) / 3600)
    """
    return math.sqrt((height_cm * weight_kg) / 3600)


h = float(input("Altura (cm): "))
w = float(input("Peso (kg): "))
area = bsa(h, w)
print(f"BSA estimada: {area:.2f} m²")
    
if area <= 0.25:
        print (f"Se encuentra en el rango BSA de Recién nacido")
elif area <= 0.5:
        print (f"Se encuentra en el rango BSA de Lactante")
elif area <= 1.14:
        print (f"Se encuentra en el rango BSA de niño")
elif area <= 1.6:
        print (f"Se encuentra en el rango BSA de Mujer adulta")
elif area <= 1.9:
        print (f"Se encuentra en el rango BSA de Hombre adulto")
else:
        print(f"Se encuentra en el rango BSA de adultos muy altos/pesados")
