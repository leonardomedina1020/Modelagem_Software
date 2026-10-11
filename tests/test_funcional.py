import subprocess
import sys


def test_checkout_cli_subtotal_250():
    """CT03 / RF05: Executa a aplicação como um usuário real por meio de
    'python -m src.checkout', simulando a entrada de 250 reais e verificando
    que a saída apresenta 'Frete: R$ 0,00' e 'Total: R$ 250,00' com código de retorno 0.
    """
    resultado = subprocess.run(
        [sys.executable, "-m", "src.checkout"],
        input="250\n",
        text=True,
        capture_output=True,
        encoding="utf-8",
    )
    assert resultado.returncode == 0
    assert "Frete: R$ 0,00" in resultado.stdout
    assert "Total: R$ 250,00" in resultado.stdout
