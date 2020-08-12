import sys
sys.stdin = open("input.txt","r")

number=str(input())
total = 0 
for t in number:
    total += int(t)

if total % 3 == 0 :
    print('1')
else:
    print('0')