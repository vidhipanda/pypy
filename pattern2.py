# Author: Vidhi Panda <vidhimpanda@gmail.com>
# print pattern


def main():
    testcases = int(input())
    for a in range(testcases):
        n = int(input())
        spaces = int(n/2)
        if n % 2 == 0:
            spaces = int(n/2) - 1
        for i in range(1, n+1, 2):
            # spaces
            for k in range(spaces):
                print(" ", end=" ")
            spaces -= 1
            for j in range(i):
                print("*", end=" ")
            print()


main()
