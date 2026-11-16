from biblioteca.modelos import Livro

class Acervo:
    def __init__(self, repo):
        self.repo = repo

    def cadastrar_livro(self, isbn, titulo, autor):
        self.repo.livros[isbn] = Livro(isbn, titulo, autor)