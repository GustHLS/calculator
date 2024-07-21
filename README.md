## Criação de um app desktop em Python com interface gráfica.
<hr>

- Versão 0.0.1
  - Criação da interface gráfica com PyQt6 e QT Designer.


- Versão 0.0.2
  - Criação do arquivo `requirements.txt` com `pip freeze > requirements.txt`.
  - Download das bibliotecas utilizando `pip3 install -r requirements.txt`.
  - Adicionada a função para os botões:
    - Número: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
    - Operações: +, -, +/-, *, /, =, 1/x, x^2, sqt(x), %.
    - Display: Deletar, apagar.


- Versão 0.0.3
  - Inicío do script que modifica o tamanho do texto display de acordo com a quantidade de caracteres. Ainda estou tentando finalizar.
  - Adicionado o limite de caracteres ao campo de texto.
  - Tipo do campo de texto modificado de QTextEdit para QLineEdit.
  - Adicionada a verificação que, se o dígito anterior for 0, remove-o e adiciona o novo número.
  - Função fatorial adicionada.
  - Design da interface modificada. Agora, apresenta cores de base azul escuro e botão de = vermelho.