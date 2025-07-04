def main():
    print('Enter number:')
    answer = int(input())

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
