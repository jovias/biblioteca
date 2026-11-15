# language: pt
Funcionalidade: Acervo de livros
  Como bibliotecária
  Quero cadastrar e buscar livros
  Para controlar o acervo da biblioteca

  Cenário: Cadastrar livro com sucesso
    Dado que o acervo está vazio
    Quando eu cadastrar o livro "Dom Casmurro" com ISBN "111"
    Então o acervo deve ter 1 livro

  Cenário: Recusar ISBN repetido
    Dado que o livro "Dom Casmurro" com ISBN "111" está cadastrado
    Quando eu cadastrar o livro "Outro livro" com ISBN "111"
    Então o cadastro deve ser recusado com a mensagem "ISBN já cadastrado"

  Cenário: Buscar livro por parte do título
    Dado que o livro "Dom Casmurro" com ISBN "111" está cadastrado
    Quando eu buscar por "casmurro"
    Então o resultado deve conter o livro "Dom Casmurro"

  Cenário: Busca sem resultado
    Dado que o livro "Dom Casmurro" com ISBN "111" está cadastrado
    Quando eu buscar por "Iracema"
    Então o resultado deve estar vazio
