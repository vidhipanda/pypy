# Author: Vidhi Panda <vidhimpanda@gmail.com>
# Check divisbility


def main():
    n = int(input())
    if n % 4 == 0 and n % 6 == 0:
        print('hey there')
    elif n % 4 == 0:
        print('hey')
    elif n % 6 == 0:
        print('there')
    else:
        print('bleh')


main()
