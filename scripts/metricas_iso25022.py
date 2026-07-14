"""
Modulo de calculo de metricas de Calidad en Uso (ISO/IEC 25022)
para el sistema MediSalud HIS.

Cada funcion retorna un diccionario con: valor, unidad, umbral y estado.
Adaptado a los archivos generados/validados en el Escenario 7 y a la
matriz de metricas del Escenario 6 (docs/diseno_metricas.md).
"""
import pandas as pd

UMBRAL_TIEMPO_TAREA = 8.0       # segundos, segun RNF-01
UMBRAL_TASA_ERROR_FACT = 0.01   # 1%, segun RNF-03
UMBRAL_EFECTIVIDAD = 0.95       # 95% de completitud esperada
UMBRAL_SATISFACCION = 0.80      # equivalente a 4.0/5.0 (Metrica 3)
UMBRAL_COBERTURA_CONTEXTO = 0.85  # diferencia entre sedes <= 15% (Metrica 5)

# Periodo de medicion cubierto por data/logs_hce.csv (Escenario 7)
PERIODO_INICIO = "2025-11-03"
PERIODO_FIN = "2025-11-07"

# Total de transacciones de facturacion simuladas en el periodo de medicion
# (dato hipotetico equivalente al que en un caso real proveeria el area
# financiera; ver limitacion documentada en el Escenario 7).
TOTAL_TRANSACCIONES_FACTURACION = 1700


def cargar_datos():
    """Carga los tres datasets base del programa de medicion."""
    logs = pd.read_csv("data/logs_hce.csv")
    encuesta = pd.read_csv("data/encuesta_satisfaccion.csv")
    incidentes = pd.read_csv("data/incidentes_2025_clasificados.csv")
    return logs, encuesta, incidentes


def metrica_efectividad(logs: pd.DataFrame) -> dict:
    """
    Efectividad = notas completadas correctamente / notas intentadas.
    """
    total = len(logs)
    completadas = logs["completada"].sum()
    valor = round(completadas / total, 4) if total else 0.0
    return {
        "nombre": "Completitud de registro de HCE",
        "caracteristica": "Efectividad",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_EFECTIVIDAD,
        "cumple": bool(valor >= UMBRAL_EFECTIVIDAD),
    }


def metrica_eficiencia(logs: pd.DataFrame) -> dict:
    """
    Eficiencia = tiempo promedio de registro de nota clinica (segundos),
    calculado solo sobre notas completadas (ver Escenario 7, Pregunta 1).
    """
    completados = logs[logs["completada"] == 1]
    valor = round(completados["tiempo_segundos"].mean(), 2)
    return {
        "nombre": "Tiempo promedio de registro de HCE",
        "caracteristica": "Eficiencia",
        "valor": valor,
        "unidad": "segundos",
        "umbral": UMBRAL_TIEMPO_TAREA,
        "cumple": bool(valor <= UMBRAL_TIEMPO_TAREA),
    }


def metrica_eficiencia_por_sede(logs: pd.DataFrame) -> pd.DataFrame:
    """Desagrega el tiempo promedio de tarea por sede."""
    return (
        logs[logs["completada"] == 1]
        .groupby("sede")["tiempo_segundos"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"tiempo_segundos": "tiempo_promedio_segundos"})
    )


def metrica_eficiencia_hora_pico(logs: pd.DataFrame) -> dict:
    """
    Desagrega la Eficiencia por franja horaria (pico 10-12h vs. resto),
    para evitar que un promedio diario oculte la degradacion en hora pico
    (ver Escenario 4, Pregunta 2, y Escenario 7).
    """
    completados = logs[logs["completada"] == 1].copy()
    completados["hora"] = pd.to_datetime(completados["timestamp"]).dt.hour
    en_pico = completados["hora"].between(10, 12)

    tiempo_pico = round(completados.loc[en_pico, "tiempo_segundos"].mean(), 2)
    tiempo_resto = round(completados.loc[~en_pico, "tiempo_segundos"].mean(), 2)
    pct_incumple_pico = round((completados.loc[en_pico, "tiempo_segundos"] > UMBRAL_TIEMPO_TAREA).mean() * 100, 1)

    return {
        "nombre": "Tiempo promedio de registro de HCE en hora pico (10-12h)",
        "caracteristica": "Eficiencia",
        "valor": tiempo_pico,
        "unidad": "segundos",
        "umbral": UMBRAL_TIEMPO_TAREA,
        "cumple": bool(tiempo_pico <= UMBRAL_TIEMPO_TAREA),
        "tiempo_promedio_resto_del_dia": tiempo_resto,
        "pct_registros_en_pico_que_incumplen": pct_incumple_pico,
    }


