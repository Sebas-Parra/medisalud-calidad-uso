"""
Escenario 8 - prueba unitaria recomendada por el taller: verifica que
metrica_eficiencia y metrica_efectividad calculan correctamente el promedio
sobre un conjunto de datos controlado, no sobre datos reales.
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from metricas_iso25022 import metrica_efectividad, metrica_eficiencia  # noqa: E402


def test_metrica_eficiencia_calcula_promedio_correcto():
    logs = pd.DataFrame({
        "tiempo_segundos": [4.0, 6.0, 8.0, 10.0],
        "completada": [1, 1, 1, 1],
    })
    resultado = metrica_eficiencia(logs)
    assert resultado["valor"] == 7.0
    assert resultado["cumple"] is True  # 7.0 <= 8.0 (umbral RNF-01)


def test_metrica_eficiencia_excluye_registros_no_completados():
    logs = pd.DataFrame({
        "tiempo_segundos": [4.0, 6.0, 120.0],
        "completada": [1, 1, 0],
    })
    resultado = metrica_eficiencia(logs)
    # El registro de 120s (no completado) no debe contaminar el promedio
    assert resultado["valor"] == 5.0
    assert resultado["cumple"] is True


def test_metrica_efectividad_calcula_proporcion_correcta():
    logs = pd.DataFrame({"completada": [1, 1, 1, 0]})
    resultado = metrica_efectividad(logs)
    assert resultado["valor"] == 0.75
    assert resultado["cumple"] is False
