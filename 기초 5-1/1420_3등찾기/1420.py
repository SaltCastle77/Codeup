import sys
sys.stdin = open("input.txt","r")

T=int(input())
result= {}

for t in range(T):
    name , score = input().split()
    result[name] = int(score)

sort_result=sorted(result.values())

for key,value in result.items():
    if value == sort_result[-3]:
        print(key)