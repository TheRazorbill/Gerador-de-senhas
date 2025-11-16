# Gerador e Verificador de Senhas em Python


##  Sobre o Projeto
Este é um script de console (CLI) desenvolvido em Python que possui duas funções principais:
1.  **Gerar senhas aleatórias** e seguras com um comprimento definido pelo usuário.
2.  **Verificar a força de uma senha** fornecida, com base em critérios de segurança comuns.

O projeto foi criado como uma forma prática de aplicar conceitos de manipulação de strings, funções e lógica de programação em Python.

---

##  Funcionalidades
- **Geração de Senhas:** Cria senhas aleatórias utilizando uma combinação de letras maiúsculas, minúsculas, números e símbolos.
- **Verificação de Força:** Avalia se uma senha atende aos seguintes critérios para ser considerada forte:
    - ✅ Possui pelo menos uma letra minúscula.
    - ✅ Possui pelo menos uma letra maiúscula.
    - ✅ Possui pelo menos um número.
    - ✅ Possui pelo menos um caractere especial (símbolo).
    - ✅ Possui um comprimento mínimo de 8 caracteres.
- **Interface Interativa:** Um menu simples no terminal guia o usuário para escolher entre gerar ou verificar senhas.
- **Tratamento de Erros:** O script lida com entradas inválidas do usuário para evitar que o programa quebre.

---

##  Como Usar
Para executar este projeto, você precisa ter o Python instalado em sua máquina.

1.  Salve o código em um arquivo com a extensão `.py` (por exemplo, `gerador_senhas.py`).
2.  Abra um terminal ou prompt de comando.
3.  Navegue até a pasta onde você salvou o arquivo.
4.  Execute o script com o seguinte comando:
    ```bash
    python gerador_senhas.py
    ```
5.  Siga as instruções que aparecerão no terminal para gerar ou verificar suas senhas.

---

##  Estrutura do Código
O script é organizado em várias funções, cada uma com uma responsabilidade específica:

- `faz_snh(tam)`: Responsável por criar uma única senha aleatória com o tamanho (`tam`) especificado.
- `checa_snh(senha)`: Verifica se uma `senha` atende a todos os critérios de força e retorna `True` (se for forte) ou `False` (se for fraca).
- `faz_varias_snh(num, tam)`: Gera um `num` de senhas, cada uma com o `tam` especificado.
- `mostra_info(senha)`: Exibe no console o detalhamento de quais critérios de força a `senha` atende.
- `comeca()`: É a função principal que inicializa o programa, exibe o menu e controla o fluxo de interação com o usuário.

---

##  Autor
Desenvolvido por **TheRazorbill**.

![Screenshot 2025-06-15 154555](https://github.com/user-attachments/assets/15a0fd06-17f9-4392-8a6d-8e0fdbc89d11)

![Screenshot 2025-06-15 154607](https://github.com/user-attachments/assets/2e797359-9be0-4aa0-96bf-11f3c12a3512)

![Screenshot 2025-06-15 155011](https://github.com/user-attachments/assets/b5b2ee96-1843-4655-9d98-4c5a485a0306)
