from whiteboard import solution
from unittest import TestCase


class TestWhiteboard(TestCase):

    def test_1(self):
        self.assertEqual(solution([1, 2, 3, 4]), 3)

    def test_2(self):
        self.assertEqual(solution([1, 2, 3, -4]), 7)

    def test_3(self):
        self.assertEqual(solution([-1, -2, -3, -4]), 3)

    def test_4(self):
        self.assertEqual(solution([5]), 0)

    def test_5(self):
        self.assertEqual(solution([]), 0)