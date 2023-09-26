import sys
k=int(sys.stdin.readline())
num_list=[]
for _ in range(k):
    num=int(sys.stdin.readline())
    num_list.append(num)
num_list.sort()
for i in range(k):
    print(num_list[i])
