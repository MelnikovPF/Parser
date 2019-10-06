from abc import abstractmethod
from typing import Iterable
from glob import glob


class AbstractSource(object):
    @abstractmethod
    def pull(self):
        pass


class ExcelFiles(AbstractSource):
    def __init__(self, source: Iterable[str]):
        self._source = source


    def pull(self):
        return glob(self._source, recursive=True)