import pytest

from biblioteca.modelos import Livro, Usuario
from biblioteca.repositorio import Repositorio
from biblioteca.acervo import Acervo


def test_cadastrar_livro_guarda_no_acervo():
    repo = Repositorio()
    acervo = Acervo(repo)

    acervo.cadastrar_livro("111", "Dom Casmurro", "Machado de Assis")

    assert repo.livros["111"].titulo == "Dom Casmurro"