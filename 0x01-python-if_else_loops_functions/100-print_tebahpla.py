#!/usr/bin/python3
# 100-print_tebahpla.py

"""Print the alphabet in reverse order alternating upper- and lower-case."""
q = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - q)), end="")
    q = 32 if q == 0 else 0


