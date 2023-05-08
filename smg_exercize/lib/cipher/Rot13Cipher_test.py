from lib.cipher.Rot13Cipher import Rot13Cipher

class TestRot13Cipher():
    """
    Test class for Rot13Cipher.
    Useless since in Rot13Cipher class we use Python Standard Library codecs class.
    It's here only for exercise.
    """
    @classmethod
    def setup_class (cls):
        """ """
        pass

    @classmethod
    def teardown_class (cls):
        """ """
        pass

    ### Method setup/teardown

    def setup_method (self):
        """ """
        self.rot13_cipher = Rot13Cipher()

    def teardown_method(self):
        """ """

        del self.rot13_cipher

    ### Tests

    def test_encrypt (self):

        test_sentence = "SentenCe ExamPle"

        expected_sentence = "FragraPr RknzCyr"

        result = self.rot13_cipher.encrypt(test_sentence)

        assert (result == expected_sentence)


    def test_decrypt (self):

        test_sentence = "FragraPr RknzCyr"

        expected_sentence = "SentenCe ExamPle"

        result = self.rot13_cipher.decrypt(test_sentence)

        assert (result == expected_sentence)
