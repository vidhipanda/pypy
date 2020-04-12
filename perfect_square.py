# Author: Vidhi Panda <vidhimpanda@gmail.com>
# Find perfect Squares


def main():
    n = int(input())
    l = []
    for i in range(1, n+1):
        if n % i == 0:
            l.append(i)
    if len(l) % 2 == 0:
        print('Not a perfect square')
    else:
        print('Perfect Square')


main()
