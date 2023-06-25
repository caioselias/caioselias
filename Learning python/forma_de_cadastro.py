# -*- coding: utf-8 -*-

cpf = input("Insira seu CPF (digite apenas números)")

#tirar espaços inicio e final
cpf = cpf.strip()
#tirar pontos
cpf = cpf.replace('.', '')
#tirar traços
cpf = cpf.replace('-', '')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print("insira o CPF corretamente")



nome = input("Digite seu nome:")
email = input("Digite seu email:")
if nome and email:
    pos_a = email.find("@")
    servidor = email[pos_a:]
    if pos_a != -1 and "." in servidor:
        print("Cadastro concluido")
    else: 
        print("Email invalido")
else:
    print("Digite seu nome e email corretamente")