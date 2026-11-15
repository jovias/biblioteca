# language: pt
Funcionalidade: Multas por atraso
  Como bibliotecária
  Quero cobrar multa de quem atrasa a devolução
  Para que os livros voltem no prazo

  Contexto:
    Dado que a usuária "ana@email.com" está cadastrada

  Cenário: Devolução dentro do prazo
    Quando a usuária "ana@email.com" devolver um livro após 10 dias
    Então a multa deve ser de 0.0 reais

  Cenário: Devolução com atraso
    Quando a usuária "ana@email.com" devolver um livro após 16 dias
    Então a multa deve ser de 4.0 reais
    E a usuária "ana@email.com" deve estar bloqueada

  Cenário: Pagar multa desbloqueia a usuária
    Dado que a usuária "ana@email.com" tem uma multa por 16 dias com o livro
    Quando a usuária "ana@email.com" pagar a multa
    Então a usuária "ana@email.com" não deve ter multa pendente
    E a usuária "ana@email.com" não deve estar bloqueada

  Cenário: Recusar pagamento sem multa
    Quando a usuária "ana@email.com" pagar a multa
    Então o pagamento deve ser recusado com a mensagem "Não há multa pendente"
