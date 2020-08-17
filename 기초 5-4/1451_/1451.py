import sys
sys.stdin = open("input.txt","r")

T= int(input())
numbers = []

for t in range(T):
    n=int(input())
    numbers.append(n)
numbers.sort()

for number in numbers:
    print(number)
    