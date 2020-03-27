# Author: Vidhi Panda <vidhimpanda@gmail.com>
# File handling

def main():
    testcases = int(input())
    for a in range(testcases):
        fname = input()
        f = open(fname,"r")
        data = f.read() 
        f.close()
        print(data.split(' ')[-1])
        data = data.replace("The", "A")
        data = data.replace("the", "a")
        print(data)
        f = open(fname,"w")
        f.write(data)
        f.close()
main()

