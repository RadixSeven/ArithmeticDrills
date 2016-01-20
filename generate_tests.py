#!/usr/bin/env python3

add_min = 0
add_max = 10

class Fact:
    def __init__(self, first, operator, second):
        self.first = first
        self.operator = operator
        self.second = second
    def __repr__(self):
        return "Fact({},{},{})".format(repr(self.first),repr(self.operator),
                                       repr(self.second))
    def __str__(self):
        return "{} {} {} =".format(str(self.first), str(self.operator),
                                   str(self.second))

facts = set()

for first in range(add_min, add_max+1):
    for second in range(add_min, add_max+1):
        facts.add(Fact(first, "+", second))
        s = first + second
        facts.add(Fact(s,"-",first))
        facts.add(Fact(s,"-",second))

for f in facts:
    print(str(f))
    print(repr(f))
