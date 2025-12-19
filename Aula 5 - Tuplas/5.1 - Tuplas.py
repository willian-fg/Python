"""
Tupla é uma coleção:

Ordenada,

Imutável,

Aceita tipos mistos.
"""

coordenadas = (10, 20)
nomes = ("Ana", "Bruno", "Carlos")

#3. Acesso por índice
nomes = ("Ana", "Bruno", "Carlos")
print(nomes[0])


#❌ Isto gera erro:

nomes[0] = "Maria"  # TypeError

#4. Percorrendo tuplas
for nome in nomes:
    print(nome)

#5. Desempacotamento de tuplas
pessoa = ("Will", 30, 1.75)
nome, idade, altura = pessoa

print(nome)
print(idade)
print(altura)

#6. Tupla com um único elemento (atenção!)
tupla_errada = (5)
print(type(tupla_errada))  # int

tupla_correta = (5,)
print(type(tupla_correta))  # tuple
