"""
Escenario 2 - Paso 2: Clasificacion de incidentes segun las 5 caracteristicas
de Calidad en Uso de ISO/IEC 25022 (Efectividad, Eficiencia, Satisfaccion,
Libertad de Riesgo, Cobertura de Contexto).

Clasifica los 3000 incidentes reales de incidentes_2025_iso_25022.csv con un
motor de reglas (diccionario de patrones exactos + regex para patrones con
valores numericos variables, p.ej. "Nota de evolucion tarda 22s en guardarse").
Genera:
  - data/incidentes_2025_clasificados.csv (dataset completo con caracteristica y justificacion)
  - docs/clasificacion_incidentes.md (Tabla 2.2, resumen cuantitativo y respuestas del escenario)
"""
import re
import pandas as pd

CSV_PATH = "incidentes_2025_iso_25022.csv"
OUT_CSV = "data/incidentes_2025_clasificados.csv"
OUT_MD = "docs/clasificacion_incidentes.md"

EFECTIVIDAD = "Efectividad"
EFICIENCIA = "Eficiencia"
SATISFACCION = "Satisfaccion"
RIESGO = "Libertad de Riesgo"
CONTEXTO = "Cobertura de Contexto"

# --- Reglas por patron numerico (tiempo o recurso consumido -> Eficiencia) ---
REGLAS_REGEX = [
    (re.compile(r"tarda \d+s en guardarse"), EFICIENCIA,
     "Mide el tiempo que toma completar una tarea ya lograda (guardar la nota); es una razon tiempo/tarea, propia de Eficiencia."),
    (re.compile(r"supera los \d+s"), EFICIENCIA,
     "Es un umbral de tiempo de carga/respuesta frente a una tarea que si se completa; corresponde a Eficiencia, no a Efectividad."),
    (re.compile(r"supera los \d+ minutos"), EFICIENCIA,
     "Mide duracion de un proceso que se completa (generacion de reporte); recursos (tiempo) usados para lograr el objetivo."),
    (re.compile(r"retraso de \d+s al procesar el pago"), EFICIENCIA,
     "El pago se procesa (objetivo logrado); el problema es el tiempo invertido, metrica de Eficiencia."),
    (re.compile(r"retraso de \d+s en la disponibilidad de resultados criticos"), EFICIENCIA,
     "Mide el tiempo hasta disponibilidad del resultado; es una metrica temporal (Eficiencia), aunque un retraso extremo deberia escalarse tambien como alerta de riesgo clinico."),
    (re.compile(r"retraso de \d+s\b"), EFICIENCIA,
     "Metrica de tiempo sobre una notificacion que si llega; corresponde a Eficiencia."),
    (re.compile(r"no logra agendar tras \d+ intentos"), EFECTIVIDAD,
     "El usuario no logra completar su objetivo (agendar la cita) pese a reintentar: fallo de Efectividad."),
    (re.compile(r"se corta a los \d+ minutos"), EFECTIVIDAD,
     "La teleconsulta (tarea) no se completa: el objetivo del usuario queda inconcluso, por lo tanto es Efectividad."),
]

# --- Reglas por descripcion exacta (agrupadas por caracteristica) ---
REGLAS_EXACTAS = {}


def registrar(caracteristica, justificacion, descripciones):
    for d in descripciones:
        REGLAS_EXACTAS[d] = (caracteristica, justificacion)


