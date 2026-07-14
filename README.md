# medisalud-calidad-uso

Programa de medición de **Calidad en Uso** (ISO/IEC 25022) para el sistema
MediSalud HIS, desarrollado como parte del *Taller Guiado Integral —
Medición de la Calidad en Uso mediante ISO/IEC 25022* (asignatura
Aseguramiento de la Calidad del Software).

Caso de estudio: red hospitalaria ficticia **MediSalud Ecuador**. Todos los
análisis se basan en `incidentes_2025_iso_25022.csv`, un dataset de 3000
incidentes reportados durante 2025 en los distintos módulos del HIS (HCE,
Portal de Citas, Facturación, Telemedicina, Farmacia, Laboratorio,
Imagenología, Reportes Gerenciales, App Móvil).

## Estructura del repositorio

```
├── analisis.py                        # Escenario 1: analisis inicial del caso
├── scripts/
│   ├── clasificar_incidentes.py       # Escenario 2: clasificacion ISO/IEC 25022
│   ├── evidencia_calidad_en_uso.py    # Escenario 3: evidencia de calidad en uso (modulo HCE)
│   ├── generar_logs_hce.py            # Escenario 7: generador de logs sinteticos de HCE
│   ├── generar_encuesta_satisfaccion.py  # Escenario 7: generador de encuesta CSAT
│   ├── 01_validacion_datos.ipynb      # Escenario 7: validacion de datos (Jupyter)
│   ├── metricas_iso25022.py           # Escenario 8: modulo de calculo de metricas
│   └── exportar_reporte.py            # Escenario 8: exportacion a JSON
├── tests/
│   └── test_metricas.py               # Escenario 8: pruebas unitarias (pytest)
├── .github/workflows/
│   └── medicion_calidad.yml           # Escenario 8: CI semanal (GitHub Actions)
├── data/
│   ├── incidentes_2025_clasificados.csv   # dataset clasificado (salida de Escenario 2)
│   ├── logs_hce.csv                   # log sintetico de registro de HCE (Escenario 7)
│   └── encuesta_satisfaccion.csv      # encuesta CSAT simulada (Escenario 7)
├── dashboards/
│   └── indicadores.json               # reporte de metricas exportado (Escenario 8)
├── docs/
│   ├── analisis_inicial.md            # Escenario 1: Tabla 1.1
│   ├── clasificacion_incidentes.md    # Escenario 2: Tabla 2.2 y resumen cuantitativo
│   ├── modelo_square.md               # Escenario 3: mapa SQuaRE y Tabla 3.2
│   ├── atributos_calidad_uso.md       # Escenario 4: fichas Usuario-Tarea-Contexto (Tabla 4.1)
│   ├── mapeo_caracteristicas.md       # Escenario 5: Tabla 5.1
│   ├── diseno_metricas.md             # Escenario 6: catalogo de 5 metricas
│   ├── obtencion_datos.md             # Escenario 7: validacion de datos
│   └── automatizacion_medicion.md     # Escenario 8: pipeline y resultados
├── reportes/                          # (reservado para informe ejecutivo, Escenario 11)
├── incidentes_2025_iso_25022.csv      # dataset fuente (no versionado, ver .gitignore)
├── taller_iso_25022_parte1.pdf        # material del taller, escenarios 1-3 (no versionado)
└── taller_iso_25022_parte2_.pdf       # material del taller, escenarios 4+ (no versionado)
```

