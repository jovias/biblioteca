
class NotaInvalida(ValueError):
    pass


class ServicoAvaliacoes:
    def __init__(self, repositorio):
        self.repo = repositorio

    def avaliar(self, isbn, nota):
        pass

    def media(self, isbn):
        return 0.0
