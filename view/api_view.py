import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ApiView:
    def process_item(self, item):
        """Processa um item e retorna um dicionário com os dados formatados."""
        attributes = item.get("attributes", {})
        title = next(iter(attributes.get("title", {}).values()), "Sem título")
        description = next(
            iter(attributes.get("description", {}).values()), "Sem descrição"
        )
        year = attributes.get("year", "Não disponível")
        tags = [
            tag["attributes"].get("name", {}).get("en", "Não disponível")
            for tag in attributes.get("tags", [])
            if tag["attributes"].get("group") == "genre"
        ]

        return {
            "Tipo": item.get("type", "Não disponível"),
            "ID": item.get("id", "Não disponível"),
            "Título": title,
            "Descrição": description,
            "Ano": str(year),
            "Genero": ", ".join(tags) if tags else "Não disponível",
        }

    def generate_items_list(self, generator):
        """Gera uma lista de itens processados a partir de um gerador."""
        all_items = []
        for data in generator:
            if not data:
                break

            if not data.get("data", []):
                break

            for item in data.get("data", []):

                processed_item = self.process_item(item)
                all_items.append(processed_item)

        return all_items

    def save_to_csv(self, items, name_file):
        """Salva a lista de itens em um arquivo CSV."""
        if items:
            df = pd.DataFrame(items)
            df.to_csv(f"./{name_file}.csv", index=False, sep="|", encoding="utf-8")

    def create_csv_data(self, generator, name_file: str = None):
        """Função principal para criar o arquivo CSV a partir do gerador."""
        items = self.generate_items_list(generator)
        logger.info("Realizando a criação do csv...")
        self.save_to_csv(items, name_file)
