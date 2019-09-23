# -*- coding: utf-8 -*-

"""Main module."""


class BitHandler():
    """A module for handling bits in/from registers.

    It's purpose is to be used with some hardware communication library like
    spidev or smbus2 and abstract the handling of various bits from registers.

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

    def get_number(self, data, res, signed=False, rev=False):
        """From a list with raw bytes make a number.

        For example data is [10100101, 11110000, 10100000] and the bits we want
        are the first 16 and just the first three of the last one. The result
        would be 1010010111110000101.

        Args:
            data: A list with the raw bytes.
            res: The bit resolution of the target number.
            signed: If the number is signed must be True.
            rev: If the msb is in the first entry must be True.

        Return:
            An integer of resolution res.
        """

        # Raise exception if data list has more entries than the needed.
        if len(data)*self._resolution - res >= self._resolution:
            raise Exception("No need for last entry of data.")

        # Make it a list if it is one element
        data = data if isinstance(data, list) else [data]
        
        # Reverse it
        if rev:
            data.reverse()

        # Find the bit number of the lsb
        low_res = res % self._resolution
        low_res = low_res if low_res else self._resolution

        # Get only the bits of interest
        data[0] = self.get_bits(data[0], low_res, self._resolution - low_res)

        # Compute the whole number from spare bytes
        num = data[0]
        for (i, d) in enumerate(data[1:], start=1):
            num += d << (i*self._resolution - (self._resolution-low_res))

        power = res - 1
        whole = 2**(power+1) - 1
        if signed:
            num = num if num < (2**power - 1) else -((whole ^ num) + 1)

        return num
