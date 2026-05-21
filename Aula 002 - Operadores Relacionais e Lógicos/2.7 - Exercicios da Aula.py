"""
Exercício 1

Peça a idade do usuário e mostre:

"Pode votar" se idade ≥ 16

"Não pode votar" caso contrário

Exercício 2

Peça:

Usuário

Senha

Mostre "Acesso permitido" se:

Usuário == "admin"

Senha == "1234"

Caso contrário, mostre "Acesso negado".

Exercício 3

Peça um número e verifique:

Se é maior que 0 → "Positivo"

Se é menor que 0 → "Negativo"

Se é igual a 0 → "Zero"
"""

print("---------- Programa 1 ----------")

idade = int(input("Qual a sua idade?"))

if idade >= 16:
    print("Pode Votar")
if idade < 16:
    print("Não pode votar")

print("---------- Programa 2 --------")

usuario = input("Usuário")
senha = input("Senha")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")

print("---------- Programa 3 ----------")

numero = int(input("Numero"))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")
