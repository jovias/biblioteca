# Sistema de Biblioteca – BDD/TDD

Projeto da Avaliação Somativa RA4 – Parte 1 da disciplina Verificação e Validação (PUCPR).

Sistema simples de biblioteca em Python, desenvolvido com BDD (pytest-bdd, cenários em Gherkin em português) e TDD (pytest). Os dados ficam em memória e não há interface: o sistema é exercitado pelos testes.

## Equipe e funcionalidades

| Integrante | Módulo | Funcionalidades |
| --- | --- | --- |
| Yumi | `biblioteca/acervo.py` | F1 cadastrar livro · F2 buscar livro por título |
| Fernanda | `biblioteca/usuarios.py` | F3 cadastrar usuário · F4 bloquear/desbloquear usuário |
| Igor | `biblioteca/emprestimos.py` | F5 emprestar livro · F6 devolver livro |
| João Vitor | `biblioteca/multas.py` | F7 calcular multa · F8 pagar multa |
| Mariana | `biblioteca/avaliacoes.py` | F9 avaliar livro · F10 calcular média das avaliações |

## Como rodar

Requer Python 3.10 ou mais recente.

macOS:

```bash
python3 -m pip install pytest pytest-bdd
python3 -m pytest -v
```

Windows:

```powershell
py -m pip install pytest pytest-bdd
py -m pytest -v
```

## Estrutura

```
biblioteca/          código do sistema
tests/features/      cenários BDD (Gherkin, em português)
tests/steps/         ligação dos cenários ao código (pytest-bdd)
tests/unit/          testes unitários escritos no ciclo TDD (pytest)
```
