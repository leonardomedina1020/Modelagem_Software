# Especificação — Cálculo de Frete

## 1. Requisitos Funcionais

**RF01:** WHEN o sistema calcular o frete de um carrinho com subtotal maior que zero e menor que 250 reais, THE SYSTEM SHALL retornar uma taxa de frete de 15 reais.

**RF02:** IF o subtotal do carrinho for maior ou igual a 250 reais, THEN THE SYSTEM SHALL retornar uma taxa de frete de 0 reais.

**RF03:** IF o subtotal do carrinho for menor ou igual a zero, THEN THE SYSTEM SHALL rejeitar o cálculo e lançar um ValueError com a mensagem "Valor de carrinho inválido".