from biblioteca.modelos import Usuario
from biblioteca.repositorio import Repositorio
from biblioteca.multas import ServicoMultas


def preparar():
    repo = Repositorio()
    repo.usuarios["ana@email.com"] = Usuario("Ana", "ana@email.com")
    return repo, ServicoMultas(repo)


def test_sem_multa_dentro_do_prazo():
    repo, servico = preparar()

    assert servico.calcular_multa("ana@email.com", 10) == 0.0


def test_multa_de_dois_reais_por_dia_de_atraso():
    repo, servico = preparar()

    assert servico.calcular_multa("ana@email.com", 16) == 4.0


def test_multa_registra_debito_e_bloqueia_usuario():
    repo, servico = preparar()

    servico.calcular_multa("ana@email.com", 16)

    assert repo.multas["ana@email.com"] == 4.0
    assert repo.usuarios["ana@email.com"].bloqueado is True
