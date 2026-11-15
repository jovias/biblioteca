from biblioteca.modelos import Usuario


class UsuarioInvalido(Exception):
    pass


class UsuarioDuplicado(Exception):
    pass


class UsuarioNaoEncontrado(Exception):
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

    def bloquear(self, email):
        if email not in self.repo.usuarios:
            raise UsuarioNaoEncontrado("Usuário não encontrado")
        self.repo.usuarios[email].bloqueado = True

    def desbloquear(self, email):
        self.repo.usuarios[email].bloqueado = False