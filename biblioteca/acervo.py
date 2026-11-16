from biblioteca.modelos import Livro

class LivroInvalido(Exception):
    pass

class Acervo:
    def __init__(self, repo):
        self.repo = repo

    def cadastrar_livro(self, isbn, titulo, autor):
        if not isbn:
            raise LivroInvalido("ISBN é obrigatório")
        self.repo.livros[isbn] = Livro(isbn, titulo, autor)