from biblioteca.modelos import Usuario


class UsuarioInvalido(Exception):
    pass


class UsuarioDuplicado(Exception):
    pass


class CadastroUsuarios:
    def __init__(self, repo):
        self.repo = repo

    def cadastrar(self, nome, email):
        if "@" not in email:
            raise UsuarioInvalido("E-mail inválido")
        if email in self.repo.usuarios:
            raise UsuarioDuplicado("E-mail já cadastrado")
        self.repo.usuarios[email] = Usuario(nome, email)
    