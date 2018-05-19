#!/usr/bin/env python

from parser import parse_formula

MOLECULES = (
    ('Water', 'H2O'),
    ('Magnesium hydroxyde', 'Mg(OH)2'),
    ('Fremy salt', 'K4[ON(SO3)2]2'),
    ('Hemoglobin', 'C2952H4664O832N812S8Fe4'),
    ("Alien's breath", 'C43(H21He43[C6Hg999]{Si2[Na[Mo1]1]}42Au3)5{{D5}}'),
)


def pprint(s):
    print(s, '>>>', parse_formula(s))


if __name__ == '__main__':

    for name, formula in MOLECULES:
        pprint(formula)
