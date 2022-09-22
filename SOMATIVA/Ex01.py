x = int(input("Digite um número:"))


def piramide():
  res = ""
  aux = 1
  for y  in range(x):
      for y in range(aux):
        res = f"{aux} "*(aux)
      print(res)
      aux = aux + 1 

piramide()