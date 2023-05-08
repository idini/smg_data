import secrets
from google.cloud import bigquery
from google.oauth2 import service_account
from lib.storage.StorageManager import StorageManager


class BigqueryStorageManager(StorageManager):
    """
    Class that implements CRUD ops on Google Bigquery.

    Args:
        project_id (id): id of Bigquery project.

    Notes:
        For Business case purpose, I develop only read and write operations.
        We will assume also that tables are composed only by two columns, id and text.

    """

    def __init__(
            self,
            credential_path:str,
            project_id:str
        ) -> None:

        super().__init__()

        credentials = service_account.Credentials.from_service_account_file(credential_path)
        self.__client = bigquery.Client(credentials = credentials, project = project_id)

    def read(self, table_name:str, id:int) -> str :
        """ method used to read an item based on an id

        Args:
            table_name (str): name of table
            id (int): id of item

        Examples:
            >>> bq_manager = BigqueryStorageManager()
            >>> bq_manager.read(table_name = 'test.test_table', id = 111)
            'This is a sentence'

        Returns:
            str|None: the sentence or Nonetype

        """
        try:
            query_job = self.__client.query(f"""
                SELECT distinct id, text
                FROM {table_name}
                where id = {id}
            """)

            result = next(query_job.result())
            return result.text
        except Exception as e:
            return None


    def write(self, table_name:str, id:int, item: str) -> None:
        """ method used to write an item in a specific table

        Args:
            table_name (str): name of table
            id (int): id of item
            item (string): item

        Examples:
            >>> bq_manager = BigqueryStorageManager()
            >>> bq_manager.write(table_name = 'test.test_table', id = 111, item = 'sentence')

        """

        try:
            query_job = self.__client.query(f"""
                insert into {table_name} values ({id}, {item})
            """)
            query_job.result()
        except Exception as e:
            raise e

