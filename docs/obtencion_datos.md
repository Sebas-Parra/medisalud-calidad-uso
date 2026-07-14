# Obtención de Datos (Escenario 7)

Genera y valida las dos fuentes de datos base necesarias para calcular las 5
métricas diseñadas en el Escenario 6, antes de automatizar nada (Escenario
8). Siguiendo la disciplina del taller: **calidad del dato antes que calidad
del indicador**.

## Fuentes generadas

| Archivo | Script generador | Filas | Alimenta la métrica |
|---|---|---|---|
| `data/logs_hce.csv` | `scripts/generar_logs_hce.py` | 3150 eventos | Métrica 2 (Eficiencia — tiempo de registro de HCE) |
| `data/encuesta_satisfaccion.csv` | `scripts/generar_encuesta_satisfaccion.py` | 150 respuestas | Métrica 3 (Satisfacción — CSAT de teleconsulta, como proxy general de satisfacción) |

Ambos generadores usan semilla fija (`random.seed`) para que los datos sean
reproducibles entre ejecuciones, y simulan de forma consistente los
hallazgos ya documentados en escenarios previos: `logs_hce.csv` degrada el
tiempo de registro en horas pico (10:00–12:00), y `encuesta_satisfaccion.csv`
asigna puntajes más bajos al rol Paciente, coherente con que Portal Citas y
Telemedicina concentran la mayoría de los incidentes de Satisfacción del
Escenario 2.

## Validación (`scripts/01_validacion_datos.ipynb`)

Notebook ejecutado con `jupyter nbconvert --execute`, resultados:

### `logs_hce.csv`

- **Nulos:** 0 en todas las columnas.
- **Rangos lógicos** (tiempos negativos o mayores a 120s): 0 registros fuera
  de rango.
- **Duplicados** (por `evento_id`): 0.
- **Resumen de `tiempo_segundos`:** media 7.43s, desviación 2.45s, mínimo
  1.5s, máximo 17.31s (n = 3150).
- **Corte por horario:** en horas pico (10:00–12:00, n = 749) la media sube a
  **10.45s**, y el **84.1%** de esos registros ya supera el umbral de 8s del
  RNF-01, frente a 6.48s de media en el resto del día. Esto confirma con
  datos de producción simulados el mismo patrón detectado en el Escenario 3
  con los incidentes reales.

### `encuesta_satisfaccion.csv`

- **Nulos:** 0 en `respuesta_id`, `sede`, `rol`, `puntaje_csat`; 54 nulos en
  `comentario`. **No es un defecto de calidad del dato:** el generador solo
  produce comentario cuando el puntaje es ≥4 (positivo) o ≤2 (negativo); un
  puntaje neutro (3) queda intencionalmente sin comentario, replicando el
  comportamiento típico de una encuesta CSAT real donde el campo de texto es
  opcional.
- **Rango lógico** (`puntaje_csat` entre 1 y 5): 0 registros fuera de rango.
- **Duplicados** (por `respuesta_id`): 0.
- **Resumen de `puntaje_csat`:** media 3.59/5 (n = 150), por debajo del rango
  deseado de la Métrica 3 (≥4.0), consistente con la brecha de satisfacción
  ya señalada en escenarios anteriores.

## Preguntas de Discusión

**1. ¿Qué consecuencias tendría calcular la métrica de tiempo de tarea sin
antes eliminar los valores atípicos (*outliers*) causados por sesiones
abandonadas?**

El promedio dejaría de representar la experiencia real de un registro
exitoso. Una sesión abandonada (el médico abre el formulario y no vuelve
hasta 40 minutos después, o el sistema registra un tiempo casi nulo por un
cierre abrupto) no es una medición válida de Eficiencia porque la tarea
nunca se completó — es, en realidad, un incidente de Efectividad. Si esos
valores no se filtran antes de promediar, un solo caso extremo puede inflar
o deflactar artificialmente la media y ocultar la señal real (por ejemplo,
la degradación genuina en horas pico que sí detectamos: 10.45s vs 6.48s).
Es exactamente la razón por la que el Paso 2 de este escenario valida
rangos lógicos (0–120s) antes de cualquier cálculo, y por la que la métrica
de Eficiencia del Escenario 6 debe calcularse **solo sobre los registros con
`completada = 1`**, no sobre el total de intentos.

**2. ¿Por qué la fuente de datos de Satisfacción (encuestas) es
cualitativamente distinta a la de Eficiencia (logs)? ¿Qué implica esto para
su frecuencia de recolección?**

Los logs de Eficiencia son un subproducto automático de cada transacción: el
sistema ya registra el timestamp de apertura y guardado sin que el usuario
haga nada adicional, por lo que pueden recolectarse de forma continua y
exhaustiva (los 3150 eventos de 5 días corresponden al 100% de los registros
de HCE simulados en ese periodo). La Satisfacción, en cambio, depende de que
el usuario decida y tenga tiempo de responder una encuesta — es una fuente
activa, no pasiva, sujeta a fatiga de encuesta y a sesgo de quién responde
(solo 150 respuestas frente a miles de interacciones reales). Esto implica
que Satisfacción no debe medirse con la misma cadencia diaria que Eficiencia:
conviene recolectarla semanal o mensualmente, sobre una muestra
estadísticamente representativa, en lugar de intentar encuestar cada
interacción, algo que además degradaría la propia satisfacción del usuario.

## Conclusiones Parciales

Las dos fuentes de datos quedan generadas, validadas y documentadas,
cerrando la brecha que el Escenario 6 había dejado abierta para la métrica
de Eficiencia y avanzando en la de Satisfacción. La métrica de Libertad de
Riesgo (tasa de errores de facturación) sigue pendiente de un dataset
análogo de transacciones de facturación, que se recomienda generar con el
mismo patrón de estos dos scripts antes de avanzar al Escenario 8
(automatización).
