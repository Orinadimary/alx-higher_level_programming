# 0-add_integer.txt

===============================
 doctest for 0-add_integer.py
===============================

This module defines an integer addition function ``add_integer(a, b=98)``.

Usage
=====

``add_integer(...)``` returns the addition of its two arguments. For numbers,
that value is equivalent to using the ``+`` operator.

``add_integer()`` expects that both arguments are either integers or floats.
If either argument is a non-integer and non-float, a TypeError is raised:

Import add_integer()
	>>> add_integer = __import__("0-add_integer").add_integer

Adding positive integer or float values
	>>> add_integer(10, 5)
	15
	>>> add_integer(10.2, 5.8)
	15

Adding one positve and one negative integers
	>>> add_integer(10, -5)
	5
	>>> add_integer(-10, 5)
	-5

Adding integer and float
	>>> add_integer(10.1, 5)
	15
	>>> add_integer(10, 5.9)
	15

Adding integer and string
	>>> add_integer(10, 'you')
	Traceback (most recent call last):
	...
	TypeError: b must be an integer
	
	>>> add_integer(10.0, 'you')
	Traceback (most recent call last):
	...
	TypeError: b must be an integer
	
	>>> add_integer('you')
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer

        >>> add_integer('you')
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer

One argument
	>>> add_integer(1)
	99

No argument
	>>> add_integer()
	Traceback (most recent call last):
	...
	TypeError: add_integer() missing 1 required positional argument: 'a'

Float overflow
	>>> add_integer(4, float("inf"))
	Traceback (most recent call last):
	...
	OverflowError: cannot convert float infinity to integer

Adding NAN
	>>> add_integer(float('NaN'))
	Traceback (most recent call last):
	...
    	ValueError: cannot convert float NaN to integer

	>>> add_integer(10, float('NaN'))
        Traceback (most recent call last):
        ...
        ValueError: cannot convert float NaN to integer
