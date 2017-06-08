from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        res = solution()

        self.assertEqual(res.shape, (5,4))
