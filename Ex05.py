def somaimposto(taxaimposto, custo):
    total=0
    imposto=0
    imposto= taxaimposto * custo
    total= custo + imposto

    print(f"O valor com imposto é R${total}")

somaimposto(0.15, 500)
somaimposto(0.42, 80)



