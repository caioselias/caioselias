# -*- coding: utf-8 -*-
"""
## 1. Faturamento do Melhor e do Pior Mês do Ano

"""

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1 = [25001, 29001, 22202, 17751, 15871, 19901]
vendas_2 = [19851, 20121, 17541, 15551, 49052, 9651]

vendas_ano = vendas_1 + vendas_2
print(vendas_ano)

maior = max(vendas_ano)
menor = min(vendas_ano)


#relacionar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

i = vendas_ano.index(maior)
print("O valor de vendas do melhor mês do ano foi de {} unidades no mês de {}".format(vendas_ano[i], meses[i]))
j = vendas_ano.index(menor)
print("O valor de vendas do pior mês do ano foi de {} unidades no mês de {}".format(vendas_ano[j], meses[j]))
"""

faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

"""

fatur = sum(vendas_ano)
relacao = maior/fatur
print("o melhor mês representou {:1%} das vendas do ano todo.".format(relacao))

"""## realizar um top 3 valores de vendas do ano
"""
print(vendas_ano)

top3 = []

k = 0
while k != 3:
    top3.append(maior)
    vendas_ano.remove(maior)
    maior = max(vendas_ano)
    print(top3)
    k = k+1
