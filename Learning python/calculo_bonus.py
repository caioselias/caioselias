# -*- coding: utf-8 -*-
#cálculo de bonus 1

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

meta = 1000

funcionarios = [vendas_funcionario1,vendas_funcionario2,vendas_funcionario3]
for i in funcionarios:
    if i >= meta:
        bonus = 0.1 * i
    else:
        bonus = 0 * i
    print(bonus)


## calculo de bonus 2

meta = 1000

funcionarios = [vendas_funcionario1,vendas_funcionario2,vendas_funcionario3]
for i in funcionarios:
    if i >= 2000:
        bonus = 0.15 * i
    elif i < 1000:
        bonus = 0 * i
    else:
        bonus = 0.1 * i
    print("o funcionário que fez {} reais ganhou {} de bonus".format(i, bonus))
 