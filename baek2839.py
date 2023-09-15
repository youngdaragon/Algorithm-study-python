import sys
input=sys.stdin.readline()
a=int(input)
k=a%5
j=a//15
# 5a+3b에서 b=0일때 쭉 돌고 만약 5a==N이면 중단 넘어가면 b=1로 바꿔서 다시돌림 b=1로 바꿀때는 N-3이런식으로 해줌
if a==4 or a==7:
    r=-1
else:
    if k==0:
        r=a//5
    elif k==1:
        r=a//5+1
    elif k==2:
        r=a//5+2
    elif k==3:
        r=a//5+1
    elif k==4:
        r=a//5+2

print(r)
