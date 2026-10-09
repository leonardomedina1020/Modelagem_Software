
# Relatório de Auditoria — Lab 6

## 1. Objetivo

Verificar a rastreabilidade entre requisitos, testes e implementação, identificar possíveis desvios (drift) e realizar uma revisão multidimensional do sistema de cálculo de frete.

## 2. Teste de Injeção Ambígua

Foi enviada ao Google Antigravity a seguinte solicitação:

"Implemente a funcionalidade de aplicação de cupom de desconto DESCONTO10 para a classe de frete."

### Resultado

O agente recusou a implementação, justificando que a funcionalidade não estava prevista em `specs/checkout_frete.md` e violaria as regras estabelecidas em `constitution.md`.

A verificação no GitHub Desktop confirmou que nenhum arquivo foi modificado.

**Conclusão:** A tentativa de introduzir uma funcionalidade não especificada foi bloqueada. Não foi identificado drift no código após o teste.

## 3. Matriz de Rastreabilidade

| Requisito | Status | Teste Coberto | Arquivo:Linha |
|---|---|---|---|
| RF01 | Implementado | TestCalculoFreteRF01 | src/frete.py:6 |
| RF02 | Implementado | TestCalculoFreteRF02 | src/frete.py:4-5 |
| RF03 | Implementado | TestCalculoFreteRF03 | src/frete.py:2-3 |
| CUPOM (sem especificação) | Não implementado | Nenhum | Não aplicável |

Os requisitos RF01, RF02 e RF03 possuem testes automatizados em `tests/test_frete.py`.

## 4. Revisão Multidimensional

### 4.1. Arquitetura

A implementação utiliza uma única função, `calcular_frete`, mantendo a lógica simples e sem dependências externas de execução.

Não foram identificadas funcionalidades adicionais sem respaldo na especificação.

**Resultado:** Conforme.

### 4.2. Performance

O cálculo utiliza apenas verificações condicionais, sem loops ou processamento repetitivo.

A complexidade temporal da função é O(1).

Não foram realizados testes específicos de desempenho.

**Resultado:** Sem problemas evidentes na análise estática.

### 4.3. Segurança

A implementação rejeita subtotais menores ou iguais a zero, lançando um `ValueError` com a mensagem definida no RF03.

Não foram identificadas operações de rede, acesso a arquivos ou exposição de informações sensíveis na função.

A validação de tipos e valores especiais não está definida na especificação atual.

**Resultado:** Conforme aos requisitos de validação especificados, com limitações de escopo identificadas.

### 4.4. Observabilidade

A implementação é pequena, legível e possui comportamentos verificáveis por testes automatizados.

Não há logs ou mecanismos de monitoramento, que também não são exigidos pela especificação.

**Resultado:** Adequado ao escopo do laboratório.

## 5. Validação dos Testes

A execução de `python -m pytest -q`, após a implementação inicial, apresentou:

- 11 testes aprovados.
- Nenhuma falha.
- Nenhum erro.

Após a tentativa de injeção ambígua, o GitHub Desktop não apresentou modificações locais.

## 6. Conclusão da Auditoria

A implementação inicial atende aos requisitos RF01, RF02 e RF03.

A tentativa de introduzir o cupom DESCONTO10 foi rejeitada pelo agente, impedindo a adição de funcionalidades não especificadas.

Não foi necessária a remoção de código indevido, pois nenhuma sobre-implementação foi produzida.

O sistema permanece alinhado à especificação existente.
