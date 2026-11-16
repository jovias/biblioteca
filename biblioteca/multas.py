PRAZO_DIAS = 14
VALOR_POR_DIA = 2.0


class ServicoMultas:
    def __init__(self, repo):
        self.repo = repo

    def calcular_multa(self, email, dias_com_livro):
        dias_atraso = max(0, dias_com_livro - PRAZO_DIAS)
        valor = dias_atraso * VALOR_POR_DIA
        if valor > 0:
            self.repo.multas[email] = valor
            self.repo.usuarios[email].bloqueado = True
        return valor

    def pagar_multa(self, email):
        pass
