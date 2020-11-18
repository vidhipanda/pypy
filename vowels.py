# Author: Vidhi Panda <vidhimpanda@gmail.com>
# Printing string without vowels

# The Main function

def main():
    inp = input()
    l = ['a', 'e', 'i', 'o', 'u']
    str1 = ''
    for i in inp:
        if i in l:
            continue
        else:
            str1 = str1 + i
    print(str1)
main()
