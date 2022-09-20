import random
def function():
    print("Lançando um par de dados")

    d1 = random.randrange(1, 6)
    d2 = random.randrange(1, 6)
    s= d1+d2
    print(f"Dado 01: {d1}\n Dado 02: {d2}.\n Soma={s}")

    while s!=x:
        if (s==7 or s==11) and (s==7 or s==1):
            print("Você é um natural")
            print("Ganhou, parabéns!!!")
        elif (s==2 or s==3 or s==12) and (s==2 or s==3 or s==12):
            print("CRAPS!!!")
            print("Você PERDEU")
        elif s==7:
            break
        else:
            x = s
            print(f"{s} é seu ponto.")
            print("Seu objetivo é continuar jogando dado até tirar este número novamente ")
function()