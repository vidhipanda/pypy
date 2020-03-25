# Author: Vidhi Panda <vidhimpanda@gmail.com>
# First n fibonacci numbers

# The Main function


def main():
    testcases = int(input())
    for i in range(testcases):
        n = int(input())
        a = 0
        b = 1
        if n >= 1:
            print(a)
        if n >= 2:
            print(b)
        if n >= 3:
            for j in range(n-2):
                c = a + b
                a = b
                b = c
                print(c)


main()
