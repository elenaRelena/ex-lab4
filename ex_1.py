#!/usr/bin/env python3
from librip.gen import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': None, 'price': 800, 'color': 'white'}
]

# Реализация задания 1
print(list(field(goods,'title1')))
print(list(field(goods,'title','color')))
print(list(gen_random(1,3,5)))