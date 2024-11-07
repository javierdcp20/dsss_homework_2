import unittest
from math_quiz import generate_random_integer, choose_operator, create_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_operator(self):
        # Test if the operator is one of the allowed operators
        allowed_operators = ['+', '-', '*']
        for _ in range(100):  # Check multiple times to ensure randomness
            operator = choose_operator()
            self.assertIn(operator, allowed_operators)

    def test_create_problem(self):
        # Test cases for create_problem function
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()

