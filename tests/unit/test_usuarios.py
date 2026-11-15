import pytest

from biblioteca.modelos import Livro, Usuario
from biblioteca.repositorio import Repositorio
from biblioteca.usuarios import CadastroUsuarios


def test_cadastrar_usuario_guarda_usuario():
    repo = Repositorio()
    cadastro = CadastroUsuarios(repo)

    cadastro.cadastrar("Ana", "ana@email.com")

    assert repo.usuarios["ana@email.com"].nome == "Ana"