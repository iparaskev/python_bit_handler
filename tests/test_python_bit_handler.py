#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_bit_handler` package."""


import unittest
from click.testing import CliRunner

from python_bit_handler import BitHandler
from python_bit_handler import cli


class TestPython_bit_handler(unittest.TestCase):
    """Tests for `python_bit_handler` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_set_bit(self):
        """Test set bits function."""

        handler = BitHandler(resolution=8)
        register_val = 0b11011001
        value = 0b1
        print("Initial value: {}\tTarget value: {}".format(bin(register_val),
                                                           bin(value)))

        max_shifts = 7
        for i in range(max_shifts):
            for j in range(1, max_shifts + 2 - i):
                new_reg_val = handler.set_bits(register_val, value, j, i)
                print("Bits: {}, Shift: {}, Value: {}".format(j, 
                                                              i,
                                                              bin(new_reg_val)))

    def test_get_bit(self):
        """Test set bits function."""

        handler = BitHandler(resolution=8)
        register_val = 0b11011001
        print("Initial value: {}".format(bin(register_val)))

        max_shifts = 7
        for i in range(max_shifts):
            for j in range(1, max_shifts + 2 - i):
                new_reg_val = handler.get_bits(register_val, j, i)
                print("Bits: {}, Shift: {}, Value: {}".format(j, 
                                                              i,
                                                              bin(new_reg_val)))
    
    def test_number(self):
        """Test get_number function."""

        handler = BitHandler(resolution=8)
        data = [0b10010101, 0b00100111, 0b11010000]
        whole_res = 0b100101010010011111010000

        res = 24

        for i in range(8):
            s = False
            number = handler.get_number(data.copy(), res=res, signed=s, rev=True)
            self.assertEqual(number, 
                             handler.get_bits(whole_res, res, i),
                             "Wrong at res {} and signed {}".format(res, s))
            res -= 1

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'python_bit_handler.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output


if __name__ == "__main__":
    unittest.main()
