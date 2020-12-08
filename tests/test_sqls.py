#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_sqls
.. moduleauthor:: Bit-a-Bit <github@bit-a-bit.info>

Tests sqls module.
"""

from os.path import exists, dirname, join 
import pytest
from yaml2sql.sqls import StatementSQL
from ruamel.yaml import YAML


PATH_EXAMPLE_FILE = join(dirname(__file__), 'example.yaml')


def test_StatementsSQL_init():
    """
    Arrange: Instantiate StatementSQL class with example.yaml
    Act: Open the file.
    Assert: self.datamodel is not null.
    """
    yaml = YAML(typ='safe')
    with open(PATH_EXAMPLE_FILE) as f:
        ssql = StatementSQL(f)
    print(ssql.datamodel)
    assert (
        not ssql.datamodel is None,
        not ssql.create_tables is None
    )
