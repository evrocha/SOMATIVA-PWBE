import random
def function():
  ponto = 0
  primeira_jogada = random.randrange(2, 12)
  def jogarDado():
    dado = random.randrange(2, 12)
    return dado
  if primeira_jogada == 7 or primeira_jogada == 11:
    print(f"Caiu {primeira_jogada} na primeira rodada")
    print("Você é um natural\nGanhou, parabéns!!!")
    return 
  elif primeira_jogada == 2 or primeira_jogada == 3 or primeira_jogada == 12:
    print(f"Caiu {primeira_jogada}\nCRAPS!!!\nVocê perdeu")
    return
  else: 
    outra_rod = jogarDado()
    ponto = primeira_jogada
    jogarDado()
    while outra_rod != ponto:
      d2 = jogarDado()
      outra_rod = d2
      print(f"{ponto} é seu ponto da primeira jogada.\n{outra_rod} É O seu ponto nesta rodada\nSeu objetivo é continuar jogando O dado até tirar o número da primeira jogada novamente")
      if outra_rod ==7:
        print(f"Você tirou 7 antes de tirar o mesmo número. Você perdeu")
        jogarDado()
        return
function() 