def metrica_cobertura_contexto(eficiencia_sede: pd.DataFrame) -> dict:
    """
    Cobertura de Contexto = 1 - |Metrica sede A - Metrica sede B| / Metrica sede A,
    comparando la sede con mayor y menor tiempo promedio (Metrica 5, Escenario 6).
    """
    peor = eficiencia_sede.loc[eficiencia_sede["tiempo_promedio_segundos"].idxmax()]
    mejor = eficiencia_sede.loc[eficiencia_sede["tiempo_promedio_segundos"].idxmin()]
    valor = round(1 - (peor["tiempo_promedio_segundos"] - mejor["tiempo_promedio_segundos"]) / peor["tiempo_promedio_segundos"], 4)
    return {
        "nombre": "Consistencia del tiempo de registro entre sedes",
        "caracteristica": "Cobertura de Contexto",
        "valor": valor,
        "unidad": "indice (0-1)",
        "umbral": UMBRAL_COBERTURA_CONTEXTO,
        "cumple": bool(valor >= UMBRAL_COBERTURA_CONTEXTO),
        "sede_mejor": mejor["sede"],
        "sede_peor": peor["sede"],
    }


def metrica_satisfaccion(encuesta: pd.DataFrame) -> dict:
    """
    Satisfaccion = promedio de puntaje CSAT (escala 1-5), normalizado a 0-1.
    """
    promedio_csat = encuesta["puntaje_csat"].mean()
    valor = round(promedio_csat / 5, 4)
    return {
        "nombre": "Indice de satisfaccion (CSAT normalizado)",
        "caracteristica": "Satisfaccion",
        "valor": valor,
        "unidad": "proporcion (0-1)",
        "umbral": UMBRAL_SATISFACCION,
        "cumple": bool(valor >= UMBRAL_SATISFACCION),
    }


def metrica_libertad_riesgo(incidentes: pd.DataFrame, total_transacciones: int) -> dict:
    """
    Libertad de Riesgo = tasa de incidentes de facturacion sobre el total
    de transacciones de facturacion procesadas en el periodo de medicion.
    """
    incidentes["fecha_dt"] = pd.to_datetime(incidentes["fecha"], format="%m/%d/%Y")
    en_periodo = incidentes[
        (incidentes["fecha_dt"] >= PERIODO_INICIO) & (incidentes["fecha_dt"] <= PERIODO_FIN)
    ]
    incidentes_facturacion = en_periodo[en_periodo["modulo"] == "Facturacion"]
    valor = round(len(incidentes_facturacion) / total_transacciones, 4)
    return {
        "nombre": "Tasa de errores de facturacion",
        "caracteristica": "Libertad de Riesgo",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_TASA_ERROR_FACT,
        "cumple": bool(valor <= UMBRAL_TASA_ERROR_FACT),
    }


def generar_reporte():
    """Orquesta el calculo de todas las metricas y consolida el resultado."""
    logs, encuesta, incidentes = cargar_datos()

    eficiencia_sede = metrica_eficiencia_por_sede(logs)

    reporte = {
        "efectividad": metrica_efectividad(logs),
        "eficiencia": metrica_eficiencia(logs),
        "eficiencia_hora_pico": metrica_eficiencia_hora_pico(logs),
        "cobertura_contexto": metrica_cobertura_contexto(eficiencia_sede),
        "satisfaccion": metrica_satisfaccion(encuesta),
        "libertad_riesgo": metrica_libertad_riesgo(incidentes, TOTAL_TRANSACCIONES_FACTURACION),
    }

    return reporte, eficiencia_sede


if __name__ == "__main__":
    reporte, eficiencia_sede = generar_reporte()

    print("=== Reporte de Calidad en Uso - MediSalud HIS ===\n")
    for clave, metrica in reporte.items():
        estado = "CUMPLE" if metrica["cumple"] else "NO CUMPLE"
        print(f"{metrica['nombre']}: {metrica['valor']} {metrica['unidad']} "
              f"(umbral: {metrica['umbral']}) -> {estado}")

    print("\n=== Eficiencia por sede (Cobertura de Contexto) ===")
    print(eficiencia_sede.to_string(index=False))
