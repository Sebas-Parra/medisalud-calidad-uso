# Identificación de Atributos de Calidad en Uso (Escenario 4)

Modelo exigido por ISO/IEC 25022 antes de diseñar cualquier métrica: toda
tarea debe definirse mediante **Usuario primario** (quién), **Tarea
representativa** (qué objetivo concreto) y **Contexto de uso** (bajo qué
condiciones). Se seleccionan 3 de los 6 procesos críticos del caso MediSalud;
las fichas 2 y 3 se fundamentan con la distribución real de incidentes ya
clasificada en el Escenario 2 (`data/incidentes_2025_clasificados.csv`).

## Tabla 4.1 (ficha 1): Atención médica y registro de HCE

| Campo | Valor |
|---|---|
| Proceso | Atención médica y registro de HCE |
| Usuario primario | Médico tratante |
| Tarea representativa | Registrar una nota de evolución clínica completa de un paciente |
| Contexto de uso | Consulta externa, horario 10:00–12:00, red interna del hospital de Quito, carga alta de usuarios concurrentes |
| Atributos de Calidad en Uso relevantes | Tiempo de tarea (Eficiencia), completitud de la nota (Efectividad), percepción de fluidez (Satisfacción) |

## Ficha 2: Agendamiento de citas por el paciente

| Campo | Valor |
|---|---|
| Proceso | Agendamiento de citas por el paciente |
| Usuario primario | Paciente (portal web / app móvil) |
| Tarea representativa | Agendar una cita médica en máximo 3 pasos, sin errores de disponibilidad (alineado a RNF-02) |
| Contexto de uso | Autoservicio fuera de horario de atención presencial, conexión móvil variable según sede (Ambato/Manta vs. Quito/Guayaquil), picos de demanda tras liberación de nuevos cupos |
| Atributos de Calidad en Uso relevantes | Completitud de tarea (Efectividad), tiempo de espera del portal (Eficiencia), percepción de facilidad del formulario (Satisfacción), consistencia entre dispositivo web y móvil (Cobertura de Contexto) |

**Evidencia real que respalda esta ficha:** el módulo Portal Citas concentra
545 incidentes en 2025, de los cuales **271 son de Efectividad** (p. ej.
"usuario no logra agendar tras 3 intentos", "el portal muestra disponibilidad
para un horario ya ocupado") y **37 de Cobertura de Contexto** (p. ej. "botón
de confirmar cita no responde en dispositivos móviles"), confirmando que
Efectividad y Cobertura de Contexto son, en la práctica, los atributos más
críticos de esta tarea — no solo una hipótesis teórica.

## Ficha 3: Facturación de una consulta con seguro médico

| Campo | Valor |
|---|---|
| Proceso | Facturación y gestión de seguros/reaseguros |
| Usuario primario | Personal de Admisión y Facturación |
| Tarea representativa | Emitir una factura electrónica validando el convenio con la aseguradora, sin duplicados ni errores de cálculo (alineado a RNF-03: tasa de error de facturación < 1%) |
| Contexto de uso | Cierre de caja / cierre de turno, convenios distintos según aseguradora y sede, reintentos de pago con tarjeta |
| Atributos de Calidad en Uso relevantes | Libertad de riesgo (financiero), completitud de la transacción (Efectividad), tiempo de procesamiento del pago (Eficiencia) |

**Evidencia real que respalda esta ficha:** el módulo Facturación registra 425
incidentes, de los cuales **261 (61.4%)** se clasificaron como **Libertad de
Riesgo** (doble cobro por reintento, factura duplicada, error de cálculo de
copago, discrepancias entre monto facturado y detalle de servicios). Esto
justifica que, a diferencia de HCE o Portal Citas, en esta tarea el atributo
prioritario no sea Efectividad ni Eficiencia sino **Libertad de Riesgo**, en
línea directa con el objetivo de negocio de MediSalud de bajar los errores de
facturación duplicada a menos del 1%.

## Preguntas de Discusión

**1. ¿Por qué es incorrecto definir una tarea como "usar el sistema HIS" en
lugar de "registrar una nota de evolución clínica"?**

Porque ISO/IEC 25022 mide una razón *A/B* (resultado observado sobre base de
referencia) y ambas partes exigen un límite claro de inicio y fin de tarea:
sin ese límite no se puede determinar cuándo la tarea se completó, cuánto
tiempo tomó, ni qué contexto la rodeaba. "Usar el sistema HIS" mezcla
decenas de tareas heterogéneas (registrar HCE, facturar, dispensar,
agendar), cada una con su propio usuario, objetivo y contexto; cualquier
métrica calculada sobre esa definición sería un promedio sin significado
operativo, incapaz de guiar una mejora concreta. Es el mismo problema que ya
se evidenció en el Escenario 2: describir un incidente como "el sistema
falla" (ambiguo) en vez de una tarea concreta impide clasificarlo o medirlo.

**2. ¿Qué ocurre si se mide la eficiencia sin haber definido el contexto de
uso (por ejemplo, sin diferenciar hora pico de hora valle)?**

El indicador se diluye y oculta el problema real. Los 63 incidentes de "nota
de evolución tarda en guardarse" documentados en el Escenario 3 tienen un
promedio de 22.1s, pero ese promedio corresponde solo a los casos ya
reportados como incidente en horas pico; si se mezclara con el tiempo de
guardado en horas valle (probablemente muy por debajo de los 8s del RNF-01),
el promedio general podría parecer aceptable y ocultar que, específicamente
entre las 10:00 y las 12:00 en Quito, el sistema incumple sistemáticamente el
requisito. Medir eficiencia sin fijar el contexto (horario, sede, carga
concurrente) lleva a conclusiones erróneas y a priorizar mal los esfuerzos de
mejora.

## Conclusiones Parciales

Las tres fichas Usuario–Tarea–Contexto (HCE, Agendamiento de citas,
Facturación con seguro) quedan listas como insumo directo para el Escenario
5 (matriz de mapeo tarea–característica–prioridad) y el Escenario 6 (diseño
de métricas concretas). El ejercicio confirma que cada proceso crítico de
MediSalud tiene un perfil de riesgo distinto: HCE es predominantemente un
problema de Eficiencia/Efectividad, Portal Citas de Efectividad/Cobertura de
Contexto, y Facturación de Libertad de Riesgo — por lo que ninguna métrica
genérica de "calidad" serviría para los tres por igual.
