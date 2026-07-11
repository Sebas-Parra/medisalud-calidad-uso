"""
Escenario 3 - Paso 2: evidencia cuantitativa de Calidad en Uso para la Tabla 3.2
(tiempo real de guardado de nota de evolucion en el modulo HCE), usada para
respaldar la fila "Calidad en uso" y las Preguntas de Discusion del escenario.
"""
import re
import pandas as pd

CSV_PATH = "data/incidentes_2025_clasificados.csv"
UMBRAL_RNF01_SEGUNDOS = 8

df = pd.read_csv(CSV_PATH)


def extraer_segundos(descripcion):
    m = re.search(r"(\d+)s", descripcion)
    return int(m.group(1)) if m else None


notas = df[df["descripcion"].str.contains("Nota de evolucion tarda")].copy()
notas["segundos"] = notas["descripcion"].map(extraer_segundos)

print("Nota de evolucion clinica (HCE) - tiempo de guardado")
print(f"  Incidentes registrados: {len(notas)}")
print(f"  Promedio: {notas['segundos'].mean():.1f}s (min {notas['segundos'].min()}s, max {notas['segundos'].max()}s)")
print(f"  Umbral RNF-01: {UMBRAL_RNF01_SEGUNDOS}s en el 90% de los casos")
pct_excede = (notas["segundos"] > UMBRAL_RNF01_SEGUNDOS).mean() * 100
print(f"  % de incidentes que ya excede el umbral: {pct_excede:.0f}%")

print("\nDistribucion de incidentes del modulo HCE por caracteristica ISO/IEC 25022:")
print(df[df["modulo"] == "HCE"]["caracteristica_iso25022"].value_counts())
