from sources import *
from collectors import *


class ExcelParser(object):
    def __init__(self, source: AbstractSource, collector: AbstractCollector):
        self._source = source
        self._collector = collector

    def start(self):
        for num, fname in enumerate(self._source, start=1):
            self._collector.push(print("File # {} | {}".format(num, fname)))
