from unittest import TestCase
from challenges.pystudy.advanced.tracer import Trace

__author__ = 'hseewald'


class TestTrace(TestCase):
    def test___call__(self):
        tracer = Trace()

        @tracer
        def rotate_list(l):
            """rotates a list"""
            return l[1:] + [l[0]]

        numbers = [1, 2, 3, 4]

        print(rotate_list.__doc__)
        print(rotate_list.__name__)
        numbers = rotate_list(numbers)

        assert (numbers == [2, 3, 4, 1])