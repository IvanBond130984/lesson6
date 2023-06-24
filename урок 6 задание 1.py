# счётчик чисел равных 0
zero_i=0
# количество целых чисел
print('Введите количество целых чисел: ')
n=int(input())
for i in range(n+1):
    temp=input('Введите целое чесло: ')
    temp=int(temp)
    if temp==0:
        zero_i+=1
print('Количество нулей',zero_i)