import sys
from pathlib import Path

# Garante que a raiz do projeto esteja no sys.path independentemente da forma de execução do pytest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.checkout import calcular_total


def test_calcular_total_com_frete():
    """RF04 / CT02: WHEN o sistema calcular o valor total de uma compra com subtotal maior que zero,
    THE SYSTEM SHALL retornar a soma do subtotal com a taxa de frete obtida pela função calcular_frete(subtotal).
    Para entrada de 100 reais, o total deve ser 115 reais (100 de subtotal + 15 de frete).
    """
    assert calcular_total(100) == 115
