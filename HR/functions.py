#! /usr/bin/env python3
# Author : Vidhi Panda <vidhimpanda@gmail.com>
# Functions in python


def IsLeap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    return leap


def main():
    year = int(input())
    if IsLeap(year):
        print('Leap')
    else:
        print('Not Leap')


if __name__ == '__main__':
    main()
