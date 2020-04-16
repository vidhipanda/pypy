#! /usr/bin/env python3
# Author : Vidhi Panda <vidhimpanda@gmail.com>
# List Comprehensions in python


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                sum = i+j+k
                if sum != n:
                    l.append([i, j, k])
    print(l)


if __name__ == '__main__':
    main()
