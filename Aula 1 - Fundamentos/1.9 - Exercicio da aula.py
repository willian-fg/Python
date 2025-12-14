"""
Exercício 1
Crie um programa que:

Peça o nome do usuário

Peça a idade

Mostre a frase:
Olá, nome. Você tem X anos.

Exercício 2
Peça dois números ao usuário e mostre:

Soma

Subtração

Multiplicação

Divisão
"""
print("-------- Programa 1 ---------")

nome_do_usuario = input("Digite seu nome:")
idade_do_usuario = input("Digite sua Idade:")
print("Olá "+nome_do_usuario+". Você tem "+idade_do_usuario+" anos.")


print("-------- Programa 2 ---------")

numero1 = int(input("digite um número"))
numero2 = int(input("digite um número"))

print(numero1+numero2)
print(numero1-numero2)
print(numero1*numero2)
print(numero1/numero2)

# Refinamento

"""Refinamento recomendado (nível profissional)
1. Melhorar mensagens de entrada"""
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

#2. Usar f-strings (forma moderna e legível)
print(f"Olá {nome_do_usuario}. Você tem {idade_do_usuario} anos.")


"""Vantagens:

Mais legível

Evita concatenação excessiva

Padrão profissional em Python

3. Exibir resultados com descrição"""

print(f"Soma: {numero1 + numero2}")
print(f"Subtração: {numero1 - numero2}")
print(f"Multiplicação: {numero1 * numero2}")
print(f"Divisão: {numero1 / numero2}")
