"""
Genera un log sintetico de eventos de registro de notas de evolucion clinica
en el modulo HCE de MediSalud HIS, simulando 5 dias habiles y 5 sedes.
"""
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
MEDICOS_POR_SEDE = 12
FECHA_INICIO = datetime(2025, 11, 3, 7, 0, 0)
DIAS = 5

filas = []
evento_id = 1

for dia in range(DIAS):
    fecha_dia = FECHA_INICIO + timedelta(days=dia)
    for sede in SEDES:
        # Mayor carga en Quito y Guayaquil (hospitales mas grandes)
        n_eventos = 180 if sede in ("Quito", "Guayaquil") else 90
        for _ in range(n_eventos):
            hora = random.randint(7, 18)
            minuto = random.randint(0, 59)
            timestamp = fecha_dia.replace(hour=hora, minute=minuto)

            # Simulamos que en horas pico (10-12h) el tiempo de registro sube
            es_hora_pico = 10 <= hora <= 12
            tiempo_base = random.gauss(6.5, 1.5)
            if es_hora_pico:
                tiempo_base += random.gauss(4.0, 2.0)  # degradacion en pico
            tiempo_segundos = max(1.5, round(tiempo_base, 2))

            # 96% de las notas se completan correctamente
            completada = random.random() < 0.96

            medico_id = f"MED-{sede[:3].upper()}-{random.randint(1, MEDICOS_POR_SEDE):02d}"

            filas.append({
                "evento_id": evento_id,
                "timestamp": timestamp.isoformat(),
                "sede": sede,
                "medico_id": medico_id,
                "tiempo_segundos": tiempo_segundos,
                "completada": int(completada),
            })
            evento_id += 1

with open("data/logs_hce.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=filas[0].keys())
    writer.writeheader()
    writer.writerows(filas)

print(f"Se generaron {len(filas)} eventos en data/logs_hce.csv")
