# Author: Vidhi Panda <vidhimpanda@gmail.com>
# Armstrong number

# The Main function


def main():
    testcases = int(input())
    for i in range(testcases):
        n = int(input())
        temp = n
        s = 0
        while n > 0:
            n1 = n % 10
            s += n1 * n1 * n1
            n = int(n/10)
            print(n)
        print("Sum and temp ", s, temp)
        if s == temp:
            print("Armstrong")
        else:
            print("Not Armstrong")


main()
