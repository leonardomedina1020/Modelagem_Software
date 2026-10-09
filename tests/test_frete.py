import sys
from pathlib import Path

# Garante que a raiz do projeto esteja no sys.path independentemente da forma de execução do pytest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from src.frete import calcular_frete


class TestCalculoFreteRF01:
    """RF01: WHEN o sistema calcular o frete de um carrinho com subtotal maior que zero
    e menor que 250 reais, THE SYSTEM SHALL retornar uma taxa de frete de 15 reais.
    """

    @pytest.mark.parametrize(
        "subtotal",
        [
            0.01,    # Limite inferior (imediatamente acima de zero)
            1.0,     # Valor baixo
            100.0,   # Valor intermediário
            200.0,   # Antigo limite de frete grátis (agora deve cobrar frete)
            249.99,  # Limite superior (imediatamente abaixo de 250)
        ],
    )
    def test_frete_subtotal_maior_que_zero_e_menor_que_duzentos_e_cinquenta(self, subtotal):
        assert calcular_frete(subtotal) == 15


class TestCalculoFreteRF02:
    """RF02: IF o subtotal do carrinho for maior ou igual a 250 reais,
    THEN THE SYSTEM SHALL retornar uma taxa de frete de 0 reais.
    """

    @pytest.mark.parametrize(
        "subtotal",
        [
            250.0,   # Limite exato de fronteira (250 reais)
            250.01,  # Imediatamente acima de 250 reais
            300.0,   # Valor acima de 250 reais
            1000.0,  # Valor alto
        ],
    )
    def test_frete_subtotal_maior_ou_igual_a_duzentos_e_cinquenta(self, subtotal):
        assert calcular_frete(subtotal) == 0


class TestCalculoFreteRF03:
    """RF03: IF o subtotal do carrinho for menor ou igual a zero,
    THEN THE SYSTEM SHALL rejeitar o cálculo e lançar um ValueError
    com a mensagem 'Valor de carrinho inválido'.
    """

    @pytest.mark.parametrize(
        "subtotal",
        [
            0.0,    # Limite exato de fronteira (zero)
            -0.01,  # Imediatamente abaixo de zero
            -10.0,  # Valor negativo
        ],
    )
    def test_subtotal_menor_ou_igual_a_zero_lanca_value_error(self, subtotal):
        with pytest.raises(ValueError, match=r"^Valor de carrinho inválido$"):
            calcular_frete(subtotal)
