import pytest
from biblioteca.repositorio import Repositorio
from biblioteca.avaliacoes import ServicoAvaliacoes, NotaInvalida


def test_avaliar_livro_guarda_nota():
    repo = Repositorio()
    servico = ServicoAvaliacoes(repo)

    servico.avaliar("111", 5)

    assert repo.avaliacoes["111"] == [5]

def test_nao_aceita_nota_acima_de_5():
    repo = Repositorio()
    servico = ServicoAvaliacoes(repo)

    with pytest.raises(NotaInvalida, match="A nota deve ser de 1 a 5"):
        servico.avaliar("111", 6)
