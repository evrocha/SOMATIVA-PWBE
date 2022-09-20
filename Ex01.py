x = int(input("Digite um número:"))

def piramide():
  res = ""
  aux = 1
  aux2 = 1
  for y in range(x):
      for y in range(aux):
        res = res + f"{aux2} "
        aux2= aux2 + 1
      print(res)
      aux =+ 1

piramide()