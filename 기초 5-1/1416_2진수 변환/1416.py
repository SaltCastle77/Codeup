import sys
sys.stdin = open("input.txt","r")

n=int(input())

rest =''

if n==0 :
    print('0')
else :
    while n>=1 :
        rest += str(n % 2)
        n = int(n/2)
    print(rest[::-1])
