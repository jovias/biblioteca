class Repositorio:
    """Guarda todos os dados em memória. Compartilhado por todos os módulos."""

    def __init__(self):
        self.livros = {}        # isbn -> Livro
        self.usuarios = {}      # email -> Usuario
        self.emprestimos = []   # lista de Emprestimo
        self.multas = {}        # email -> valor devido (float)
        self.avaliacoes = {}    # isbn -> lista de notas (int)
