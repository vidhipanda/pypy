# Author: Vidhi Panda <vidhimpanda@gmail.com>
# Dictonary in python

def main():
    dict_country = {
        'India':'Delhi',
        'Pakistan':'Islamabad',
        'Srilanka':'Columbia',
        'Italy':'Rome',
        'Bangladesh':'Dhaka'
    }
    testcases = int(input())
    for a in range(testcases):
        country = input()
        for ctry in dict_country.keys():
            if ctry.lower() == country.lower():
                capital = dict_country[ctry]
                break
            else:
                capital = "Not Found"
        print("The capital of "+country +" is " +capital)

        

main()
