from abc import ABC as AbstractClass, abstractmethod

class StorageManager (AbstractClass):

    def __init__ (self) -> None:
        pass

    @abstractmethod
    def  read(self, id: int) -> None:
        raise Exception(f'{self.__class__}.read() to be implemented!')

    @abstractmethod
    def write(self, id:int, item: str) -> int:
        raise Exception(f'{self.__class__}.write() to be implemented!')