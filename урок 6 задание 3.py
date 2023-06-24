print('Введите 2 числа:')
a,b=map(int, input().split())
for i in range(a,b+1):
    if i%2==0:
        print(i,sep='', end=' ')