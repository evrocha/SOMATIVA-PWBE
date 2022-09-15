# arrumar o calculo
def valorPagamento():
    vlr_prest = 1
    vlr_tot = 0
    while(vlr_prest!= 0):
        vlr_pag = 0
        
        vlr_prest = float(input("Valor prestação: "))
        d_atr = int(input("Dias em atraso: "))

        if d_atr == 0:
            vlr_pag = vlr_prest
            vlr_tot = vlr_tot + vlr_pag

        elif d_atr!= 0:
            vlr_pag = (vlr_prest * 0.03) + (d_atr * 0.001)
            vlr_tot = vlr_tot + vlr_pag
        
        # vlr_tot = vlr_tot + vlr_pag
        
    else:
        print(f"\t Relatório do dia:\n",
        f"Valor total das prestações pagas = {vlr_tot}")


valorPagamento()