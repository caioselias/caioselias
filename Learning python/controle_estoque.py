# -*- coding: utf-8 -*-
#controle de estoque

categoria = input("Digite a categoria:")
nome_produto = input("Digite o nome do produto:")
quantidade = int(input("Digite a quantidade:"))


if categoria == "" or nome_produto == "" or quantidade == "":
    
    print("Digite corretamente os dados")
else:
    pass

    if categoria == "alimentos":
        estoque = 50
        if quantidade < estoque:
            print(f"Solicitar {nome_produto} à equipe de compras, temos apenas {quantidade} em estoque")
    elif categoria == "bebidas":
        estoque = 75
        if quantidade < estoque:
            print(f"Solicitar {nome_produto} à equipe de compras, temos apenas {quantidade} em estoque")
    elif categoria == "limpeza":
        estoque = 30
        if quantidade < estoque:
            print(f"Solicitar {nome_produto} à equipe de compras, temos apenas {quantidade} em estoque")
