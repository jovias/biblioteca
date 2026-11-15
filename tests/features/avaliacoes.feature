
# language: pt
Funcionalidade: Avaliação de livros
  Como leitora da biblioteca
  Quero dar nota aos livros que li
  Para ajudar outras pessoas a escolher o que ler

  Contexto:
    Dado que o livro "Dom Casmurro" com ISBN "111" está cadastrado

  Cenário: Avaliar livro com nota válida
    Quando eu avaliar o livro "111" com nota 5
    Então a média do livro "111" deve ser 5.0

  Cenário: Recusar nota fora da faixa
    Quando eu avaliar o livro "111" com nota 6
    Então a avaliação deve ser recusada com a mensagem "A nota deve ser de 1 a 5"

  Cenário: Livro sem avaliações
    Então a média do livro "111" deve ser 0.0

  Cenário: Média de várias avaliações
    Quando eu avaliar o livro "111" com nota 5
    E eu avaliar o livro "111" com nota 4
    E eu avaliar o livro "111" com nota 4
    Então a média do livro "111" deve ser 4.3
