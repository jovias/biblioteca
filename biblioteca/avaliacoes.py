class NotaInvalida(ValueError):
    pass


NOTA_MINIMA = 1
NOTA_MAXIMA = 5


class ServicoAvaliacoes:
    def __init__(self, repositorio):
        self.repo = repositorio

    
    def avaliar(self, isbn, nota):
        if not NOTA_MINIMA <= nota <= NOTA_MAXIMA:
            raise NotaInvalida("A nota deve ser de 1 a 5")

        self.repo.avaliacoes.setdefault(isbn, []).append(nota)

    def media(self, isbn):
        return 0.0
