
# Программа обращатся к справочнику 2Gis, забирает данные, перегоняет в табличный вид и возвращает файл в формате *.xlsx
# Шаг 1. Программа выходит в сеть или идет в указанную папку, в случае обработки Excel

# (здесь в интерфейсе возможен диалог с выбором файла или папки, где ищется файл)
# Шаг 2. Каким-то образом программа получает доступ к веб ресурсу или скачивает файл
# (в случае если мы забираем csv с сайта)
# Шаг 3. Происходит забор данных (скачивание файла или базы)
# Шаг 4. Чтение полученных данных
# Шаг 5. Извлечение данных и их обработка, для того чтобы массив данных структурировать под те классы что были описаны
# Здесь, видимо, ищется информация и размещается в структуре
# Шаг 6. Перегон данных в нужный формат
# Шаг 7. Сбор файла в том же формате Excel и выгрузка его

from dataclasses import dataclass


@dataclass
# Класс Company, содержит информацию об организации
class Company:
    region: str
    city: str
    name: str
    inn: int
    type: str
    industry: str
    address: str
    phone: str
    site: str
    facebook: str
    vkontakte: str
    instagram: str


from math import *


@dataclass
class Point:
    x: float
    y: float
    z: float

    def to_vector(self) -> tuple:
        return self.x, self.y, self.z

    def to_json(self) -> str:
        import json
        return json.dumps({
            'x': self.x,
            'y': self.y,
        })

    def distance(self, other) -> float:
        return sqrt(
            ((other.x - self.x) ** 2) +
            ((other.y - self.y) ** 2) +
            (())
        )
