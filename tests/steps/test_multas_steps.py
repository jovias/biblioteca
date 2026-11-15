import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from biblioteca.modelos import Usuario
from biblioteca.repositorio import Repositorio
from biblioteca.multas import ServicoMultas, SemMultaPendente

scenarios("multas.feature")


@pytest.fixture
def contexto():
    repo = Repositorio()
    return {"repo": repo, "servico": ServicoMultas(repo), "erro": None, "valor": None}


@given(parsers.parse('que a usuária "{email}" está cadastrada'))
def usuaria_cadastrada(contexto, email):
    contexto["repo"].usuarios[email] = Usuario("Ana", email)


@given(parsers.parse('que a usuária "{email}" tem uma multa por {dias:d} dias com o livro'))
def tem_multa(contexto, email, dias):
    contexto["servico"].calcular_multa(email, dias)


@when(parsers.parse('a usuária "{email}" devolver um livro após {dias:d} dias'))
def devolver_apos(contexto, email, dias):
    contexto["valor"] = contexto["servico"].calcular_multa(email, dias)


@when(parsers.parse('a usuária "{email}" pagar a multa'))
def pagar(contexto, email):
    try:
        contexto["servico"].pagar_multa(email)
    except SemMultaPendente as e:
        contexto["erro"] = str(e)


@then(parsers.parse("a multa deve ser de {valor:f} reais"))
def multa_de(contexto, valor):
    assert contexto["valor"] == valor


@then(parsers.parse('a usuária "{email}" deve estar bloqueada'))
def bloqueada(contexto, email):
    assert contexto["repo"].usuarios[email].bloqueado is True


@then(parsers.parse('a usuária "{email}" não deve estar bloqueada'))
def nao_bloqueada(contexto, email):
    assert contexto["repo"].usuarios[email].bloqueado is False


@then(parsers.parse('a usuária "{email}" não deve ter multa pendente'))
def sem_multa(contexto, email):
    assert email not in contexto["repo"].multas


@then(parsers.parse('o pagamento deve ser recusado com a mensagem "{mensagem}"'))
def recusado(contexto, mensagem):
    assert contexto["erro"] == mensagem
