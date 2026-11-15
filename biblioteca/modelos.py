from dataclasses import dataclass


@dataclass
class Livro:
    isbn: str
    titulo: str
    autor: str
    disponivel: bool = True


@dataclass
class Usuario:
    nome: str
    email: str
    bloqueado: bool = False


@dataclass
class Emprestimo:
    livro: Livro
    usuario: Usuario
    ativo: bool = True
