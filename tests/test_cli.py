#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_cli
.. moduleauthor:: Bit-a-Bit <hola@bit-a-bit.info>

This is the test module for the project's command-line interface (CLI)
module.
"""
# fmt: off
from os.path import exists, join, dirname
from os import remove
import yaml2sql.cli as cli
from yaml2sql import __version__
# fmt: on
from click.testing import CliRunner, Result


# To learn more about testing Click applications, visit the link below.
# http://click.pocoo.org/5/testing/


PATH_EXAMPLE_FILE = join(dirname(__file__), 'example.yaml')


def test_version_displays_library_version():
    """
    Arrange/Act: Run the `version` subcommand.
    Assert: The output matches the library version.
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["version"])
    assert (
        __version__ in result.output.strip()
    ), "Version number should match library version."


def test_verbose_output():
    """
    Arrange/Act: Run the `version` subcommand with the '-v' flag.
    Assert: The output indicates verbose logging is enabled.
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["-v", "version"])
    assert (
        "Verbose" in result.output.strip()
    ), "Verbose logging should be indicated in output."

def test_create_tables_stout():
    """
    Arrange/Act: Run the `create-tables` command.
    Assert: Output to stout.
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.create_tables, [PATH_EXAMPLE_FILE])
    assert (
        'CREATE TABLE' in result.output.strip()
    )

def test_create_tables_file():
    """
    Arrange/Act: Run the `create-tables` command.
    Assert: Output to stout.
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.create_tables, [PATH_EXAMPLE_FILE, PATH_EXAMPLE_FILE + '.tmp'])
    assert (
        exists(PATH_EXAMPLE_FILE + '.tmp'),
        remove(PATH_EXAMPLE_FILE + '.tmp') is None
    )
