from controller.api_controller import ApiController


def main():
    client = ApiController()

    # Coleta todas as informações
    # client.process_query("all_manga")

    # Pusca pela linguagem original
    # linguagens: en, ru, es
    # client.process_query("original_language", language='pt-br')

    # Busca pela linguagem disponivel
    # linguagens: en, ru, es
    # client.process_query("available_languages", language='pt-br')

    # Coleta as informações referente ao titulo passado
    # titles: naruto, dragon ball, boku no hero
    client.process_query("name_manga", title="boku no hero")


if __name__ == "__main__":
    main()
