from types import GeneratorType
# Итератор для удаления дубликатов
class Unique(object):
    IGNORE_CASE = False
    INDEX = 0
    OBJECTS = []
    PUSTOTA = []

    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, то Aбв и АБВ разные строки
        #           ignore_case = False, то Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False(то есть регистры важны)
        if 'ignore_case' in kwargs.keys():
            self.IGNORE_CASE = kwargs['ignore_case']
        if type(items == GeneratorType):
            self.OBJECTS = list(items)
        else:
            self.OBJECTS = items
        # self.ITEMS = len(items)

    def __next__(self):
        while True:  
            if self.INDEX == (len(self.OBJECTS) - 1):
                raise StopIteration
            self.INDEX += 1

            val = self.OBJECTS[self.INDEX]
            val2 = str(val).lower()
            if self.IGNORE_CASE:
                val = val2
            if val not in self.PUSTOTA:
                self.PUSTOTA.append(val)
                return val

    def __iter__(self):
        del self.PUSTOTA[:]
        self.INDEX = -1
        return self
