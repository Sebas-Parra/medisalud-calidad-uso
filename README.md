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
│   └── evidencia_calidad_en_uso.py    # Escenario 3: evidencia de calidad en uso (modulo HCE)
├── data/
│   └── incidentes_2025_clasificados.csv   # dataset clasificado (salida de Escenario 2)
├── docs/
│   ├── analisis_inicial.md            # Escenario 1: Tabla 1.1
│   ├── clasificacion_incidentes.md    # Escenario 2: Tabla 2.2 y resumen cuantitativo
│   └── modelo_square.md               # Escenario 3: mapa SQuaRE y Tabla 3.2
├── dashboards/                        # (reservado para indicadores/KPI, Escenario 9)
├── reportes/                          # (reservado para informe ejecutivo, Escenario 11)
├── incidentes_2025_iso_25022.csv      # dataset fuente (no versionado, ver .gitignore)
└── taller_iso_25022_parte1.pdf        # material del taller (no versionado, ver .gitignore)
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

## Próximos escenarios

4. Identificación de atributos de Calidad en Uso
5. Mapeo de características de calidad
6. Diseño de métricas
7. Obtención de datos
8. Automatización de la medición
9. Construcción de indicadores (KPI)
10. Interpretación de resultados
11. Presentación ejecutiva para directivos
12. Plan de mejora continua
