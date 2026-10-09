def calcular_frete(subtotal: float) -> int:
    if subtotal <= 0:
        raise ValueError("Valor de carrinho inválido")
    if subtotal >= 200:
        return 0
    return 15
