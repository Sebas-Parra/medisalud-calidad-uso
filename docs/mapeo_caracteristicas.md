# Mapeo de Características de Calidad (Escenario 5)

Medir las 5 características de ISO/IEC 25022 para todas las tareas posibles
de MediSalud no es viable ni deseable: consume recursos y genera ruido. Se
prioriza según **impacto en el negocio** y **frecuencia de la tarea**,
seleccionando para medición prioritaria las combinaciones alto–alto y
alto–medio, siguiendo la matriz de priorización del taller.

Se cubren las 6 tareas correspondientes a los 6 procesos críticos del caso
MediSalud (capítulo de Caso de Estudio), en vez de limitarse a las 3 fichas
del Escenario 4, para que la matriz sirva de insumo completo al Escenario 6.
El Impacto se basa en los objetivos de negocio y riesgos identificados en el
caso; la Frecuencia y las Características ISO/IEC 25022 relevantes se
fundamentan con el volumen y la clasificación real de incidentes por módulo
obtenidos en el Escenario 2 (`data/incidentes_2025_clasificados.csv`).

## Tabla 5.1: Matriz de mapeo tarea–característica–prioridad

| Tarea | Proceso crítico | Impacto | Frecuencia | Características ISO/IEC 25022 | Prioridad |
|---|---|---|---|---|---|
| Registrar nota de evolución clínica | Atención médica y registro de HCE | Alto | Alta (769 incidentes, HCE es el módulo con más volumen) | Eficiencia, Efectividad | **1** |
| Agendar cita en el portal | Agendamiento y admisión de pacientes | Alto | Alta (545 incidentes; 38.000+ pacientes activos) | Efectividad, Satisfacción | **1** |
| Facturar consulta con seguro médico | Facturación y gestión de seguros/reaseguros | Alto | Media (425 incidentes) | Libertad de Riesgo (261/425 = 61.4%), Efectividad | **2** |
| Dispensar medicamento prescrito | Prescripción y dispensación de medicamentos | Alto | Media (258 incidentes) | Libertad de Riesgo (192/258 = 74.4%) | **2** |
| Completar una teleconsulta | Telemedicina y seguimiento remoto | Medio | Media (320 incidentes; servicio en expansión desde 2022) | Efectividad, Satisfacción (66/320 = 20.6%) | **2** |
| Generar reporte gerencial mensual | Generación de reportes gerenciales | Medio | Baja (88 incidentes; el módulo con menor volumen, 45 usuarios de Gerencia) | Efectividad | 3 |

Nota metodológica: la característica dominante de cada tarea no se asumió a
priori, se leyó directamente de la clasificación real del Escenario 2. Por
ejemplo, Farmacia y Facturación quedaron dominadas por Libertad de Riesgo
(no por Efectividad, el atributo que intuitivamente se asociaría a un
"error del sistema"), y Telemedicina mostró Satisfacción como segunda
característica relevante en lugar de Cobertura de Contexto, porque en los
datos reales no se registraron incidentes de Telemedicina asociados a un
contexto de uso específico (0 casos).

## Preguntas de Discusión

**1. ¿Qué riesgo corre una organización que intenta medir absolutamente todo
desde el primer día de un programa de calidad en uso?**

Diluye el esfuerzo del equipo de calidad en tareas de bajo impacto (como
"Generar reporte gerencial mensual", con solo 88 incidentes y 45 usuarios),
retrasando la instrumentación de las tareas que sí concentran el riesgo del
negocio (HCE, Portal de Citas, Facturación, Telemedicina y Farmacia —las
5 tareas de prioridad 1 y 2— que juntas concentran 2317 de los 3000
incidentes, el 77.2%). Además, un programa que reporta
decenas de métricas simultáneas a Dirección General pierde credibilidad y
foco frente a uno que reporta pocas métricas bien elegidas y accionables,
exactamente el objetivo de negocio #4 del caso ("reportes trimestrales a
Dirección General").

**2. ¿Por qué "Consultar historial de resultados" tiene menor prioridad pese
a tener alta frecuencia?**

Porque la matriz de priorización combina impacto **y** frecuencia: una tarea
muy frecuente pero de bajo impacto (por ejemplo, una consulta de solo
lectura, sin riesgo clínico ni financiero directo, y sin bloquear ningún
objetivo de negocio) no justifica el mismo esfuerzo de medición que una
tarea de alto impacto. Frecuencia alta sin impacto alto genera mucho
volumen de datos pero poco valor de decisión; es la razón por la que el
taller recomienda priorizar alto–alto y alto–medio, y dejar alto–bajo o
bajo–alto para una segunda fase del programa de medición.

## Conclusiones Parciales

La matriz resultante deja 2 tareas de prioridad 1 (Registrar nota de
evolución clínica, Agendar cita en el portal) y 3 de prioridad 2 (Facturar
consulta con seguro, Dispensar medicamento, Completar teleconsulta), que en
conjunto serán las que se desarrollen en profundidad en el Escenario 6 al
diseñar métricas concretas. La tarea de reportes gerenciales queda en
prioridad 3, no por ser irrelevante, sino porque su bajo volumen e impacto
relativo no la hace todavía indispensable para el primer ciclo del programa
de medición de Calidad en Uso.
