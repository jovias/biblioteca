
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from biblioteca.modelos import Livro
from biblioteca.repositorio import Repositorio
from biblioteca.avaliacoes import ServicoAvaliacoes, NotaInvalida

scenarios("avaliacoes.feature")


@pytest.fixture
def contexto():
    repo = Repositorio()
    return {"repo": repo, "servico": ServicoAvaliacoes(repo), "erro": None}


@given(parsers.parse('que o livro "{titulo}" com ISBN "{isbn}" está cadastrado'))
def livro_cadastrado(contexto, titulo, isbn):
    contexto["repo"].livros[isbn] = Livro(isbn, titulo, "Autor")


@when(parsers.parse('eu avaliar o livro "{isbn}" com nota {nota:d}'))
def avaliar(contexto, isbn, nota):
    try:
        contexto["servico"].avaliar(isbn, nota)
    except NotaInvalida as e:
        contexto["erro"] = str(e)


@then(parsers.parse('a média do livro "{isbn}" deve ser {media:f}'))
def media_deve_ser(contexto, isbn, media):
    assert contexto["servico"].media(isbn) == media


@then(parsers.parse('a avaliação deve ser recusada com a mensagem "{mensagem}"'))
def recusada(contexto, mensagem):
    assert contexto["erro"] == mensagem
