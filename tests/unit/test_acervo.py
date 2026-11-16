import pytest

from biblioteca.modelos import Livro, Usuario
from biblioteca.repositorio import Repositorio
from biblioteca.acervo import Acervo
from biblioteca.acervo import LivroInvalido
from biblioteca.acervo import LivroDuplicado


def test_cadastrar_livro_guarda_no_acervo():
    repo = Repositorio()
    acervo = Acervo(repo)

    acervo.cadastrar_livro("111", "Dom Casmurro", "Machado de Assis")

    assert repo.livros["111"].titulo == "Dom Casmurro"


def test_nao_cadastra_livro_sem_isbn():
    acervo = Acervo(Repositorio())

    with pytest.raises(LivroInvalido):
        acervo.cadastrar_livro("", "Dom Casmurro", "Machado de Assis")


def test_nao_cadastra_isbn_repetido():
    acervo = Acervo(Repositorio())
    acervo.cadastrar_livro("111", "Dom Casmurro", "Machado de Assis")

    with pytest.raises(LivroDuplicado):
        acervo.cadastrar_livro("111", "Outro livro", "Outro autor")


def test_busca_encontra_livro_pelo_titulo():
    acervo = Acervo(Repositorio())
    acervo.cadastrar_livro("111", "Dom Casmurro", "Machado de Assis")

    resultado = acervo.buscar_por_titulo("Dom Casmurro")

    assert [livro.titulo for livro in resultado] == ["Dom Casmurro"]


def test_busca_nao_traz_outros_titulos():
    acervo = Acervo(Repositorio())
    acervo.cadastrar_livro("111", "Dom Casmurro", "Machado de Assis")
    acervo.cadastrar_livro("222", "Iracema", "José de Alencar")

    resultado = acervo.buscar_por_titulo("Iracema")

    assert [livro.titulo for livro in resultado] == ["Iracema"]