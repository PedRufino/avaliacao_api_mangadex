# Avaliacao API MangaDex
Este projeto inclui a avaliação proposta pelo professor Orlando, com o objetivo de realizar o consumo de uma API.

## Funcionalidades

- **Coleta de todas as informações:** Recupere todos os dados disponíveis dos mangás.
  - Exemplo de uso:
    ```python
    client.process_query("all_manga")
    ```

- **Busca pela linguagem original:** Filtre os mangás pela sua língua original, como inglês, russo ou espanhol.
  - Linguagens suportadas: `en`, `ru`, `es`
  - Exemplo de uso:
    ```python
    client.process_query("original_language", language='pt-br')
    ```

- **Busca pela linguagem disponível:** Filtre os mangás pelas línguas disponíveis para leitura.
  - Linguagens suportadas: `en`, `ru`, `es`
  - Exemplo de uso:
    ```python
    client.process_query("available_languages", language='pt-br')
    ```

- **Coleta de informações por título:** Obtenha detalhes sobre um mangá específico a partir de seu título.
  - Exemplos de títulos: `naruto`, `dragon ball`, `boku no hero`
  - Exemplo de uso:
    ```python
    client.process_query("title", title='naruto')
    ```

## Como utilizar

1. Clone o repositório:
    ```bash
    git clone https://github.com/PedRufino/avaliacao_api_mangadex.git
    ```

2. Acesse o diretório do projeto:
    ```bash
    cd avaliacao_api_mangadex
    ```

3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

4. Instale o projeto no modo desenvolvimento:
    ```bash
    pip install -e .
    ```

5. Execute o cliente e realize consultas conforme as funcionalidades descritas acima.
