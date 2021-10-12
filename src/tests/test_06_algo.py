import pytest
import unittest
from module_one._06_algos import *

tc = unittest.TestCase()


def test_gcd():
    
    with tc.assertRaises(ValueError):
        gcd(0,0)

    res = gcd(0, 1)
    assert res == 1

    res = gcd(1,0)
    assert res == 1

    res = gcd(10,20)
    assert res == 10

    res = gcd(20,10)
    assert res == 10

    res = gcd(23,19)
    assert res == 1

    res = gcd(23,46)
    assert res == 23

    res = gcd(23,23)
    assert res == 23

def test_prime_below():
    
    with tc.assertRaises(ValueError):
        primes_below(1)

    res = primes_below(2)
    assert res == [2]

    res = primes_below(8)
    assert res == [2,3,5,7]


def test_sum_of_even_fibonacci_number_for_nth_term():

    res = sum_of_even_fibonacci_number_for_nth_term(2)
    assert res == 2

    res = sum_of_even_fibonacci_number_for_nth_term(10)
    assert res == 44

    res = sum_of_even_fibonacci_number_for_nth_term(1)
    assert res == 0

def test_two_sum():

    res = two_sum([1,2,3,1], 2)
    assert res == [0,3]

    res = two_sum([3,2,3], 6)
    assert res == [0,2]

def test_reverse():
    
    res = reverse(126)
    assert res == 621

    res = reverse(110)
    assert res == 11

    res = reverse(101)
    assert res == 101

    res = reverse(42)
    assert res == 24

    res = reverse(0)
    assert res == 0

    res = reverse(2147483647)
    assert res == 0