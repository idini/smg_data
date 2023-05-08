import codecs

class Rot13Cipher(object):
    """
    Cipher Class that uses ROT13 algorithm from Python Standard Library Codecs.
    """

    def __init__(self) -> None:
        """ """
        pass

    def encrypt(self, sentence: str) -> str :
        """ method used for encrypt a sentence

        Args:
            sentence (str): sentence to be encrypted

        Examples:
            >>> rot_cipher = Rot13Cipher()
            >>> rot_cipher.encrypt("example")
            'rknzcyr'

        Returns:
            str: the sentence encrypted.

        """
        return codecs.encode(obj = sentence, encoding = 'rot_13')


    def decrypt(self, sentence: str) -> str :
        """ method used for decrypt a sentence

        Args:
            sentence (str): sentence to be decrypted

        Examples:
            >>> rot_cipher = Rot13Cipher()
            >>> rot_cipher.decrypt("rknzcyr")
            'example'

        Returns:
            str: the sentence decrypted.

        """
        return codecs.decode(obj = sentence, encoding = 'rot_13')