"""
Genera una encuesta de satisfaccion (CSAT) simulada para MediSalud HIS,
con 150 respuestas distribuidas entre sedes y roles de usuario. Los puntajes
se sesgan de forma consistente con los hallazgos reales del Escenario 2:
Telemedicina y Portal de Citas concentran mas quejas de Satisfaccion, por lo
que Paciente recibe puntajes ligeramente mas bajos que Medico o Enfermeria.
"""
import csv
import random

random.seed(7)

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
ROLES = ["Medico", "Enfermeria", "Admision", "Farmacia", "Paciente", "Gerencia"]
N_RESPUESTAS = 150

# Media de puntaje CSAT (escala 1-5) por rol, calibrada con los hallazgos
# de docs/clasificacion_incidentes.md (Satisfaccion concentrada en Portal
# Citas y Telemedicina, ambos de alto uso por Paciente).
MEDIA_CSAT_POR_ROL = {
    "Medico": 3.6,
    "Enfermeria": 3.7,
    "Admision": 3.5,
    "Farmacia": 3.8,
    "Paciente": 3.1,
    "Gerencia": 4.0,
}

COMENTARIOS_POSITIVOS = [
    "El sistema funciona bien en general",
    "Facil de usar una vez que aprendes el flujo",
    "Buena experiencia en esta ocasion",
    "Sin problemas relevantes",
]
COMENTARIOS_NEGATIVOS = [
    "El formulario de agendamiento es confuso",
    "El audio se desincroniza durante la videoconsulta",
    "Es lento en horas pico",
    "Tuve que repetir varias veces la misma accion",
]


def generar_puntaje(rol):
    media = MEDIA_CSAT_POR_ROL[rol]
    valor = round(random.gauss(media, 0.9))
    return max(1, min(5, valor))


def generar_comentario(puntaje):
    if puntaje >= 4:
        return random.choice(COMENTARIOS_POSITIVOS)
    if puntaje == 3:
        return ""
    return random.choice(COMENTARIOS_NEGATIVOS)


filas = []
for respuesta_id in range(1, N_RESPUESTAS + 1):
    sede = random.choice(SEDES)
    rol = random.choice(ROLES)
    puntaje = generar_puntaje(rol)
    filas.append({
        "respuesta_id": respuesta_id,
        "sede": sede,
        "rol": rol,
        "puntaje_csat": puntaje,
        "comentario": generar_comentario(puntaje),
    })

with open("data/encuesta_satisfaccion.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=filas[0].keys())
    writer.writeheader()
    writer.writerows(filas)

print(f"Se generaron {len(filas)} respuestas en data/encuesta_satisfaccion.csv")
