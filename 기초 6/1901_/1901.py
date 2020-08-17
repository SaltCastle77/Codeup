import sys
sys.stdin = open("input.txt","r")

n = int(input())

def sequence(k):
    if k != 1 :
        sequence(k-1)
    print(k)

sequence(n)