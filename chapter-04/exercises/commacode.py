# commacode.py
# Date: Tuesday 8 July 2025
# Author: Brendan Gasparin <brendan.gasparin@gmail.com>
# Takes a list of strings from the user and outputs the list with commas
# and an 'and' before the final item.

import sys

def main():
    userList = []
    # Get a list of strings from the user.
    try:
        while(True):
            answer = input('Enter a list item or f to finish the list: ')
            if answer == 'f':
                break
            else:
                userList.append(answer)
    except KeyboardInterrupt:
        sys.exit()
    
    printList(userList)


def printList(thisList):
    for i in range(len(thisList) - 1):
        print(thisList[i] + ', ', end = '')
    print('and ' + thisList[-1] + '.')


if __name__ == "__main__":
    main()
