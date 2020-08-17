import sys
sys.stdin = open("input.txt","r")

T=int(input())

numbers = list(map(int,input().split()))

for i in range(T):
    for number in numbers:
        print(number,end=' ')
    print()
    last = numbers.pop(0)
    numbers = numbers+[last]