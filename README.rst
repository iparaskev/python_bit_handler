==================
python-bit-handler
==================


A small python module for handling bits in registers with hardware interfaces communication libraries.


* Free software: MIT license

Overview
--------

python_bit_handler is a small module that can be added to any driver that is 
written for sensors/effectors that require handling of specific bits/bytes of
registers through a hardware interface like spi or i2c.

Features
--------

- Initialization of handler.

  .. code:: python

    handler = BitHandler(resolution=8)
    
- Set any bits to any variable 

  .. code:: python

    number = 0b10101100
    number = handler.set_bits(number, 0b111, bits=3, shift=1)

- Get any bits from a variable.

  .. code:: python

    number = 0b10101100
    bits = handler.get_bits(number, bits=3, shift=1)

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
