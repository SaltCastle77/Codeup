import sys
sys.stdin = open("input.txt","r")

T=int(input())
number=list(map(int,input().split()))
for t in range(T-1,-1,-1):
    print(number[t],end=' ')
    