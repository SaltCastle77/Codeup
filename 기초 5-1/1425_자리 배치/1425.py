import sys
sys.stdin = open("input.txt","r")

n,c = tuple(map(int,input().split()))
numbers = list(map(int,input().split()))

sort_number = []

min_value = float("inf")
for i in numbers : 
   if i < min_value :
       numbers[i] == numbers[0]
       numbers.pop(0)
