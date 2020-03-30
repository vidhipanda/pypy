# Author: Vidhi Panda <vidhimpanda@gmail.com>
# Min_Max in a list.

def main():
    testcases = int(input())
    for a in range(testcases):
        l = int(input())
        arr = []
        for k in range(l):
            n = int(input())
            arr.append(n)
        max = arr[0]
        min = arr[0]
        for i in range(1,l):
            if arr[i] > max:
                max = arr[i]
            if arr[i] < min:
                min = arr[i]
        print("MIN =",min)
        print("MAX =",max)

main()

            


