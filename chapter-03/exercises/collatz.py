# collatz.py
# Date: Saturday 5th July 2025
# Author: Brendan Gasparin <brendan.gasparin@gmail.com>
# Prompts user for a positive integer and runs it through the Collatz sequence.


import sys

def main():
    answer = 'Alphabetical'
    while not str(answer).isnumeric():
        print('Enter an integer greater than zero:')
        try:
            answer = int(input())
        except ValueError:
            print("You must enter an integer greater than zero.")
        else:
            if (answer <= 0):
                answer = 'Negative'

    while answer != 1:
        answer = collatz(answer)


def collatz(number):
    if (number % 2 == 0):
        collatzed = number // 2
        print(collatzed)
        return collatzed
    else:
        collatzed = 3 * number + 1
        print(collatzed)
        return collatzed


main()
