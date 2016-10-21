# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        #self.ignore_case = False
        self.items = iter(items) if isinstance(items, list) else items
        self.num = 0
        self.fl=False
        self.unique=[]
        if (kwargs.get('ignore_case')==True):
           #self.items=[str(it).lower() for it in items]
           self.fl=True
    
    def __next__(self):
        # Нужно реализовать __next__ 
        for it in self.items:
            if (self.fl==True and type(it)!=int):  
                if (it.lower() not in self.unique):
                    buf=str(it).lower()
                    self.unique.append(str(buf))
                    return it
            else:
                if (it not in self.unique):
                    self.unique.append(it)
                    return it
        raise StopIteration()


    def __iter__(self):
        return self
