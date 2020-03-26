# Author: Vidhi Panda <vidhimpanda@gmail.com>
# print pattern


def main():
    testcases = int(input())
    for a in range(testcases):
        n = int(input())
        for i in range(n):
            for j in range(i+1):
                print("*", end=" ")
            print()


main()
