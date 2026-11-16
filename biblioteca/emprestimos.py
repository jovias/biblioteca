
from biblioteca.modelos import Emprestimo


def emprestar_livro(repo, isbn, email):
    livro = repo.livros[isbn]
    usuario = repo.usuarios[email]

    if not livro.disponivel:
        raise ValueError("Livro indisponível")

    if usuario.bloqueado:
        raise ValueError("Usuário bloqueado")

    emprestimos_ativos = sum(
        1 for emprestimo in repo.emprestimos
        if emprestimo.usuario.email == email and emprestimo.ativo
    )

    if emprestimos_ativos >= 3:
        raise ValueError("Limite de 3 empréstimos atingido")

    emprestimo = Emprestimo(
        livro=livro,
        usuario=usuario
    )

    repo.emprestimos.append(emprestimo)
    livro.disponivel = False

    return emprestimo
