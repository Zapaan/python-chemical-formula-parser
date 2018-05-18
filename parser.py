#!/usr/bin/env python

import re
from collections import Counter


ATOM_REGEX = '([A-Z][a-z]*)(\d*)'
OPENERS = '({['
CLOSERS = ')}]'


def dictify(tuples):
    """Transform tuples of tuples to a dict of atoms."""
    res = dict()
    for atom, n in tuples:
        try:
            res[atom] += int(n or 1)
        except KeyError:
            res[atom] = int(n or 1)
    return res


def is_balanced(formula):
    """Check if all sort of brackets come in pairs."""
    # Very naive check, just here because you always need some input checking
    c = Counter(formula)
    return c['['] == c[']'] and c['{'] == c['}'] and c['('] == c[')']


def fuse(mol1, mol2, w=1):
    """
    Fuse 2 dicts representing molecules. Return a new dict.

    This fusion does not follow the laws of physics.
    """
    return {atom: (mol1.get(atom, 0) + mol2.get(atom, 0)) * w for atom in set(mol1) | set(mol2)}


def parse(formula, check_balance=True):
    if check_balance and not is_balanced(formula):
        raise ValueError("Watch your brackets ![{]$[&?)]}!]")

    q = []
    mol = {}
    i = 0

    while i in range(len(formula)):
        # Using a classic loop allow for manipulating the cursor
        token = formula[i]

        if token in CLOSERS:
            m = re.match('\d+', formula[i+1:])
            if m:
                weight = int(m.group(0))
                i += len(m.group(0))
            else:
                weight = 1

            submol = dictify(re.findall(ATOM_REGEX, ''.join(q)))
            return fuse(mol, submol, weight), i

        elif token in OPENERS:
            submol, l = parse(formula[i+1:], False)
            mol = fuse(mol, submol)
            # skip the already read submol
            i += l + 1
        else:
            q.append(token)
        i+=1

    # Fuse in all that's left at base level
    return fuse(mol, dictify(re.findall(ATOM_REGEX, ''.join(q)))), i


if __name__ == '__main__':
    print(parse('H2O'))
    print(parse('Mg(OH)2'))
    print(parse('K4[ON(SO3)2]2'))
