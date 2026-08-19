Sistema de Cadastro de Usuários em Python

Esse é um projeto prático de sistema de gerenciamento de usuários via terminal (CLI) que fiz em Python. O objetivo principal foi criar um CRUD completo (Criar, Ler, Atualizar e Deletar) garantindo que os dados não se perdessem, por isso integrei com arquivos JSON.

  Sobre o desenvolvimento e aprendizado

Esse projeto nasceu de um trabalho em equipe na faculdade e foi uma experiência muito legal. Nós dividimos as tarefas, e eu fiquei responsável principalmente por montar a lógica de Atualizar e o Pesquisar do código. O restante foi feito em grupo.

Sendo bem transparente sobre o nosso processo: como estamos na fase de aprendizado, usamos ferramentas de IA (como o ChatGPT e Gemini) para nos ajudar com dúvidas chatas de sintaxe e formatar blocos de código mais rápido. Porém, entender a lógica, desenhar a arquitetura do CRUD e resolver os bugs de fluxo foi discutida e feita pelo grupo.
  
  O que o código faz na prática?

* **Cadastro:** Recebe dados completos (Nome, CPF, Data de Nascimento, E-mail, etc.).
* **Validações:** Usa regex para não deixar passar CPF ou datas em formatos errados e bloqueia CPFs duplicados.
* **Busca e Atualização:** Dá para achar o usuário pelo CPF e atualizar só o que precisa, mantendo o resto.
* **Salvamento local:** Salva tudo no arquivo `banco_dados.json`.

  O que usei para construir

* Python 3.10+ (Aproveitando a estrutura match/case pros menus)
* Bibliotecas Nativas: `json`, `re`, `os`
