#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os
# carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer
# outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em
# caixa alta ou caixa baixa, independentemente de como foram digitados

from operator import contains
import random

def function():
    i = 0
    frase2 = ''
    f3 = ''
    frase = str(input("Digite uma palavra: "))   
    
    while i<len(frase):
        num_used = []
        num_rand = random.randrange(0, len(frase))
        frase2 = frase[num_rand]

        num_used.extend(frase2)
        
        

        # print(i)
        print(frase2)
        i = i+1
    print(num_used) 
    
        
function()