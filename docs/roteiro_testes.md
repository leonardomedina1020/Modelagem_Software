
# Roteiro de Testes — Sistema de Cálculo de Frete

## 1. Objetivo

Validar as funcionalidades do sistema de cálculo de frete por meio de testes unitários, de integração e funcionais, verificando a conformidade com os requisitos especificados.

## 2. Casos de Teste


### CT01 — Teste Unitário

- **Objetivo:** Verificar a aplicação de frete grátis para compras com subtotal maior ou igual a 250 reais.
- **Requisito:** RF02.
- **Pré-condição:** A função `calcular_frete()` deve estar implementada.
- **Entradas:** 250.00, 250.01, 300.00 e 1000.00.
- **Procedimento:** Executar os quatro casos parametrizados da classe `TestCalculoFreteRF02` utilizando pytest.
- **Resultado esperado:** Retornar 0 reais de frete para todas as entradas.
- **Resultado obtido:** 4 casos aprovados (PASSED).
- **Status:** Aprovado.


### CT02 — Teste de Integração

- **Objetivo:** Verificar a integração entre o cálculo de frete e o cálculo do valor total de uma compra.
- **Pré-condição:** Existência de um componente de checkout que utilize a função `calcular_frete()`.
- **Entrada:** Subtotal de 100 reais.
- **Procedimento:** Executar o cálculo total da compra, incluindo o frete.
- **Resultado esperado:** Total de 115 reais, sendo 100 reais de subtotal e 15 reais de frete.
- **Status:** Pendente de implementação e execução.

### CT03 — Teste Funcional

- **Objetivo:** Verificar o cálculo de uma compra por meio da interface de execução do sistema.
- **Pré-condição:** Existência de uma interface de linha de comando para o checkout.
- **Entrada:** Subtotal de 250 reais.
- **Procedimento:** Executar a aplicação, informar o subtotal e consultar o resultado.
- **Resultado esperado:** Frete de 0 reais e total de 250 reais.
- **Status:** Pendente de implementação e execução.

## 3. Critérios de Aceitação

- Os três tipos de teste devem ser executados.
- Os resultados obtidos devem corresponder aos resultados esperados.
- Cada teste deve possuir código disponível no GitHub.
- Cada execução deve ter seu resultado registrado.
- Nenhum teste deve ser considerado aprovado sem execução efetiva.
