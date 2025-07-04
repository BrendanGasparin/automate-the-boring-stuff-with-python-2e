import sys

def main():
    print('Enter number:')
    try:
        answer = int(input())
    except ValueError:
        print("You must enter an integer.")
        sys.exit()

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
