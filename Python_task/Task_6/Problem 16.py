
# Problem Name: Check Strict Superset
# Hackerrank Url: https://www.hackerrank.com/challenges/py-check-strict-superset/problem


A = set(map(int, input().split()))

n = int(input())
B = set(map(int, input().split()))

print(A.issubset(B))
