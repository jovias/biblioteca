# Validação do módulo de multas

Na branch `joao-multas-tdd`, o módulo foi reimplementado com cenários BDD e seis ciclos TDD, documentados nos commits RED e GREEN.

## Execuções confirmadas pelo integrante

- `py -m pytest tests/unit/test_multas.py -v`: seis testes unitários aprovados no encerramento do ciclo 6 (`6 passed`).
- `py -m pytest tests/steps/test_multas_steps.py -v`: quatro cenários BDD aprovados (`4 passed`).

## Cenários BDD aprovados

1. Devolução dentro do prazo.
2. Devolução com atraso.
3. Pagar multa desbloqueia a usuária.
4. Recusar pagamento sem multa.

As capturas das execuções foram registradas pelo integrante para o relatório acadêmico.
