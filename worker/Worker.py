from abc import abstractmethod, ABCMeta


class Worker(metaclass=ABCMeta):
    @abstractmethod
    def work(self, text, voice=None):
        pass
