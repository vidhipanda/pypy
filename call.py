# Author: Vidhi Panda <vidhimpanda@gmail.com>
# API call in python

import requests


def main():
    testcases = int(input())
    for a in range(testcases):
        emp_id = input()
        get(emp_id)


def get(id):
    url = "http://dummy.restapiexample.com/api/v1/employees"
    x = requests.get(url)
    emp_list = x.json()['data']
    found = 0
    for emp in emp_list:
        if str(emp['id']) == str(id):
            print("id =", id)
            print("name =", emp['employee_name'])
            print("age =", emp['employee_age'])
            found = 1
            break
    if found == 0:
        print('ID not found')


main()
