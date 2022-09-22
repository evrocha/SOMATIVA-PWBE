def analisenum(num):
    if num>0:
        return f'P'
    else:
        return f'N'

print(analisenum(int(input('Digite um número qualquer: '))))