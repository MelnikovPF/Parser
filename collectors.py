from abc import abstractmethod
import pandas as pd


class AbstractCollector(object):
    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def save(self):
        pass


class ExcelCollector(AbstractCollector):
    def __init__(self):
        self._filename = None
        self._df = pd.DataFrame()


    def push(self):
        return
        if len(fname) > 0:
                data = pd.read_excel(fname, sheet_name=0, header=0, index_col=0, usecols="B:I", skiprows=10)
                _df = data.append(data)
        df.head()


    def save(self):
        self._df.to_excel('C:\example\example.xlsx')
