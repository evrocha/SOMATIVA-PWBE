def conversao(A=int(12), P=int(24)):
    hora12 = 0
    print('Conversão de Hora')
    print('Digite no formato 24 horas')
    hora = int(input('Horas: '))
    minuto = int(input('Minutos: '))
    global hora24
    hora24 = f'{hora}:{minuto}'
    
    if hora<=A and hora>0: 
        hora12 = f'{hora}:{minuto} AM'

    elif hora>A and hora<=P: 
        hora12 = f'{(hora-12)}:{minuto} PM'

    return hora12

def saida():
    x = conversao()
    print(f'{hora24} é a mesma coisa que {x}')


x = 'SIM'
while x == 'SIM':
    saida()
    x = str(input('Deseja realizar a operação novamente? Digite Sim ou Não'))
    x = x.upper()



         