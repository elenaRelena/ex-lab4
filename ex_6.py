#!/usr/bin/env python3
import json
import sys
import os.path
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gen import field, gen_random
from librip.iterators import Unique as unique

path = path = "data_light.json"

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path, encoding="utf8") as f:
    data = json.load(f)
    #print(type(data))


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return sorted(unique(field(arg, 'job-name'), ignore_case=True), key=lambda x: x.lower())


@print_result
def f2(arg):
    #return list(filter(lambda x: 'программист' in str(x),arg)) #все, что содержит 'программист'
    return list(filter(lambda x: str(x).startswith('Программист'),arg)) #все, что начинается с 'программист'


@print_result
def f3(arg):
    return list(map(lambda x: str(x)+' с опытом Python', arg))


@print_result
def f4(arg):
    res = gen_random(100000, 200000, len(arg))
    #return list(map(lambda x: x+', зарплата '+str(next(res)) + ' руб.', arg))
    return list(x+', зарплата '+str(next(res)) + ' руб.' for x in arg)


with timer():
    f4(f3(f2(f1(data))))