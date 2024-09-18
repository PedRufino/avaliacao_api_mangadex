from view.api_view import ApiView
from model.api_model import ApiModel

from typing_extensions import Literal
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ApiController:
    def __init__(self):
        self.model = ApiModel()
        self.view = ApiView()
        super().__init__()

    def process_query(
        self,
        query_type: Literal[
            "all_manga", "original_language", "available_languages", "name_manga"
        ],
        language: str = None,
        title: str = None,
    ):
        """
        Permite realizar consultas específicas e processar os resultados de acordo,
        utilizando um método dinâmico para chamar o método apropriado da instância ApiModel
        """
        logger.info("Coletando informações...")

        if query_type == "all_manga":
            data = self.model.get_all_manga()
        elif query_type == "original_language":
            data = self.model.get_original_language(language)
        elif query_type == "available_languages":
            data = self.model.get_available_languages(language)
        elif query_type == "name_manga":
            data = self.model.get_name_manga(title)
        else:
            raise Exception("Opção Invalida!")

        self.view.create_csv_data(data, query_type)
