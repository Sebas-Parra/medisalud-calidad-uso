# Analisis Inicial del Caso MediSalud (Escenario 1)

Fuente de datos: `incidentes_2025_iso_25022.csv` (3000 incidentes registrados en 2025).

## Tabla 1.1: Matriz de analisis inicial del caso MediSalud

| Pregunta guia | Respuesta del grupo |
|---|---|
| ¿Cuales son los 3 procesos mas criticos del negocio? | Segun el volumen de incidentes reportados en 2025 (3000 registros), los 3 procesos con mas incidentes son: 1) **Atencion medica y registro de historia clinica** (modulo `HCE`: 769 incidentes, 25.6% del total); 2) **Agendamiento y admision de pacientes** (modulo `Portal Citas`: 545 incidentes, 18.2% del total); y 3) **Facturacion y gestion de seguros/reaseguros** (modulo `Facturacion`: 425 incidentes, 14.2% del total). Coinciden con los procesos de mayor riesgo clinico, reputacional y financiero descritos en el caso de estudio. |
| ¿Que usuarios se ven mas afectados por la problematica actual? | Los usuarios mas afectados son **Paciente** (919 incidentes, 30.6%), seguidos de **Medico** (689 incidentes, 23.0%) y **Enfermeria** (677 incidentes, 22.6%). Esto confirma que la problematica no solo es percibida por TI, sino que impacta directamente la experiencia de pacientes y personal clinico. |
| ¿Que evidencia tiene hoy MediSalud sobre la calidad de su software? | Hoy MediSalud cuenta con: (a) disponibilidad/uptime de servidores reportado por TI, y (b) un registro crudo de 3000 incidentes reportados durante 2025 (`incidentes_2025_iso_25022.csv`), sin clasificar segun las caracteristicas de ISO/IEC 25022 ni convertido aun en metricas o indicadores. Es evidencia reactiva (quejas), no medicion proactiva. |
| ¿Que evidencia le falta? | Falta evidencia estructurada de Calidad en Uso: metricas normalizadas de efectividad (tasa de tareas completadas), eficiencia (tiempos reales de tarea, ej. registro de HCE), satisfaccion (encuestas), libertad de riesgo (incidentes de seguridad/datos clinicos, ej. el caso de datos de otro paciente visibles) y cobertura de contexto (comparacion entre sedes). Tambien falta clasificar este dataset segun las 5 caracteristicas de ISO/IEC 25022 (Escenario 2). |

## Datos de respaldo

### Incidentes por modulo

| Modulo | Incidentes | % del total |
|---|---|---|
| HCE | 769 | 25.6% |
| Portal Citas | 545 | 18.2% |
| Facturacion | 425 | 14.2% |
| Telemedicina | 320 | 10.7% |
| App Movil | 278 | 9.3% |
| Farmacia | 258 | 8.6% |
| Laboratorio | 166 | 5.5% |
| Imagenologia | 151 | 5.0% |
| Reportes Gerenciales | 88 | 2.9% |

### Incidentes por rol de usuario

| Rol | Incidentes | % del total |
|---|---|---|
| Paciente | 919 | 30.6% |
| Medico | 689 | 23.0% |
| Enfermeria | 677 | 22.6% |
| Admision | 490 | 16.3% |
| Farmacia | 137 | 4.6% |
| Gerencia | 88 | 2.9% |

### Incidentes por sede

| Sede | Incidentes | % del total |
|---|---|---|
| Quito | 1035 | 34.5% |
| Guayaquil | 791 | 26.4% |
| Cuenca | 464 | 15.5% |
| Ambato | 386 | 12.9% |
| Manta | 324 | 10.8% |
