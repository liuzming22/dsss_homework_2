import unittest
from math_quiz import get_random_integer, choose_random_operator, basic_math_operation


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_random_operator(self):
        # Test if random operator choosed is one of '+', '-', '*'.
        supported_operators = ['+','-','*']
        result = choose_random_operator()
        self.assertIn(result, supported_operators)

    def test_basic_math_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 3, '-', '6 - 3', 3),
                (5, 7, '*', '5 * 7', 35),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = basic_math_operation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                

if __name__ == "__main__":
    unittest.main()
 