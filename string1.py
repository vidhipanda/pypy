# Author: Vidhi Panda <vidhimpanda@gmail.com>
# string handling


def isVowel(ch, arr):
    for i in arr:
        if ch == i:
            return True
    return False


def main():
    testcases = int(input())
    for a in range(testcases):
        str1 = input()
        p = 0
        if "ay" in str1:
            print(str1)
            continue
        arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for ch in str1:
            if isVowel(ch, arr):
                break
            p += 1
        print(str1[p:] + str1[:p] + "ay")


main()
