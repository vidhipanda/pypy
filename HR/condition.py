#! /usr/bin/env python3
# Author : Vidhi Panda <vidhimpanda@gmail.com>
# If-Else in python


def main():
    n = int(input())
    if n % 2 != 0:
        print('Weird')
    else:
        if n >= 2 and n <= 5:
            print('Not Weird')
        elif n >= 6 and n <= 20:
            print('Weird')
        else:
            print('Not Weird')


main()
