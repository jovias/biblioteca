
# language: pt

Funcionalidade: Empréstimos de livros
  Como usuário da biblioteca
  Quero emprestar e devolver livros
  Para utilizar o acervo disponível

  Cenário: Emprestar livro disponível
    Dado que o livro "Dom Casmurro" está disponível
    E que a usuária "Ana" não possui empréstimos
    Quando Ana pegar o livro "Dom Casmurro" emprestado
    Então o empréstimo deve ser registrado
    E o livro "Dom Casmurro" deve ficar indisponível

  Cenário: Recusar empréstimo acima do limite
    Dado que a usuária "Ana" possui 3 livros emprestados
    Quando Ana tentar pegar o livro "Dom Casmurro" emprestado
    Então o empréstimo deve ser recusado
    E deve aparecer a mensagem "Limite de 3 empréstimos atingido"

  Cenário: Recusar empréstimo para usuário bloqueado
    Dado que a usuária "Ana" está bloqueada
    Quando Ana tentar pegar o livro "Dom Casmurro" emprestado
    Então o empréstimo deve ser recusado

  Cenário: Recusar empréstimo de livro indisponível
    Dado que o livro "Dom Casmurro" já está emprestado
    Quando Ana tentar pegar o livro "Dom Casmurro" emprestado
    Então o empréstimo deve ser recusado

  Cenário: Devolver livro emprestado
    Dado que o livro "Dom Casmurro" está emprestado para Ana
    Quando Ana devolver o livro "Dom Casmurro"
    Então a devolução deve ser registrada
    E o livro "Dom Casmurro" deve ficar disponível

  Cenário: Recusar devolução de livro não emprestado
    Dado que o livro "Dom Casmurro" não está emprestado
    Quando Ana tentar devolver o livro "Dom Casmurro"
    Então a devolução deve ser recusada
