
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from biblioteca.modelos import Livro, Usuario
from biblioteca.repositorio import Repositorio
from biblioteca.emprestimos import emprestar_livro, devolver_livro

scenarios("emprestimos.feature")


@pytest.fixture
def contexto():
    return {
        "repo": Repositorio(),
        "livro": None,
        "usuario": None,
        "resultado": None,
        "erro": None,
    }


def preparar_livro(contexto, titulo, disponivel=True):
    livro = Livro(
        isbn="123",
        titulo=titulo,
        autor="Machado de Assis",
        disponivel=disponivel,
    )
    contexto["repo"].livros[livro.isbn] = livro
    contexto["livro"] = livro


def preparar_usuario(contexto, nome="Ana", bloqueado=False):
    usuario = Usuario(
        nome=nome,
        email="ana@email.com",
        bloqueado=bloqueado,
    )
    contexto["repo"].usuarios[usuario.email] = usuario
    contexto["usuario"] = usuario


@given(parsers.parse('que o livro "{titulo}" está disponível'))
def livro_disponivel(contexto, titulo):
    preparar_livro(contexto, titulo)


@given(parsers.parse('que a usuária "{nome}" não possui empréstimos'))
def usuario_sem_emprestimos(contexto, nome):
    preparar_usuario(contexto, nome)


@given(parsers.parse('que a usuária "{nome}" possui 3 livros emprestados'))
def usuario_com_tres_emprestimos(contexto, nome):
    preparar_usuario(contexto, nome)

    for i in range(3):
        livro = Livro(
            isbn=str(200 + i),
            titulo=f"Livro {i}",
            autor="Autor",
        )
        contexto["repo"].livros[livro.isbn] = livro
        emprestar_livro(
            contexto["repo"],
            livro.isbn,
            contexto["usuario"].email,
        )


@given(parsers.parse('que a usuária "{nome}" está bloqueada'))
def usuario_bloqueado(contexto, nome):
    preparar_usuario(contexto, nome, bloqueado=True)


@given(parsers.parse('que o livro "{titulo}" já está emprestado'))
def livro_ja_emprestado(contexto, titulo):
    preparar_livro(contexto, titulo, disponivel=False)


@given(parsers.parse('que o livro "{titulo}" está emprestado para Ana'))
def livro_emprestado_para_ana(contexto, titulo):
    preparar_livro(contexto, titulo)
    preparar_usuario(contexto)

    emprestar_livro(
        contexto["repo"],
        contexto["livro"].isbn,
        contexto["usuario"].email,
    )


@given(parsers.parse('que o livro "{titulo}" não está emprestado'))
def livro_nao_emprestado(contexto, titulo):
    preparar_livro(contexto, titulo)
    preparar_usuario(contexto)


@when(parsers.parse('Ana tentar pegar o livro "{titulo}" emprestado'))
@when(parsers.parse('Ana pegar o livro "{titulo}" emprestado'))
def tentar_emprestar(contexto, titulo):
    if contexto["livro"] is None:
        preparar_livro(contexto, titulo)

    if contexto["usuario"] is None:
        preparar_usuario(contexto)

    try:
        contexto["resultado"] = emprestar_livro(
            contexto["repo"],
            contexto["livro"].isbn,
            contexto["usuario"].email,
        )
    except ValueError as erro:
        contexto["erro"] = str(erro)


@when(parsers.parse('Ana devolver o livro "{titulo}"'))
@when(parsers.parse('Ana tentar devolver o livro "{titulo}"'))
def tentar_devolver(contexto, titulo):
    if contexto["livro"] is None:
        preparar_livro(contexto, titulo)

    if contexto["usuario"] is None:
        preparar_usuario(contexto)

    try:
        contexto["resultado"] = devolver_livro(
            contexto["repo"],
            contexto["livro"].isbn,
            contexto["usuario"].email,
        )
    except ValueError as erro:
        contexto["erro"] = str(erro)


@then("o empréstimo deve ser registrado")
def emprestimo_registrado(contexto):
    assert contexto["resultado"] is not None
    assert contexto["resultado"].ativo is True


@then("o empréstimo deve ser recusado")
def emprestimo_recusado(contexto):
    assert contexto["erro"] is not None


@then(parsers.parse('deve aparecer a mensagem "{mensagem}"'))
def verificar_mensagem(contexto, mensagem):
    assert contexto["erro"] == mensagem


@then(parsers.parse('o livro "{titulo}" deve ficar indisponível'))
def livro_indisponivel(contexto, titulo):
    assert contexto["livro"].disponivel is False


@then("a devolução deve ser registrada")
def devolucao_registrada(contexto):
    assert contexto["resultado"] is not None
    assert contexto["resultado"].ativo is False


@then(parsers.parse('o livro "{titulo}" deve ficar disponível'))
def livro_disponivel_novamente(contexto, titulo):
    assert contexto["livro"].disponivel is True


@then("a devolução deve ser recusada")
def devolucao_recusada(contexto):
    assert contexto["erro"] is not None
