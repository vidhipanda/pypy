# Author: Vidhi Panda <vidhimpanda@gmail.com>
# File handling

def main():
    testcases = int(input())
    for a in range(testcases):
        fname = input()
        fname1 = fname + '.txt'
        f = open(fname1,'w')
        data = 'Hello, "' +fname  + '"\n'
        f.write(data)
        f.close()
main()

