import sys
sys.stdin = open("input.txt","r")

n=int(input())

for i in range(1,7):
    for j in range(1,7):
        if i+j ==n:
            print('{} {}'.format(i,j))




