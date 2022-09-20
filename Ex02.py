x = int(input("Digite um número:"))

def piramide():
  res = ""
  aux = 1
  for y  in range(x):
      for y in range(aux):
        res = res + f"{x} "
      print(res)
      aux =+ 1

piramide()