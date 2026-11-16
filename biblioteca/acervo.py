from biblioteca.modelos import Livro

class LivroInvalido(Exception):
    pass

class LivroDuplicado(Exception):
    pass

class Acervo:
    def __init__(self, repo):
        self.repo = repo

    def cadastrar_livro(self, isbn, titulo, autor):
        if not isbn:
            raise LivroInvalido("ISBN é obrigatório")
        if isbn in self.repo.livros:
            raise LivroDuplicado("ISBN já cadastrado")
        self.repo.livros[isbn] = Livro(isbn, titulo, autor)