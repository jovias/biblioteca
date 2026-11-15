import pytest

from biblioteca.modelos import Livro, Usuario
from biblioteca.repositorio import Repositorio
from biblioteca.usuarios import CadastroUsuarios
from biblioteca.usuarios import UsuarioInvalido
from biblioteca.usuarios import UsuarioDuplicado


def test_cadastrar_usuario_guarda_usuario():
    repo = Repositorio()
    cadastro = CadastroUsuarios(repo)

    cadastro.cadastrar("Ana", "ana@email.com")

    assert repo.usuarios["ana@email.com"].nome == "Ana"


def test_nao_cadastra_email_invalido():
    cadastro = CadastroUsuarios(Repositorio())

    with pytest.raises(UsuarioInvalido):
        cadastro.cadastrar("Ana", "ana.email.com")   


def test_nao_cadastra_email_repetido():
    cadastro = CadastroUsuarios(Repositorio())
    cadastro.cadastrar("Ana", "ana@email.com")

    with pytest.raises(UsuarioDuplicado):
        cadastro.cadastrar("Ana Maria", "ana@email.com")



def test_bloquear_usuario():
    repo = Repositorio()
    cadastro = CadastroUsuarios(repo)
    cadastro.cadastrar("Ana", "ana@email.com")

    cadastro.bloquear("ana@email.com")

    assert repo.usuarios["ana@email.com"].bloqueado is True    


def test_desbloquear_usuario():
    repo = Repositorio()
    cadastro = CadastroUsuarios(repo)
    cadastro.cadastrar("Ana", "ana@email.com")
    cadastro.bloquear("ana@email.com")

    cadastro.desbloquear("ana@email.com")

    assert repo.usuarios["ana@email.com"].bloqueado is False