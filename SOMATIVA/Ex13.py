import random as r
resultado = []
global x

def quadradoPerfeito():
    x = 0
    while x < 1:
        numeros = [1,2,3,4,5,6,7,8,9]
        p_trinca = []
        s_trinca = []
        t_trinca = []

        for i in range(3):
            numero_p = r.choice(numeros)
            numeros.remove(numero_p)
            p_trinca.append(numero_p)

        for i in range(3):
            numero_s = r.choice(numeros)
            numeros.remove(numero_s)
            s_trinca.append(numero_s)

        for i in range(3):
            numero_t = r.choice(numeros)
            numeros.remove(numero_t)
            t_trinca.append(numero_t)

        if(sum(p_trinca) == sum(s_trinca) == sum(t_trinca)):
            if(sum(p_trinca) == (p_trinca[0] + s_trinca[1] + t_trinca[2])):
                if(sum(p_trinca) == (p_trinca[2] + s_trinca[1] + t_trinca[0])):
                    if((p_trinca[1]+ s_trinca[1]+ t_trinca[1]) == (p_trinca[0]+ s_trinca[0]+ t_trinca[0]) == (p_trinca[2]+ s_trinca[2]+ t_trinca[2])):
                        resultado.append(p_trinca)
                        resultado.append(s_trinca)
                        resultado.append(t_trinca)
                        x = x + 1
                        
                    
    print("RESULTADO:")                                  
    for i in range(3):
        print(f"{resultado[i]} ")

    print("\n")
    print("SOMA DAS LINHAS")
    print(sum(p_trinca))
    print(sum(s_trinca))
    print(sum(t_trinca))

    print("\n")
    print("SOMA DAS COLUNAS")
    print(p_trinca[0]+ s_trinca[0]+ t_trinca[0])
    print(p_trinca[2]+ s_trinca[2]+ t_trinca[2])
    print(p_trinca[1]+ s_trinca[1]+ t_trinca[1])

    print("\n")
    print("SOMA DAS COLUNAS")
    print(p_trinca[0] + s_trinca[1] + t_trinca[2])
    print(p_trinca[0] + s_trinca[1] + t_trinca[2])
    
quadradoPerfeito()