## Entorno

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install pandas numpy matplotlib plotly jupyter openpyxl
```

## Escenarios completados

### Escenario 1 — Introducción al Caso Empresarial

`analisis.py` → [docs/analisis_inicial.md](docs/analisis_inicial.md)

Primer reconocimiento del caso a partir del volumen de incidentes: los 3
procesos más críticos del negocio (HCE, Portal de Citas, Facturación) y los
usuarios más afectados (pacientes, médicos, enfermería), contrastando la
evidencia que hoy tiene MediSalud (incidentes crudos, uptime de servidores)
contra la que le falta (métricas normalizadas de Calidad en Uso).

### Escenario 2 — Comprensión de ISO/IEC 25022

`scripts/clasificar_incidentes.py` → [docs/clasificacion_incidentes.md](docs/clasificacion_incidentes.md), `data/incidentes_2025_clasificados.csv`

Clasificación de los 3000 incidentes en las 5 características de Calidad en
Uso mediante un motor de reglas, con justificación técnica por tipo de
incidente:

| Característica | Incidentes | % |
|---|---|---|
| Libertad de Riesgo | 1221 | 40.7% |
| Efectividad | 1197 | 39.9% |
| Eficiencia | 360 | 12.0% |
| Satisfacción | 138 | 4.6% |
| Cobertura de Contexto | 84 | 2.8% |

Hallazgo principal: incidentes que a primera vista parecen simples fallos
funcionales (p. ej. "no carga el historial de alergias", "datos de otro
paciente visibles") en realidad son riesgos clínicos o de privacidad, no
fallas de Efectividad — de ahí que Libertad de Riesgo sea la característica
más frecuente del dataset.

### Escenario 3 — Comprensión del Modelo SQuaRE

`scripts/evidencia_calidad_en_uso.py` → [docs/modelo_square.md](docs/modelo_square.md)

Ubica ISO/IEC 25022 dentro de la familia ISO/IEC 25000 (SQuaRE), con un mapa
conceptual (25000 → 25010 → 25022 → 25040) y diferencia los tres niveles de
calidad (interna, externa, en uso) aplicados a MediSalud HIS. Evidencia
cuantitativa del módulo HCE: el 100% de los 63 incidentes de "nota de
evolución tarda en guardarse" supera el umbral RNF-01 (8s), con un promedio
de 22.1s — mostrando que la calidad en uso puede fallar aunque el código
fuente sea internamente impecable.

### Escenario 4 — Identificación de Atributos de Calidad en Uso

[docs/atributos_calidad_uso.md](docs/atributos_calidad_uso.md)

Tres fichas Usuario–Tarea–Contexto (modelo exigido por ISO/IEC 25022 antes de
diseñar métricas): Atención médica/HCE, Agendamiento de citas por el
paciente y Facturación de una consulta con seguro médico. Las dos últimas se
fundamentan con la distribución real de incidentes del Escenario 2: Portal
Citas concentra su problema en Efectividad (271 de 545 incidentes) y
Cobertura de Contexto (37), mientras que Facturación concentra el 61.4% de
sus incidentes (261 de 425) en Libertad de Riesgo (doble cobro, facturas
duplicadas, errores de cálculo) — evidenciando que cada proceso crítico
requiere priorizar atributos distintos, no una métrica genérica de "calidad".

### Escenario 5 — Mapeo de Características de Calidad

[docs/mapeo_caracteristicas.md](docs/mapeo_caracteristicas.md)

Matriz de mapeo tarea–característica–prioridad (Tabla 5.1) para las 6 tareas
correspondientes a los 6 procesos críticos de MediSalud, priorizadas por
impacto en el negocio y frecuencia real de incidentes. Resultado: 2 tareas de
prioridad 1 (Registrar nota de evolución clínica, Agendar cita en el portal)
y 3 de prioridad 2 (Facturar consulta con seguro, Dispensar medicamento,
Completar teleconsulta), que serán las desarrolladas en profundidad en el
Escenario 6. La característica dominante de cada tarea se leyó directamente
de los datos reales en vez de asumirse: Farmacia (74.4%) y Facturación
(61.4%) quedaron dominadas por Libertad de Riesgo, no por Efectividad.

### Escenario 6 — Diseño de Métricas

[docs/diseno_metricas.md](docs/diseno_metricas.md)

Catálogo de 5 métricas formales de Calidad en Uso (una por característica),
diseñadas sobre las tareas priorizadas del Escenario 5, con fórmula,
variables, unidad, rango deseado (derivado de los RNF-01/02/03 del caso),
fuente de datos, frecuencia y responsable: Tasa de éxito de agendamiento
(Efectividad), Tiempo de registro de HCE (Eficiencia, ≤8s por RNF-01), Índice
de satisfacción de teleconsulta (Satisfacción), Tasa de errores de
facturación (Libertad de Riesgo, <1% por RNF-03) y Consistencia entre sedes
del Portal de Citas (Cobertura de Contexto). Se identifica que la métrica de
Libertad de Riesgo aún carece de denominador (total de facturas emitidas),
dato que deberá aportar el Escenario 7.

### Escenario 7 — Obtención de Datos

`scripts/generar_logs_hce.py`, `scripts/generar_encuesta_satisfaccion.py`,
`scripts/01_validacion_datos.ipynb` → [docs/obtencion_datos.md](docs/obtencion_datos.md)

Genera y valida las dos fuentes de datos base (`data/logs_hce.csv`, 3150
eventos; `data/encuesta_satisfaccion.csv`, 150 respuestas) que alimentarán el
cálculo automatizado de métricas en el Escenario 8. Validación sin nulos
inesperados, sin duplicados y con rangos lógicos correctos. Hallazgo clave:
en horas pico (10:00–12:00) el tiempo de registro de HCE simulado sube a
10.45s de media y el 84.1% de esos registros ya incumple el umbral de 8s del
RNF-01, replicando con datos de producción simulados el mismo patrón
detectado con incidentes reales en el Escenario 3.

### Escenario 8 — Automatización de la Medición

`scripts/metricas_iso25022.py`, `scripts/exportar_reporte.py`,
`tests/test_metricas.py`, `.github/workflows/medicion_calidad.yml` →
[docs/automatizacion_medicion.md](docs/automatizacion_medicion.md)

Pipeline Python que calcula automáticamente las 5 métricas del Escenario 6 y
las exporta a `dashboards/indicadores.json`, con pruebas unitarias (pytest) y
un workflow de GitHub Actions que lo ejecuta cada lunes. Resultado real:
Efectividad, Cobertura de Contexto y Libertad de Riesgo cumplen; Satisfacción
no cumple (0.72 vs. umbral 0.80). El hallazgo más importante: la Eficiencia
agregada del día completo "cumple" (7.43s), pero desagregada por hora pico
"no cumple" (**10.47s, con 84.1% de incumplimiento** entre 10:00–12:00) — la
automatización expuso en la práctica el riesgo, ya anticipado en el
Escenario 4, de medir sin fijar el contexto de uso.

## Próximos escenarios

9. Construcción de indicadores (KPI)
10. Interpretación de resultados
11. Presentación ejecutiva para directivos
12. Plan de mejora continua
