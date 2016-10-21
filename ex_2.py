#!/usr/bin/env python3
from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 5, 8)
data3 = ['A','a','b','v','B','A']
# Реализация задания 2

print(list(Unique(data1)))
print(list(Unique(list(data2))))
print(list(Unique(data3, ignore_case=True)))