registrar(EFECTIVIDAD,
          "El usuario no logra completar la tarea prevista (funcion ausente, bloqueada o interrumpida), independientemente del tiempo o riesgo.",
          [
    "El sistema no envia la confirmacion por correo electronico",
    "El sistema no reconoce el convenio con la aseguradora",
    "El sistema no permite anular una factura emitida por error",
    "El chat de la consulta no permite enviar imagenes",
    "Perdida de la nota de evolucion tras un cierre inesperado de sesion",
    "El modulo de facturacion se cae durante el cierre de caja",
    "La app no permite actualizar el numero de contacto del paciente",
    "Grabacion de la consulta no se almacena correctamente",
    "La aplicacion se cierra inesperadamente al abrir resultados de laboratorio",
    "El sistema no permite adjuntar el reporte en PDF del laboratorio externo",
    "El medico no puede compartir pantalla con resultados de examenes",
    "Filtro de especialidad medica no devuelve resultados",
    "Error al reagendar una cita previamente confirmada",
    "La sesion se cierra automaticamente antes de terminar la consulta",
    "El boton de teleconsulta no redirige correctamente a la videollamada",
    "El reporte de ocupacion hospitalaria no se actualiza automaticamente",
    "Receta electronica no se genera al finalizar la teleconsulta",
    "El inicio de sesion con biometria falla de forma intermitente",
    "Las imagenes de rayos X no cargan en el visor DICOM",
    "Notificacion de recordatorio de cita llega con la fecha incorrecta",
    "El campo de diagnostico CIE-10 no permite busqueda por texto",
    "Resultados de examenes no se visualizan en formato PDF",
    "Version desactualizada del app impide iniciar sesion",
    "Factura electronica no llega al correo registrado del paciente",
    "Paciente no puede unirse a la sala virtual a la hora agendada",
    "El sistema se congela al adjuntar resultados de laboratorio a la HCE",
    "Sesion expira antes de finalizar el proceso de agendamiento",
    "Cita agendada no aparece reflejada en el calendario del especialista",
    "El sistema bloquea la dispensacion sin mostrar el motivo",
    "El dashboard de indicadores no refleja los datos del ultimo cierre",
    "Exportacion a Excel del reporte gerencial falla de forma intermitente",
    "Notificaciones push no llegan pese a estar activadas",
])

registrar(RIESGO,
          "Aunque puede describirse como un 'error del sistema', lo relevante no es si la tarea se completo sino que expone al paciente o a la organizacion a un riesgo clinico, financiero o de privacidad (Libertad de Riesgo, no Efectividad).",
          [
    "Historial de alergias no carga al abrir la ficha del paciente",
    "Duplicidad de codigos entre dos presentaciones distintas de un mismo farmaco",
    "Signos vitales registrados por enfermeria no aparecen en la HCE del medico",
    "Datos de otro paciente visibles brevemente al abrir un expediente",
    "Alerta de vencimiento de lote no se muestra en el modulo",
    "Receta electronica se genera con la dosis incorrecta tras guardar",
    "Orden medica no se sincroniza con el modulo de farmacia",
    "El sistema no descuenta automaticamente el medicamento dispensado",
    "Doble reserva de un mismo cupo por dos pacientes distintos",
    "Nota de credito no se aplica al saldo pendiente del paciente",
    "Alerta de interaccion medicamentosa no se despliega correctamente",
    "Reintento de transaccion genera doble cobro en la tarjeta",
    "Duplicado de historia clinica al registrar un paciente ya existente",
    "Error al registrar la dispensacion de un medicamento controlado",
    "Consulta anterior no se muestra en el resumen de antecedentes",
    "El pago del bono de consulta no se refleja tras completarlo",
    "Error de calculo en el copago del seguro medico",
    "Receta electronica llega incompleta desde el modulo de HCE",
    "Discrepancia entre el reporte financiero y el modulo de facturacion",
    "Reembolso aprobado no se refleja en el estado de cuenta",
    "Factura generada con el nombre del paciente incorrecto",
    "Factura duplicada al reintentar pago",
    "Orden de laboratorio duplicada tras reintentar el envio",
    "Resultado de examen de laboratorio no se sincroniza con la HCE",
    "Inventario del sistema no coincide con el stock fisico del insumo",
    "Firma electronica del medico no se valida al cerrar la consulta",
    "Codigo de barras de la muestra no es reconocido por el lector",
    "El informe radiologico no se adjunta automaticamente a la HCE",
    "El portal muestra disponibilidad para un horario ya ocupado",
    "Cancelacion de cita no libera el cupo en el calendario",
    "Discrepancia entre el monto facturado y el detalle de servicios",
])

registrar(SATISFACCION,
          "El sistema puede seguir siendo usable, pero degrada la percepcion de comodidad/confianza del usuario (calidad de experiencia), sin impedir totalmente la tarea ni exponer un riesgo concreto.",
          [
    "Formulario confuso, abandono de registro antes de completar la cita",
    "Audio desincronizado durante la teleconsulta",
    "Calidad de video muy baja pese a tener buena conexion a internet",
    "Perdida de calidad en las imagenes al ser visualizadas desde la app",
])

