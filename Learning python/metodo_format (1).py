# -*- coding: utf-8 -*-

faturamento = 2000
custo = 500
lucro = faturamento - custo

print('O faturamento da loja foi ' + str(faturamento) + '.O custo da loja foi ' + str(custo) + '.Assim, o lucro da loja foi de ' + str(lucro))

"""### Método format"""
# faturamento = 2000
# custo = 500
# lucro = faturamento - custo
print("'O faturamento da loja foi {}.O custo da loja foi {}.Assim, o lucro da loja foi de {}".format(faturamento,custo,lucro))
print(f"'O faturamento da loja foi {faturamento}.O custo da loja foi {custo}.Assim, o lucro da loja foi de {lucro}")

ganhou = int(input("Insira o qto ganhou:"))
perdeu = int(input("Insira o qto perdeu:"))
sobrou = ganhou - perdeu
print(sobrou)