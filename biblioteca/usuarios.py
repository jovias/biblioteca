from biblioteca.modelos import Usuario


class UsuarioInvalido(Exception):
    pass


class CadastroUsuarios:
    def __init__(self, repo):
        self.repo = repo

    def cadastrar(self, nome, email):
        self.repo.usuarios[email] = Usuario(nome, email)