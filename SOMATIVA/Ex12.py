import random as r
from xml.etree.ElementTree import tostring
letras = []

def embaralhar():
    palavra = str(input("Digite a palavra que deseja embaralhar:"))
    letras = list(palavra)
    r.shuffle(letras)
    palavra = ""
    for i in range(letras.__len__()):
        palavra = palavra + f"{letras[i]}"
    print(palavra)
    
embaralhar()