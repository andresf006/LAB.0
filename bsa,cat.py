import math
def bsa(height_cm, weight_kg):
    """
    BSA = sqrt((height_cm * weight_kg) / 3600)
    """
    return math.sqrt((height_cm * weight_kg) / 3600)


h = float(input("Altura (cm): "))
w = float(input("Peso (kg): "))
area = bsa(h, w)
print(f"BSA estimado: {area:.2f} m²")
    
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
