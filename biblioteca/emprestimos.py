
from biblioteca.modelos import Emprestimo


def emprestar_livro(repo, isbn, email):
    livro = repo.livros[isbn]
    usuario = repo.usuarios[email]

    if not livro.disponivel:
        raise ValueError("Livro indisponível")

    emprestimo = Emprestimo(
        livro=livro,
        usuario=usuario
    )

    repo.emprestimos.append(emprestimo)
    livro.disponivel = False

    return emprestimo
