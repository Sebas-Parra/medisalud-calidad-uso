# Diseño de Métricas ISO/IEC 25022 (Escenario 6)

Catálogo de 5 métricas formales (una por característica de Calidad en Uso),
diseñadas sobre las tareas de prioridad 1 y 2 de la matriz del Escenario 5
(`docs/mapeo_caracteristicas.md`). Cada ficha sigue la estructura exigida por
el taller: nombre, característica, propósito, fórmula, variables, unidad,
rango deseado, fuente de datos, frecuencia de medición y responsable.

## Métrica 1 — Efectividad

| Campo | Valor |
|---|---|
| Nombre | Tasa de éxito de agendamiento |
| Característica | Efectividad |
| Propósito | Medir si el paciente logra completar el agendamiento de una cita a través del portal/app, sin errores de disponibilidad |
| Fórmula | X = Citas agendadas con éxito / Intentos de agendamiento |
| Variables | *Citas agendadas con éxito*: agendamientos confirmados sin error; *Intentos de agendamiento*: total de sesiones donde el paciente inició el flujo de agendamiento |
| Unidad | Porcentaje (%) |
| Rango deseado | ≥ 95% (alineado al objetivo de negocio de reducir la fricción del portal; ver RNF-02: máximo 3 pasos, sin errores de disponibilidad) |
| Fuente de datos | Logs de aplicación del Portal de Citas (evento de éxito/fracaso por sesión) |
| Frecuencia de medición | Diaria (agregada semanalmente para el dashboard) |
| Responsable | Gerencia de Calidad y Aseguramiento, con datos provistos por Gerencia de TI |

