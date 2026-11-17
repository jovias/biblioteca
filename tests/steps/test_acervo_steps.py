import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from biblioteca.repositorio import Repositorio
from biblioteca.acervo import Acervo, LivroDuplicado

scenarios("acervo.feature")


@pytest.fixture
def contexto():
    repo = Repositorio()
    return {"repo": repo, "acervo": Acervo(repo), "erro": None, "resultado": None}


@given("que o acervo está vazio")
def acervo_vazio(contexto):
    assert contexto["repo"].livros == {}


@given(parsers.parse('que o livro "{titulo}" com ISBN "{isbn}" está cadastrado'))
def livro_cadastrado(contexto, titulo, isbn):
    contexto["acervo"].cadastrar_livro(isbn, titulo, "Autor")


@when(parsers.parse('eu cadastrar o livro "{titulo}" com ISBN "{isbn}"'))
def cadastrar(contexto, titulo, isbn):
    try:
        contexto["acervo"].cadastrar_livro(isbn, titulo, "Autor")
    except LivroDuplicado as e:
        contexto["erro"] = str(e)


@when(parsers.parse('eu buscar por "{texto}"'))
def buscar(contexto, texto):
    contexto["resultado"] = contexto["acervo"].buscar_por_titulo(texto)


@then(parsers.parse("o acervo deve ter {qtd:d} livro"))
def acervo_tem(contexto, qtd):
    assert len(contexto["repo"].livros) == qtd


@then(parsers.parse('o cadastro deve ser recusado com a mensagem "{mensagem}"'))
def recusado(contexto, mensagem):
    assert contexto["erro"] == mensagem


@then(parsers.parse('o resultado deve conter o livro "{titulo}"'))
def resultado_contem(contexto, titulo):
    assert titulo in [livro.titulo for livro in contexto["resultado"]]


@then("o resultado deve estar vazio")
def resultado_vazio(contexto):
    assert contexto["resultado"] == []
