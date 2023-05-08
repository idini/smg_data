from lib.dataencryption.DataEncryptor import DataEncryptor
from lib.storage.FakeStorageManager import FakeStorageManager
from lib.cipher.Rot13Cipher import Rot13Cipher


class TestDataEncryptor():

    @classmethod
    def setup_class (cls):
        """ """
        cls.storage_manager = FakeStorageManager()
        cls.cipher = Rot13Cipher()

    @classmethod
    def teardown_class (cls):
        """ """
        del cls.storage_manager
        del cls.cipher

    ### Method setup/teardown

    def setup_method (self):
        """ """
        self.data_encryptor = DataEncryptor(
            storage_manager = self.storage_manager,
            cipher = self.cipher
        )

    def teardown_method(self):
        """ """
        del self.data_encryptor

    ### Tests

    def test_read_sentence (self):

        sentence_id = 16793

        expected_result = {
            'id' : sentence_id,
            'text': 'Adriana Lima',
            'ciphered_text': 'Nqevnan Yvzn'
        }

        result = self.data_encryptor.read_sentence(sentence_id)

        assert (result == expected_result)

    def test_write_sentence (self):

        sentence = 'Adriana Lima'
        id = 2000001

        expected_result = {
            'id' : id,
            'text': sentence,
            'ciphered_text': 'Nqevnan Yvzn'
        }

        result = self.data_encryptor.write_sentence(id, sentence)

        assert (result == expected_result)