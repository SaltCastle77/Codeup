import sys
sys.stdin = open("input.txt","r")

T= int(input())

for t in range(T,0,-1):
    print("*"*t)
