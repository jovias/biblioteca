import pytest

from biblioteca.modelos import Livro, Usuario
from biblioteca.repositorio import Repositorio
from biblioteca.acervo import Acervo
from biblioteca.acervo import LivroInvalido


def test_cadastrar_livro_guarda_no_acervo():
    repo = Repositorio()
    acervo = Acervo(repo)

    acervo.cadastrar_livro("111", "Dom Casmurro", "Machado de Assis")

    assert repo.livros["111"].titulo == "Dom Casmurro"


def test_nao_cadastra_livro_sem_isbn():
    acervo = Acervo(Repositorio())

    with pytest.raises(LivroInvalido):
        acervo.cadastrar_livro("", "Dom Casmurro", "Machado de Assis")