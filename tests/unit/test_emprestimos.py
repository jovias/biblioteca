import pytest
from biblioteca.modelos import Livro, Usuario, Emprestimo
from biblioteca.repositorio import Repositorio
from biblioteca.emprestimos import emprestar_livro, devolver_livro


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

def test_nao_emprestar_acima_do_limite():
    repo = Repositorio()

    usuario = Usuario(
        nome="Ana",
        email="ana@email.com"
    )
    repo.usuarios[usuario.email] = usuario

    # Cria três empréstimos ativos para Ana
    for i in range(3):
        livro = Livro(
            isbn=str(100 + i),
            titulo=f"Livro {i + 1}",
            autor="Autor Teste",
            disponivel=False
        )

        repo.livros[livro.isbn] = livro

        emprestimo = Emprestimo(
            livro=livro,
            usuario=usuario,
            ativo=True
        )

        repo.emprestimos.append(emprestimo)

    # Livro que Ana tentará emprestar
    novo_livro = Livro(
        isbn="999",
        titulo="Dom Casmurro",
        autor="Machado de Assis"
    )

    repo.livros[novo_livro.isbn] = novo_livro

    
    with pytest.raises(
        ValueError,
        match="Limite de 3 empréstimos atingido"
    ):
        emprestar_livro(
            repo,
            novo_livro.isbn,
            usuario.email
        )

def test_devolver_livro_emprestado():
    repo = Repositorio()

    livro = Livro(
        isbn="555",
        titulo="Dom Casmurro",
        autor="Machado de Assis"
    )

    usuario = Usuario(
        nome="Ana",
        email="ana@email.com"
    )

    repo.livros[livro.isbn] = livro
    repo.usuarios[usuario.email] = usuario

    
    emprestimo = emprestar_livro(
        repo, livro.isbn, usuario.email
    )

    assert emprestimo.ativo is True
    assert livro.disponivel is False

    
    devolver_livro(repo, livro.isbn, usuario.email)

def test_nao_devolver_livro_nao_emprestado():
    repo = Repositorio()

    livro = Livro(
        isbn="999",
        titulo="Dom Casmurro",
        autor="Machado de Assis"
    )

    usuario = Usuario(
        nome="Ana",
        email="ana@email.com"
    )

    repo.livros[livro.isbn] = livro
    repo.usuarios[usuario.email] = usuario

    with pytest.raises(
        ValueError,
        match="Empréstimo ativo não encontrado"
    ):
        devolver_livro(repo, livro.isbn, usuario.email)

    assert livro.disponivel is True
    assert len(repo.emprestimos) == 0
