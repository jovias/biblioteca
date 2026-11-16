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
        livro = Livro(isbn, titulo, autor)
        self.repo.livros[isbn] = livro
        return livro

    def buscar_por_titulo(self, texto):
        return []