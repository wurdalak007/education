#Напишите функцию подсчитывающую количество способов разбить n фантиков на монетки по 1,5,10 фантиков.
n = int(input())
res = 0

for i in range(n//10 + 1):
    res += (n - i*10)//5 + 1

print(res)