**Evidencia de referencia:** de los 545 incidentes del módulo Portal Citas,
271 (49.7%) ya se clasificaron como Efectividad en el Escenario 2 (p. ej.
"usuario no logra agendar tras 3 intentos", "el portal muestra
disponibilidad para un horario ya ocupado"), lo que confirma que esta es la
característica más urgente a instrumentar para esta tarea.

## Métrica 2 — Eficiencia

| Campo | Valor |
|---|---|
| Nombre | Tiempo de tarea — registro de nota de evolución clínica |
| Característica | Eficiencia |
| Propósito | Medir cuánto tarda un médico en registrar una nota de evolución clínica completa durante consulta externa |
| Fórmula | X = (Σ tᵢ) / n, donde tᵢ es el tiempo (segundos) que tarda el registro i-ésimo y n el número total de registros observados |
| Variables | tᵢ: tiempo en segundos entre apertura del formulario y confirmación del guardado; n: número de notas registradas en el periodo |
| Unidad | Segundos (s) |
| Rango deseado | X ≤ 8s en el 90% de los casos (RNF-01 del caso de estudio) |
| Fuente de datos | Logs de la aplicación web/HIS (marca de tiempo al abrir el formulario y al confirmar el guardado) |
| Frecuencia de medición | Diaria, con corte adicional por franja horaria (pico 10:00–12:00 vs. resto) |
| Responsable | Gerencia de TI (instrumentación de logs), Gerencia de Calidad (análisis) |

**Evidencia de referencia:** ya calculada en el Escenario 3
(`scripts/evidencia_calidad_en_uso.py`): los 63 incidentes reales de "nota de
evolución tarda en guardarse" promedian **22.1s**, con el **100%** superando
el umbral de 8s. Esta métrica formaliza esa evidencia como indicador
permanente en vez de un hallazgo puntual.

## Métrica 3 — Satisfacción

| Campo | Valor |
|---|---|
| Nombre | Índice de satisfacción de la teleconsulta (CSAT) |
| Característica | Satisfacción |
| Propósito | Medir la percepción de comodidad y confianza del paciente/médico tras completar una teleconsulta |
| Fórmula | X = (Σ Puntajes CSAT) / N. de encuestados |
| Variables | Puntaje CSAT: respuesta de 1 (muy insatisfecho) a 5 (muy satisfecho) en encuesta post-consulta; N. de encuestados: número de respuestas recibidas en el periodo |
| Unidad | Puntaje promedio en escala 1–5 |
| Rango deseado | X ≥ 4.0 / 5 |
| Fuente de datos | Encuesta de satisfacción (CSAT) enviada automáticamente al finalizar la videollamada (`data/encuesta_satisfaccion.csv`, a generar en el Escenario 7) |
| Frecuencia de medición | Semanal |
| Responsable | Dirección Médica (seguimiento de experiencia clínica), Gerencia de Calidad (consolidación) |

**Evidencia de referencia:** 66 de los 320 incidentes de Telemedicina (20.6%)
ya se clasificaron como Satisfacción en el Escenario 2 (audio desincronizado,
calidad de video baja pese a buena conexión), justificando medir esta
característica de forma explícita y no solo la finalización técnica de la
llamada (objetivo de negocio: 95% de tasa de finalización de teleconsultas).

## Métrica 4 — Libertad de Riesgo

| Campo | Valor |
|---|---|
| Nombre | Tasa de errores de facturación |
| Característica | Libertad de Riesgo |
| Propósito | Medir la proporción de facturas emitidas con error financiero (duplicidad, doble cobro, cálculo incorrecto de copago) que exponen a MediSalud o al paciente a un riesgo económico |
| Fórmula | X = Facturas erróneas / Facturas emitidas |
| Variables | Facturas erróneas: facturas con doble cobro, duplicidad, o discrepancia de monto reportadas o detectadas por conciliación; Facturas emitidas: total de facturas generadas en el periodo |
| Unidad | Porcentaje (%) |
| Rango deseado | X < 1% (RNF-03: la tasa de errores de facturación no debe superar el 1% de las transacciones mensuales) |
| Fuente de datos | Sistema de facturación (conteo total de transacciones) cruzado con registros de incidentes de facturación |
| Frecuencia de medición | Mensual, con corte de cierre de caja |
| Responsable | Departamento de Admisión y Facturación, con auditoría de Gerencia de Calidad |

**Evidencia de referencia:** el 61.4% de los incidentes de Facturación (261
de 425) ya se clasificaron como Libertad de Riesgo en el Escenario 2. Nótese
que el dataset actual solo aporta el **numerador** (facturas con incidente
reportado); todavía falta el **denominador** (total de facturas emitidas en
el periodo), que es exactamente el dato que el Escenario 7 (Obtención de
Datos) deberá generar/obtener para poder calcular esta métrica de forma
completa.

## Métrica 5 — Cobertura de Contexto

| Campo | Valor |
|---|---|
| Nombre | Consistencia del tiempo de agendamiento entre sedes |
| Característica | Cobertura de Contexto |
| Propósito | Verificar que el Portal de Citas ofrezca una experiencia equivalente en todas las sedes de la red, no solo en las de mayor infraestructura |
| Fórmula | X = 1 − ( \|Métrica sede A − Métrica sede B\| / Métrica sede A ) |
| Variables | Métrica sede A / sede B: tiempo de espera promedio del portal (segundos) en la sede con mejor y peor desempeño del periodo |
| Unidad | Índice adimensional (0 a 1); se reporta también como % de similitud |
| Rango deseado | X ≥ 0.85 (diferencia entre sedes ≤ 15%) |
| Fuente de datos | Logs del Portal de Citas con metadato de sede, cruzados con la Métrica 1 (Efectividad) por sede |
| Frecuencia de medición | Mensual |
| Responsable | Gerencia de TI (instrumentación por sede), Gerencia de Calidad (interpretación) |

**Evidencia de referencia:** 37 de los 545 incidentes de Portal Citas (6.8%)
ya se clasificaron como Cobertura de Contexto en el Escenario 2 (fallos
específicos de dispositivo móvil/tablet). Dado que MediSalud opera en 5
ciudades con infraestructura desigual (Quito concentra 1035 incidentes
totales frente a los 324 de Manta), esta métrica es la única forma de saber
si la experiencia del paciente en Manta es comparable a la de Quito, en
lugar de asumirlo.

## Preguntas de Discusión

**1. ¿Por qué es importante fijar de antemano el rango deseado y no solo
calcular el valor de la métrica?**

Porque un número aislado no tiene significado operativo: 22.1 segundos no es
"bueno" ni "malo" hasta que se compara contra un umbral definido de antemano
(RNF-01: 8 segundos). Fijar el rango antes de medir evita el sesgo de
ajustar la interpretación después de ver el resultado ("total, no está tan
mal"), y es indispensable para automatizar alertas en el Escenario 8: sin un
umbral explícito, ningún pipeline puede decidir cuándo un valor es una
desviación que amerita acción.

**2. ¿Qué diferencia existe entre una métrica de Eficiencia y un simple
cronómetro de tiempo de respuesta del servidor?**

El cronómetro de servidor mide solo la latencia técnica de una petición
(por ejemplo, 200ms de respuesta HTTP del backend de HCE), sin considerar si
el usuario completó su tarea ni cuánto le costó realmente. La métrica de
Eficiencia de ISO/IEC 25022 mide el tiempo de la **tarea completa desde la
perspectiva del usuario** (desde que abre el formulario hasta que confirma
el guardado), incluyendo tiempo de lectura, reintentos por errores de
validación y esperas de interfaz — por eso el registro de una nota puede
tardar 22.1 segundos en producción aunque el servidor responda en
milisegundos. Es la diferencia entre medir el sistema y medir la experiencia
real del usuario, que es precisamente el objeto de la Calidad en Uso.

## Conclusiones Parciales

Las 5 métricas documentadas traducen la matriz priorizada del Escenario 5 en
fórmulas concretas, reproducibles y con umbrales explícitos derivados
directamente de los requerimientos no funcionales del caso (RNF-01, RNF-02,
RNF-03). Dos de ellas (Eficiencia y Libertad de Riesgo) ya cuentan con
evidencia real parcial de escenarios anteriores; las demás quedan listas
para ser calculadas de punta a punta una vez que el Escenario 7 aporte las
fuentes de datos que aún faltan (encuestas de satisfacción, conteo total de
transacciones y agendamientos, no solo los incidentes).
