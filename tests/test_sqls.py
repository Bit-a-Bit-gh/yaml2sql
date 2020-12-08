#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_example
.. moduleauthor:: Bit-a-Bit <github@bit-a-bit.info>

This is a sample test module.
"""

from os.path import exists, dirname, join 
import pytest
from yaml2sql.sqls import StatementSQL
from ruamel.yaml import YAML

"""
This is just an example test suite.  It will check the current project version
numbers against the original version numbers and will start failing as soon as
the current version numbers change.
"""


def test_StatementsSQL_init():
    """
    Arrange: Instantiate StatementSQL class with example.yaml
    Act: Open the file.
    Assert: self.datamodel is not null.
    """
    yaml = YAML(typ='safe')
    with open(join(dirname(__file__), 'example.yaml')) as f:
        ssql = StatementSQL(f)
    print(ssql.datamodel)
    assert (
        not ssql.datamodel is None
    )


@pytest.mark.parametrize("a,b,c", [(1, 2, 5), (3, 4, 25)])
def test_ab_addSquares_equalsC(a, b, c):
    """
    Arrange: Acquire the first two parameters (a and b).
    Act: Add the squares of the first two parameters (a and b).
    Assert: The sum of the squares equals the third parameter (c).

    :param a: the first parameter
    :param b: the second parameter
    :param c: the result of adding the squares of a and b
    """
    assert (
        a * a + b * b == c,
        "'c' should be the sum of the squares of 'a' and 'b'. "
        "This is an example test and can be removed.",
    )
