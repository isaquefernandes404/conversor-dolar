cotacao = float(input("digite a cotação atual: "))
real = float(input("digite o valor em BRL: "))
dolar = real / cotacao
print(f"com o valor de {real}, com a cotação {cotacao}, voce possui U${dolar:.2f} dolares")