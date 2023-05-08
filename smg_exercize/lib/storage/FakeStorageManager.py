import json
import secrets
from lib.storage.StorageManager import StorageManager

class FakeStorageManager(StorageManager):
    """
    Class that implements CRUD ops on Fake Big Data Storage (simulating CRUD ops on real DB storage like BigQuery).

    Notes:
        For Business case purpose, I develop only read and write operations.
        I use a static file inside lib in readonly mode as a storage.
        Every update of the storage will be destroyed at the end.


    """

    def __init__(self) -> None:
        """ """
        super().__init__()
        path_to_storage_file = './lib/data/sentences.json'

        self.__storage = dict()
        try:
            with open(path_to_storage_file, 'r') as f:
                for line in f.readlines():
                    json_line = json.loads(line.strip())
                    self.__storage[int(json_line['id'])] = json_line['text']

        except FileNotFoundError as err:
            print(err)

    def read(self, id: int) -> str :
        """ method used to read a record based on an id

        Args:
            id (int): id of record.

        Examples:
            >>> fake_storage = FakeStorage()
            >>> fake_storage.read(111)
            'This is a result'

        Returns:
            str|None: the result or Nonetype

        """
        return self.__storage.get(id)


    def write(self, id:int, item: str) -> None :
        """ method used to write an item inside storage

        Args:
            id (int): id of item
            item (str): item to be inserted in storage.

        Examples:
            >>> fake_storage = FakeStorage()
            >>> fake_storage.write(111, "sentence")

        Notes:
            The id of the new item is generated TODO

        """
        if id in self.__storage:
            raise Exception("Id already in the storage")
        self.__storage[id] = item

