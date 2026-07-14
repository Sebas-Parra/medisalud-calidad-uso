# Automatización de la Medición (Escenario 8)

Pipeline en Python que calcula automáticamente las métricas de Calidad en Uso
diseñadas en el Escenario 6, a partir de los datos validados en el Escenario
7, y las exporta en JSON para alimentar los dashboards del Escenario 9.

```
Datos crudos (CSV/logs) → Limpieza (Pandas) → Cálculo de métricas ISO 25022 → dashboards/indicadores.json
```

## Componentes

| Archivo | Función |
|---|---|
| `scripts/metricas_iso25022.py` | Módulo con una función por métrica (`metrica_efectividad`, `metrica_eficiencia`, `metrica_eficiencia_por_sede`, `metrica_eficiencia_hora_pico`, `metrica_cobertura_contexto`, `metrica_satisfaccion`, `metrica_libertad_riesgo`) y `generar_reporte()` que las orquesta |
| `scripts/exportar_reporte.py` | Ejecuta `generar_reporte()` y exporta el resultado a `dashboards/indicadores.json` |
| `tests/test_metricas.py` | Pruebas unitarias con pytest sobre datos controlados (no datos reales), recomendadas por el taller |
| `.github/workflows/medicion_calidad.yml` | Workflow de GitHub Actions que ejecuta el pipeline cada lunes a las 06:00 UTC (o manualmente vía `workflow_dispatch`) y publica `indicadores.json` como artefacto |

Nota de diseño: el módulo del libro calcula Efectividad y Eficiencia sobre
`logs_hce.csv`, mientras que el Escenario 6 había priorizado Efectividad
para la tarea de Agendamiento de citas (Portal Citas). Se mantuvo la
implementación sobre HCE porque es el único dataset del Escenario 7 con una
marca explícita de finalización de tarea (`completada`); medir Efectividad
del agendamiento requeriría generar un log análogo del Portal de Citas,
pendiente para una siguiente iteración del programa de medición.

## Resultado de la ejecución (`python scripts/metricas_iso25022.py`)

| Métrica | Valor | Umbral | Estado |
|---|---|---|---|
| Completitud de registro de HCE (Efectividad) | 0.9651 | ≥ 0.95 | **CUMPLE** |
| Tiempo promedio de registro de HCE (Eficiencia, todo el día) | 7.43s | ≤ 8s | **CUMPLE** |
| Tiempo promedio de registro de HCE en hora pico 10–12h (Eficiencia) | 10.47s | ≤ 8s | **NO CUMPLE** |
| Consistencia entre sedes (Cobertura de Contexto) | 0.984 | ≥ 0.85 | **CUMPLE** |
| Índice de satisfacción CSAT normalizado (Satisfacción) | 0.7173 (≈3.59/5) | ≥ 0.80 | **NO CUMPLE** |
| Tasa de errores de facturación (Libertad de Riesgo) | 0.29% | ≤ 1% | **CUMPLE** |

**Hallazgo más importante del escenario:** la métrica agregada de Eficiencia
del día completo (7.43s) reporta "CUMPLE", ocultando que específicamente en
horas pico (10:00–12:00) el sistema incumple el umbral RNF-01 con un
promedio de **10.47s** y que el **84.1%** de los registros de esa franja ya
lo superan. Esto es exactamente la advertencia que se anticipó en el
Escenario 4 (Pregunta 2: "qué ocurre si se mide eficiencia sin diferenciar
hora pico de hora valle") y confirma por qué `metrica_eficiencia_hora_pico()`
se añadió como desagregación obligatoria y no opcional del pipeline: un
reporte que solo mostrara el promedio general habría comunicado a Dirección
General que el problema de lentitud de HCE ya está resuelto, cuando en
realidad persiste justo en el horario más crítico.

La métrica de Satisfacción tampoco cumple (0.72 frente al umbral de 0.80),
consistente con el promedio CSAT de 3.59/5 ya reportado en el Escenario 7.

## Preguntas de Discusión

**1. ¿Qué ventajas ofrece programar la medición en GitHub Actions frente a
ejecutarla manualmente cada trimestre?**

Reproducibilidad (mismo entorno y versión de Python en cada corrida, sin
depender de la máquina de un analista en particular), trazabilidad (cada
ejecución queda registrada con su artefacto `indicadores.json` descargable),
y detección temprana: con una corrida semanal automática, una degradación
como la de horas pico se detectaría en días, no al cierre de un trimestre.
Además desacopla el programa de medición de la disponibilidad de una
persona específica del equipo de calidad — el objetivo de negocio #4 del
caso ("reportes trimestrales a Dirección General") se cumple mejor con
datos acumulados semana a semana que con un cálculo manual de última hora.

**2. ¿Qué riesgo existe si el umbral (`UMBRAL_TIEMPO_TAREA`) queda
"hardcodeado" en el script en lugar de estar en un archivo de configuración
externo?**

Cambiar un umbral de negocio (por ejemplo, si tras cumplir el objetivo de
reducir 30% el tiempo de HCE el nuevo umbral aceptado pasara de 8s a 6s)
exigiría modificar y re-desplegar código fuente, mezclando una decisión de
negocio con un cambio de ingeniería en el control de versiones — y quien
apruebe ese cambio (Gerencia de Calidad) normalmente no es quien tiene
permisos para modificar el repositorio de código. Además, el mismo valor
puede quedar duplicado en varios lugares sin sincronizarse: en este propio
repositorio, `UMBRAL_TIEMPO_TAREA = 8.0` vive en
`scripts/metricas_iso25022.py`, pero el mismo umbral también está descrito
en prosa en `docs/diseno_metricas.md`; si el umbral cambiara solo en el
código (o solo en la documentación), ambas fuentes quedarían inconsistentes
sin que nada lo detecte automáticamente. Externalizar los umbrales en un
archivo de configuración (YAML/JSON) versionado aparte resolvería ese riesgo.

## Conclusiones Parciales

El programa de medición de Calidad en Uso queda completamente automatizado:
de fórmulas normativas en un documento (Escenario 6) a un pipeline
ejecutable, con pruebas unitarias y listo para integrarse en un flujo de
integración continua semanal. El resultado más valioso no es la
automatización en sí, sino que esta automatización **expuso un problema que
el promedio agregado ocultaba** (la degradación en horas pico), demostrando
en la práctica por qué ISO/IEC 25022 exige definir el contexto de uso antes
de medir Eficiencia.
