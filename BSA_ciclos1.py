import math

def bsa(height_cm, weight_kg):
    return math.sqrt((height_cm * weight_kg) / 3600)

def clasificar_simple(area):
    if area < 1.5:
        return "Bajo"
    elif 1.5 <= area <= 2.0:
        return "Normal"
    else:
        return "Alto"


n = int(input("Ingrese el número de personas: "))
categorias = []
for i in range(n):
        print(f"Persona {i+1}:")
        h, w = map(float, input("Ingrese altura (cm) y peso (kg), separados por coma: ").split(","))
        area = bsa(h, w)
        cat = clasificar_simple(area)
        categorias.append(cat)
        print(f"BSA: {area:.2f} m² - Categoría: {cat}")
print("\ncategorías totales:")
print(categorias)
