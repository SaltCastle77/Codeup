import sys
sys.stdin = open("input.txt","r")

T=int(input())
number=list(map(int,input().split()))
for _ in range(2):
    for t in range(T):
        print(number[t])
