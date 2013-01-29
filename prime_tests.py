import unittest
from prime import prime_number_check, prime_list, process_prime_list


class PrimeTests(unittest.TestCase):

    def test_prime_number_check_fail(self):
        result = prime_number_check(4, [2,3,4,5,6,7])
        self.assertEqual(result, False)

    def test_prime_number_check_success(self):
        result = prime_number_check(3, [2,3,4,5,6,7])
        self.assertEqual(result, 3)

    def test_prime_list_success(self):
        result = prime_list(3)
        self.assertEqual(list(result), [2,3,5])

if __name__ == '__main__':
    unittest.main(verbosity=2)
