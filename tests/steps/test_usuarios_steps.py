import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from biblioteca.repositorio import Repositorio
from biblioteca.usuarios import CadastroUsuarios, UsuarioInvalido

scenarios("usuarios.feature")


@pytest.fixture
def contexto():
    repo = Repositorio()
    return {"repo": repo, "cadastro": CadastroUsuarios(repo), "erro": None}


@given(parsers.parse('que a usuária "{nome}" com e-mail "{email}" está cadastrada'))
def usuaria_cadastrada(contexto, nome, email):
    contexto["cadastro"].cadastrar(nome, email)


@given(parsers.parse('que a usuária "{email}" está bloqueada'))
def usuaria_bloqueada(contexto, email):
    contexto["cadastro"].bloquear(email)


@when(parsers.parse('eu cadastrar a usuária "{nome}" com e-mail "{email}"'))
def cadastrar(contexto, nome, email):
    try:
        contexto["cadastro"].cadastrar(nome, email)
    except UsuarioInvalido as e:
        contexto["erro"] = str(e)


@when(parsers.parse('eu bloquear a usuária "{email}"'))
def bloquear(contexto, email):
    contexto["cadastro"].bloquear(email)


@when(parsers.parse('eu desbloquear a usuária "{email}"'))
def desbloquear(contexto, email):
    contexto["cadastro"].desbloquear(email)


@then(parsers.parse('a usuária "{email}" deve estar cadastrada'))
def esta_cadastrada(contexto, email):
    assert email in contexto["repo"].usuarios


@then(parsers.parse('o cadastro deve ser recusado com a mensagem "{mensagem}"'))
def recusado(contexto, mensagem):
    assert contexto["erro"] == mensagem


@then(parsers.parse('a usuária "{email}" deve estar bloqueada'))
def esta_bloqueada(contexto, email):
    assert contexto["repo"].usuarios[email].bloqueado is True


@then(parsers.parse('a usuária "{email}" não deve estar bloqueada'))
def nao_esta_bloqueada(contexto, email):
    assert contexto["repo"].usuarios[email].bloqueado is False
