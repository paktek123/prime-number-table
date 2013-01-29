#!/usr/bin/env python
# -*- coding: utf8 -*-

def prime_number_check(number, prime_list):
    """
    Function to check if number is prime and to update prime list
    """
    for prime in prime_list:
        # check if number is not already in list or does not return a remainder
        if not (number == prime or number % prime):
            return False

    # Update the list if number is prime
    prime_list.append(number)

    return number

def prime_list(limit):
    """
    Function to return prime numbers and limit them
    """
    # Add 2 as first prime number
    prime_list = [2,]

    # Variables to help count and limit prime numbers
    start, prime_counter = 2, 0

    # Start infinite loop
    while True:

        # Check if number is a prime number
        if prime_number_check(start, prime_list):
            # Increment number for counting primes
            prime_counter += 1

            # If prime_counter reaches limit return primes
            if prime_counter == limit:
                # set() used to remove duplicates
                return set(prime_list)

        # Next number to be checked for prime number in loop
        start += 1

def process_prime_list(prime_numbers):
    """
    Process the prime numbers list to populate table and print output
    """
    # Add 1 as first element in list
    prime_numbers.insert(0, 1)

    table = []

    # Add the first row and prime numbers as column headers
    table.append(prime_numbers)

    # Iterate over column numbers (without 1)
    for number in prime_numbers[1:]:
        row = []
        # Iterate over column prime numbers
        for column in prime_numbers:
            # Add the products to the row
            row.append(number*column)

        # Populate the table with the row
        table.append(row)

    # Add 'X' in the corner of table
    table[0][0] = 'X'

    # Add split for heading
    width = len(table[0])
    table.insert(1, ['-' for x in range(1,width)])
    height = len(table)
    for row in table:
        row.insert(1, '|')

    # Pretty print table
    for row in table:
        print ' '.join(map(str, [str(element).rjust(6,' ') for element in row]))

if __name__ == '__main__':
    # Get limit of prime numbers for user input
    prime_limit = int(input('Please enter the first n prime numbers you would like to see: '))
    # Get list of prime numbers depending on the limit
    prime_numbers = list(prime_list(prime_limit))
    # Show table
    process_prime_list(prime_numbers)
