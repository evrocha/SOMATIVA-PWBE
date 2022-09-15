import random
sum = []
numeros = [1,2,3,4,5,6,7,8,9]
res = 0

while True:
    for x in range(3): 
        num = random.choice(numeros)
        numeros.remove(num)
        res = res+ num
        print(num)
    sum.append(res)
    
    if (sum[0] == sum[1]):
        break
    else:
        numeros = [1,2,3,4,5,6,7,8,9]
        sum = []
        res = 0
print(sum)