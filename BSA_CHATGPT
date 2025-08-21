import math

def bsa(height_cm, weight_kg):
    """
    Calcula la superficie corporal (BSA) usando la fórmula:
    BSA = sqrt((altura_cm * peso_kg) / 3600)
    """
    return math.sqrt((height_cm * weight_kg) / 3600)


h = float(input("Altura (cm): "))
w = float(input("Peso (kg): "))
area = bsa(h, w)
 
print(f"BSA estimada: {area:.2f} m²")

    # Clasificación según rangos clínicos reales
if area < 1.50:
        categoria = "Baja superficie corporal"
elif 1.50 <= area <= 2.00:
        categoria = "Normal"
else:
        categoria = "Alta superficie corporal"

print(f"Clasificación: {categoria}")
