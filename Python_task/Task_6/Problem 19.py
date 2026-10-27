
# Problem Name: Validating phone numbers
# Hackerrank Url: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

T = int(input())

for _ in range(T):
    number = input()
    
    if re.fullmatch(r'[7-9][0-9]{9}', number):
        print("YES")
    else:
        print("NO")
