# language: pt
Funcionalidade: Cadastro e bloqueio de usuários
  Como bibliotecária
  Quero cadastrar e bloquear usuários
  Para controlar quem pode pegar livros

  Cenário: Cadastrar usuário com sucesso
    Quando eu cadastrar a usuária "Ana" com e-mail "ana@email.com"
    Então a usuária "ana@email.com" deve estar cadastrada

  Cenário: Recusar e-mail inválido
    Quando eu cadastrar a usuária "Ana" com e-mail "ana.email.com"
    Então o cadastro deve ser recusado com a mensagem "E-mail inválido"

  Cenário: Bloquear usuária
    Dado que a usuária "Ana" com e-mail "ana@email.com" está cadastrada
    Quando eu bloquear a usuária "ana@email.com"
    Então a usuária "ana@email.com" deve estar bloqueada

  Cenário: Desbloquear usuária
    Dado que a usuária "Ana" com e-mail "ana@email.com" está cadastrada
    E que a usuária "ana@email.com" está bloqueada
    Quando eu desbloquear a usuária "ana@email.com"
    Então a usuária "ana@email.com" não deve estar bloqueada