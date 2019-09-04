# -*- coding: utf-8 -*-

"""Main module."""


class BitHandler():
    """A module for handling bits in/from registers.

    It's purpose is to be used with some hardware communication library like
    spidev2 or smbus and abstract the handling of various bits from registers.

    Args:
        resolution: The resolution of the registers in bits.
    """

    def __init__(self, resolution=8):
        """Constructor."""

        self._resolution = resolution

    def set_bits(self, register_val, value, num_bits, shift):
        """Set shift bits from start of register with value.

        Args:
            register_val: The saved value of a register.
            value: The new value that will be stored in the target bits.
            num_bits: Integer indicating how many bits to set.
            shift: Integer indicating the starting bit in the number.
        """

        # Zero target bits
        max_val = 2**self._resolution - 1
        mask = ((max_val << (num_bits + shift)) | ((1 << shift) - 1)) & max_val
        register_val &= mask

        return register_val | (value << shift)

    def get_bits(self, register_val, num_bits, shift):
        """Get specific bits from register
        
        Args:
            register_val: The complete register value
            num_bits: How many bits we want.
            shift: The shift from the start.
        """
        
        mask = ((1 << num_bits) - 1) << shift

        return (register_val & mask) >> shift
