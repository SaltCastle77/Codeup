import sys
sys.stdin = open("input.txt","r")

h,r = map(int,input().split())

for i in range(r):
    for j in range((h*2)-1):
        if j == 0:
            print('*')
        elif j == 1:
            print(' *')
        elif j == 2:
            print('  *')
        elif j == 3:
            print(' *')
        elif j == 4:
            print('*')

