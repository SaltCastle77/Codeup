import sys
sys.stdin = open("input.txt","r")

n,m = map(int,input().split())

if n>m :
    print(m,end=' ')
    print(n)
else : 
    print(n, end=' ')
    print(m)