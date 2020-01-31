#Author: Vidhi Panda <vidhimpanda@gmail.com>
#Concatenates two string
def concatenation(strng1,strng2):
    concatenate = strng1+" "+strng2
    return concatenate

#The main function
def main():
    str1=input("Enter the 1st string: ")
    str2=input("Enter the 2nd string: ")
    x=concatenation(str1,str2)
    print("The concatenated string is: " +x)
    
    
main()
