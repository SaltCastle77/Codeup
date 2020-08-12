import sys
sys.stdin = open("input.txt","r")

T=int(input())


for t in range(1,T+1):
    for j in range(0,T):
        print(t*T-j, end=' ')   
    print()     