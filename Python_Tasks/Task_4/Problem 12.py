
# Problem Name: Introduction to Sets
# Hackerrank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(arr):
    unique_heights = set(arr)
    result = sum(unique_heights) / len(unique_heights)
    return round(result, 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
