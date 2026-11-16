
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

    repo.livros[livro.isbn] = livro
    repo.usuarios[usuario.email] = usuario

    emprestimo = emprestar_livro(repo, livro.isbn, usuario.email)

    assert emprestimo.ativo is True
    assert livro.disponivel is False
    assert len(repo.emprestimos) == 1
