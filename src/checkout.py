from src.frete import calcular_frete


def calcular_total(subtotal: float) -> float:
    return subtotal + calcular_frete(subtotal)
