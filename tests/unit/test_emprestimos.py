import pytest
from biblioteca.modelos import Livro, Usuario
from biblioteca.repositorio import Repositorio
from biblioteca.emprestimos import emprestar_livro


def test_emprestar_livro_disponivel():
    repo = Repositorio()

    livro = Livro(
        isbn="123",
        titulo="Dom Casmurro",
        autor="Machado de Assis"
    )

    usuario = Usuario(
        nome="Ana",
        email="ana@email.com"
    )


def test_nao_emprestar_livro_indisponivel():
    repo = Repositorio()

    livro = Livro(
        isbn="456",
        titulo="O Cortiço",
        autor="Aluísio Azevedo",
        disponivel=False
    )

    usuario = Usuario(
        nome="Ana",
        email="ana@email.com"
    )


def test_nao_emprestar_para_usuario_bloqueado():
    repo = Repositorio()

    livro = Livro(
        isbn="789",
        titulo="Memórias Póstumas de Brás Cubas",
        autor="Machado de Assis"
    )

    usuario = Usuario(
        nome="Ana",
        email="ana@email.com",
        bloqueado=True
    )

    repo.livros[livro.isbn] = livro
    repo.usuarios[usuario.email] = usuario

    with pytest.raises(ValueError):
        emprestar_livro(repo, livro.isbn, usuario.email)

    assert len(repo.emprestimos) == 0
    assert livro.disponivel is True

