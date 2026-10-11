from src.frete import calcular_frete


def calcular_total(subtotal: float) -> float:
    return subtotal + calcular_frete(subtotal)


def main() -> None:
    subtotal = float(input())
    frete = calcular_frete(subtotal)
    total = calcular_total(subtotal)
    print(f"Frete: R$ {frete:.2f}".replace(".", ","))
    print(f"Total: R$ {total:.2f}".replace(".", ","))


if __name__ == "__main__":
    main()
