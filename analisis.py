"""
Escenario 1 - Paso 3: Analisis dirigido del caso MediSalud.
Genera docs/analisis_inicial.md a partir de data/incidentes_2025_iso_25022.csv,
respondiendo con evidencia las 4 preguntas guia de la Tabla 1.1 del taller.
"""
import pandas as pd

CSV_PATH = "incidentes_2025_iso_25022.csv"
OUTPUT_PATH = "docs/analisis_inicial.md"

# Mapeo modulo -> proceso critico del negocio (seccion "Procesos Criticos del Negocio")
PROCESO_POR_MODULO = {
    "HCE": "Atencion medica y registro de historia clinica",
    "Portal Citas": "Agendamiento y admision de pacientes",
    "Facturacion": "Facturacion y gestion de seguros/reaseguros",
    "Telemedicina": "Telemedicina y seguimiento remoto",
    "Farmacia": "Prescripcion y dispensacion de medicamentos",
    "Reportes Gerenciales": "Generacion de reportes gerenciales",
    "App Movil": "Agendamiento y admision de pacientes (canal movil)",
    "Laboratorio": "Atencion medica y registro de historia clinica (apoyo diagnostico)",
    "Imagenologia": "Atencion medica y registro de historia clinica (apoyo diagnostico)",
}

df = pd.read_csv(CSV_PATH)
total_incidentes = len(df)

por_modulo = df["modulo"].value_counts()
por_rol = df["rol_usuario"].value_counts()
por_sede = df["sede"].value_counts()

top3_modulos = por_modulo.head(3)
top3_roles = por_rol.head(3)

print("Analisis de incidentes por modulo:")
for modulo, count in por_modulo.items():
    pct = 100 * count / total_incidentes
    print(f"  {modulo}: {count} incidentes ({pct:.1f}%)")

print("\nAnalisis de incidentes por rol de usuario:")
for rol, count in por_rol.items():
    pct = 100 * count / total_incidentes
    print(f"  {rol}: {count} incidentes ({pct:.1f}%)")

print("\nAnalisis de incidentes por sede:")
for sede, count in por_sede.items():
    pct = 100 * count / total_incidentes
    print(f"  {sede}: {count} incidentes ({pct:.1f}%)")

# --- Construccion de las respuestas de la Tabla 1.1 ---

procesos_top = []
for modulo, count in top3_modulos.items():
    proceso = PROCESO_POR_MODULO.get(modulo, modulo)
    pct = 100 * count / total_incidentes
    procesos_top.append(f"**{proceso}** (modulo `{modulo}`: {count} incidentes, {pct:.1f}% del total)")

respuesta_p1 = (
    "Segun el volumen de incidentes reportados en 2025 (" + f"{total_incidentes} registros" + "), "
    "los 3 procesos con mas incidentes son: 1) " + procesos_top[0] + "; 2) " + procesos_top[1] +
    "; y 3) " + procesos_top[2] + ". Coinciden con los procesos de mayor riesgo clinico, "
    "reputacional y financiero descritos en el caso de estudio."
)

roles_top = []
for rol, count in top3_roles.items():
    pct = 100 * count / total_incidentes
    roles_top.append(f"**{rol}** ({count} incidentes, {pct:.1f}%)")

respuesta_p2 = (
    "Los usuarios mas afectados son " + roles_top[0] + ", seguidos de " + roles_top[1] +
    " y " + roles_top[2] + ". Esto confirma que la problematica no solo es percibida por TI, "
    "sino que impacta directamente la experiencia de pacientes y personal clinico."
)

respuesta_p3 = (
    f"Hoy MediSalud cuenta con: (a) disponibilidad/uptime de servidores reportado por TI, y "
    f"(b) un registro crudo de {total_incidentes} incidentes reportados durante 2025 "
    "(`incidentes_2025_iso_25022.csv`), sin clasificar segun las caracteristicas de ISO/IEC 25022 "
    "ni convertido aun en metricas o indicadores. Es evidencia reactiva (quejas), no medicion proactiva."
)

respuesta_p4 = (
    "Falta evidencia estructurada de Calidad en Uso: metricas normalizadas de efectividad "
    "(tasa de tareas completadas), eficiencia (tiempos reales de tarea, ej. registro de HCE), "
    "satisfaccion (encuestas), libertad de riesgo (incidentes de seguridad/datos clinicos, ej. "
    "el caso de datos de otro paciente visibles) y cobertura de contexto (comparacion entre sedes). "
    "Tambien falta clasificar este dataset segun las 5 caracteristicas de ISO/IEC 25022 (Escenario 2)."
)

contenido = f"""# Analisis Inicial del Caso MediSalud (Escenario 1)

Fuente de datos: `{CSV_PATH}` ({total_incidentes} incidentes registrados en 2025).

## Tabla 1.1: Matriz de analisis inicial del caso MediSalud

| Pregunta guia | Respuesta del grupo |
|---|---|
| ¿Cuales son los 3 procesos mas criticos del negocio? | {respuesta_p1} |
| ¿Que usuarios se ven mas afectados por la problematica actual? | {respuesta_p2} |
| ¿Que evidencia tiene hoy MediSalud sobre la calidad de su software? | {respuesta_p3} |
| ¿Que evidencia le falta? | {respuesta_p4} |

## Datos de respaldo

### Incidentes por modulo

| Modulo | Incidentes | % del total |
|---|---|---|
""" + "\n".join(
    f"| {modulo} | {count} | {100 * count / total_incidentes:.1f}% |"
    for modulo, count in por_modulo.items()
) + """

### Incidentes por rol de usuario

| Rol | Incidentes | % del total |
|---|---|---|
""" + "\n".join(
    f"| {rol} | {count} | {100 * count / total_incidentes:.1f}% |"
    for rol, count in por_rol.items()
) + """

### Incidentes por sede

| Sede | Incidentes | % del total |
|---|---|---|
""" + "\n".join(
    f"| {sede} | {count} | {100 * count / total_incidentes:.1f}% |"
    for sede, count in por_sede.items()
) + "\n"

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(contenido)

print(f"\nArchivo generado: {OUTPUT_PATH}")
