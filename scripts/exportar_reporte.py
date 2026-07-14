"""
Escenario 8 - Paso 2: exporta el reporte de metricas de Calidad en Uso
a JSON, listo para ser consumido por los dashboards del Escenario 9.
"""
import json

from metricas_iso25022 import generar_reporte

reporte, eficiencia_sede = generar_reporte()

salida = {
    "metricas": reporte,
    "eficiencia_por_sede": eficiencia_sede.to_dict(orient="records"),
}

def _a_nativo(valor):
    """Convierte tipos numpy (bool_, float64, int64) a tipos nativos serializables en JSON."""
    if hasattr(valor, "item"):
        return valor.item()
    raise TypeError(f"Objeto no serializable: {type(valor)}")


with open("dashboards/indicadores.json", "w", encoding="utf-8") as f:
    json.dump(salida, f, indent=2, ensure_ascii=False, default=_a_nativo)

print("Reporte exportado a dashboards/indicadores.json")
