num = str(input("Digite um número:"))
x = num.__len__() - 1
res = ""

while x != -1:
    res = res + f"{num[x]}"
    x = x - 1

print(res)
