
from biblioteca.repositorio import Repositorio
from biblioteca.avaliacoes import ServicoAvaliacoes


def test_avaliar_livro_guarda_nota():
    repo = Repositorio()
    servico = ServicoAvaliacoes(repo)

    servico.avaliar("111", 5)

    assert repo.avaliacoes["111"] == [5]