registrar(CONTEXTO,
          "El fallo solo se manifiesta en un contexto de uso especifico (tipo de dispositivo/canal), lo que evidencia que el sistema no mantiene su calidad fuera del contexto principal de diseno.",
          [
    "Boton de confirmar cita no responde en dispositivos moviles",
    "El sistema no permite adjuntar imagenes de heridas desde la tablet",
])

registrar(EFICIENCIA,
          "Mide el consumo de un recurso (datos moviles) necesario para lograr una tarea que si se completa, encajando en la relacion recursos/resultado de Eficiencia.",
          [
    "Consumo elevado de datos moviles al abrir el modulo de citas",
])


def clasificar(descripcion):
    if descripcion in REGLAS_EXACTAS:
        return REGLAS_EXACTAS[descripcion]
    for patron, caracteristica, justificacion in REGLAS_REGEX:
        if patron.search(descripcion.lower()):
            return caracteristica, justificacion
    return "SIN CLASIFICAR", "Descripcion no cubierta por las reglas actuales; revisar manualmente."


def main():
    df = pd.read_csv(CSV_PATH)
    df["caracteristica_iso25022"], df["justificacion"] = zip(*df["descripcion"].map(clasificar))

    sin_clasificar = df[df["caracteristica_iso25022"] == "SIN CLASIFICAR"]
    if len(sin_clasificar):
        print(f"ADVERTENCIA: {len(sin_clasificar)} incidentes sin clasificar:")
        print(sin_clasificar["descripcion"].unique())

    df.to_csv(OUT_CSV, index=False)
    print(f"Dataset clasificado guardado en {OUT_CSV}")

    total = len(df)
    resumen = df["caracteristica_iso25022"].value_counts()
    print("\nDistribucion por caracteristica ISO/IEC 25022:")
    for car, count in resumen.items():
        print(f"  {car}: {count} ({100*count/total:.1f}%)")

    resumen_modulo = pd.crosstab(df["modulo"], df["caracteristica_iso25022"])

    # --- Tabla 2.2 representativa (una fila por patron de incidente, agrupando
    # variantes que solo difieren en un valor numerico, p.ej. "tarda 9s" vs "tarda 22s") ---
    df["patron"] = df["descripcion"].str.replace(r"\d+", "#", regex=True)
    muestra = (
        df.drop_duplicates(subset="patron", keep="first")
        .sort_values(["caracteristica_iso25022", "modulo"])
        [["id", "descripcion", "modulo", "caracteristica_iso25022", "justificacion"]]
    )

    orden_caract = [EFECTIVIDAD, EFICIENCIA, SATISFACCION, RIESGO, CONTEXTO]

    def tabla_md(sub_df):
        filas = ["| ID | Descripcion | Modulo | Justificacion tecnica |", "|---|---|---|---|"]
        for _, r in sub_df.iterrows():
            filas.append(f"| {r['id']} | {r['descripcion']} | {r['modulo']} | {r['justificacion']} |")
        return "\n".join(filas)

    secciones_muestra = []
    for car in orden_caract:
        sub = muestra[muestra["caracteristica_iso25022"] == car]
        secciones_muestra.append(f"### {car} ({len(df[df['caracteristica_iso25022']==car])} incidentes, "
                                  f"{100*len(df[df['caracteristica_iso25022']==car])/total:.1f}% del total)\n\n" + tabla_md(sub))

    resumen_tabla = "| Caracteristica ISO/IEC 25022 | Incidentes | % del total |\n|---|---|---|\n" + "\n".join(
        f"| {car} | {resumen.get(car, 0)} | {100*resumen.get(car,0)/total:.1f}% |" for car in orden_caract
    )

    crosstab_md = "| Modulo | " + " | ".join(orden_caract) + " |\n" + "|---|" + "---|" * len(orden_caract) + "\n"
    for modulo in resumen_modulo.index:
        fila = [str(resumen_modulo.loc[modulo, car]) if car in resumen_modulo.columns else "0" for car in orden_caract]
        crosstab_md += f"| {modulo} | " + " | ".join(fila) + " |\n"

    # Caso real citado por el escenario para incidente tipo "1005"
    caso_riesgo = df[df["descripcion"] == "Datos de otro paciente visibles brevemente al abrir un expediente"].iloc[0]
    caso_alergia = df[df["descripcion"] == "Historial de alergias no carga al abrir la ficha del paciente"].iloc[0]

    contenido = f"""# Clasificacion de Incidentes segun ISO/IEC 25022 (Escenario 2)

Fuente de datos: `{CSV_PATH}` ({total} incidentes). Clasificacion generada por
`scripts/clasificar_incidentes.py` mediante un motor de reglas (patrones exactos
y expresiones regulares) sobre las 244 descripciones unicas del dataset, y
aplicada a las {total} filas. Dataset completo clasificado en `{OUT_CSV}`.

## Tabla 2.2: Clasificacion de incidentes (una fila por tipo de incidente real)

""" + "\n\n".join(secciones_muestra) + f"""

## Resumen cuantitativo por caracteristica

{resumen_tabla}

## Incidentes por modulo y caracteristica

{crosstab_md}

## Actividad para el Estudiante: incidente "datos de otro paciente visibles"

Caso real del dataset (id `{caso_riesgo['id']}`, modulo `{caso_riesgo['modulo']}`):
*"{caso_riesgo['descripcion']}"*.

**¿Por que corresponde a Libertad de Riesgo y no a Efectividad, a pesar de tratarse
tambien de un error del sistema?** Porque la pregunta que define Efectividad es
"¿el usuario logro su objetivo?" -- en este caso el medico si pudo completar su
tarea (abrir el expediente). El problema no es la tarea del usuario que la reporta,
sino que el sistema **expuso datos clinicos de un tercero**, lo cual es un riesgo de
privacidad y cumplimiento normativo (proteccion de datos en salud) independiente
de si la tarea original se completo o no. La misma logica aplica al incidente
id `{caso_alergia['id']}` (*"{caso_alergia['descripcion']}"*): que no cargue el
historial de alergias no es solo una falla funcional, es una condicion que puede
llevar a que el medico prescriba un medicamento contraindicado -- un riesgo clinico,
no solo una tarea incompleta.

## Preguntas de Discusion

**1. ¿Puede un sistema ser efectivo pero no eficiente? De un ejemplo del caso MediSalud.**

Si. Por ejemplo, "Nota de evolucion tarda 28s en guardarse": el medico logra
guardar la nota (Efectividad cumplida, la tarea se completa), pero el tiempo
invertido excede por mucho el umbral RNF-01 (8s en el 90% de los casos), por lo
que el sistema es efectivo pero deficiente en Eficiencia.

**2. ¿Por que la Cobertura de Contexto es especialmente relevante para una red
hospitalaria con sedes en cinco ciudades distintas?**

Porque MediSalud no opera en un unico contexto: cada sede (Quito, Guayaquil,
Cuenca, Ambato, Manta) puede tener conectividad, dispositivos y volumen de
usuarios distintos. Un modulo que funciona bien en Quito (mejor infraestructura)
podria fallar en Manta; y canales como el portal movil introducen contextos de
uso (dispositivos, redes moviles) no siempre contemplados en el diseno original.
Los incidentes de tipo "{CONTEXTO}" (p. ej. boton de confirmar cita que no
responde en moviles, adjuntar imagenes desde tablet) muestran que la calidad
del sistema no es uniforme entre contextos, lo cual justifica medir
explicitamente esta caracteristica y no asumir que un resultado positivo en
un contexto se replica en todos.

## Conclusiones Parciales

La clasificacion basada en reglas sobre las {len(REGLAS_EXACTAS) + len(REGLAS_REGEX)}
patrones de incidente identificados en los datos reales confirma el patron de
confusion mencionado en el taller: una lectura superficial tenderia a marcar la
mayoria de estos incidentes como "Efectividad", pero al aplicar la pregunta guia
("¿logro su objetivo?" vs "¿a que costo o riesgo lo logro?") una parte importante
se reclasifica como Eficiencia (temporizaciones) o Libertad de Riesgo (seguridad
clinica, financiera y de privacidad). Esto valida que ISO/IEC 25022 aporta un
vocabulario comun que evita reportar todos los problemas de forma ambigua como
"el sistema falla".
"""

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"\nReporte generado: {OUT_MD}")


if __name__ == "__main__":
    main()
