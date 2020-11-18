#! usr/bin/env python3

from ctypes import c_float, c_long, byref, POINTER, cast
from time import time
from math import sqrt


def custom_sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:

       int: Floored Square Root
    """
    s = time()
    xhalf = 0.5 * number
    x = c_float(number)
    i = cast(byref(x), POINTER(c_long)).contents.value
    i = c_long(0x5F375A86 - (i >> 1))
    x = cast(byref(i), POINTER(c_float)).contents.value

    x = x * (1.5 - xhalf * x * x)
    print(f"Took {(time() - s):.10f} custom_sqrt seconds to calculate {number}")
    return x * number


def bs_sqrt(start, end, number):
    s = time()
    if start <= end:
        mid = (start + end) // 2
        if (mid * mid) < number and ((mid + 1) * (mid + 1) > number):
            return mid
        elif mid * mid < number:
            return bs_sqrt(mid + 1, end, number)
        else:
            return bs_sqrt(start, mid - 1, number)
    print(f"Took {(time() - s):.10f} bs_sqrt seconds to calculate {number}")
    return start


def math_sqrt(number):
    s = time()
    xhalf = sqrt(number)
    print(f"Took {(time() - s):.10f} math_sqrt seconds to calculate {number}")
    return xhalf


def main():
    print("custom_sqrt")
    print("Pass" if custom_sqrt(9) == 3 else "Fail")
    print("Pass" if custom_sqrt(0) == 0 else "Fail")
    print("Pass" if custom_sqrt(16) == 4 else "Fail")
    print("Pass" if custom_sqrt(1) == 1 else "Fail")
    print("Pass" if custom_sqrt(27) == 5 else "Fail")
    print("bs_sqrt")
    print("Pass" if bs_sqrt(0, 9, 9) == 3 else "Fail")
    print("Pass" if bs_sqrt(0, 0, 0) == 0 else "Fail")
    print("Pass" if bs_sqrt(0, 16, 16) == 4 else "Fail")
    print("Pass" if bs_sqrt(0, 1, 1) == 1 else "Fail")
    print("Pass" if bs_sqrt(0, 27, 27) == 5 else "Fail")
    print("math_sqrt")
    print("Pass" if math_sqrt(9) == 3 else "Fail")
    print("Pass" if math_sqrt(0) == 0 else "Fail")
    print("Pass" if math_sqrt(16) == 4 else "Fail")
    print("Pass" if math_sqrt(1) == 1 else "Fail")
    print("Pass" if math_sqrt(27) == 5 else "Fail")


if __name__ == "__main__":
    main()
