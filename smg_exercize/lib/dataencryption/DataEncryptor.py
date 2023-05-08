from lib.storage.StorageManager import StorageManager
from lib.cipher.Rot13Cipher import Rot13Cipher


class DataEncryptor(object):
    """
    This class is used from API to read and write sentences

    Args:
        storage_manager (StorageManager): the StorageManager object.
        cipher (Rot13Cipher): the Rot13Cipher used.

    """

    def __init__(
            self,
            storage_manager:StorageManager,
            cipher: Rot13Cipher
        ) -> None:

        self.__storage_manager = storage_manager
        self.__cipher          = cipher

    def read_sentence(self, sentence_id:int):
        """
        method used to read a sentence based on a sentence_id

        Args:
            sentence_id (int): id of item

        Returns:
            str|None: the result follow the schema `SentenceWithCypher`, i.e.::
            {
                'id': 10,
                'text': 'super movie title',
                'ciphered_text': 'fhcre zbivr gvgyr'
            }
            or Nonetype
        """

        text = self.__storage_manager.read(id = sentence_id)
        if not text:
            return None
        ciphered_text = self.__cipher.encrypt(text)

        result = dict()

        result['id'] = sentence_id
        result['text'] = text
        result['ciphered_text'] = ciphered_text

        return result

    def write_sentence(self, sentence_id: int, sentence:str) -> dict:
        """
        method used to write a sentence in the storage

        Args:
            sentence_id (int): id of sentence
            sentence (srt): sentence

        Returns:
            str|None: the result follow the schema `SentenceWithCypher`, i.e.::
            {
                'id': 10,
                'text': 'super movie title',
                'cyphered_text': 'fhcre zbivr gvgyr'
            }
            or Nonetype
        """
        try:
            self.__storage_manager.write(id = sentence_id, item = sentence)
            ciphered_text = self.__cipher.encrypt(sentence)

            result = dict()

            result['id'] = sentence_id
            result['text'] = sentence
            result['ciphered_text'] = ciphered_text

            return result
        except Exception as e:
            print(e)
            return None
