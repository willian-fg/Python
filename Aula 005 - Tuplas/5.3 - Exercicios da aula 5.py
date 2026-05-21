# ----- Exercício 1 -----

informacoes_do_usuario = ("will", 45, 1.75)
nome, idade, altura = informacoes_do_usuario
print(nome)
print(idade)
print(altura)

# ----- Exercício 2 -----

numeros_do_usuario = set()

for i in range(5):
    n = int(input("Digite um Número:"))
    numeros_do_usuario.add(n)
print(numeros_do_usuario)

# ----- Exercício 3 -----
con_a = {1, 2, 3}
con_b = {3, 4, 5}

print(con_a | con_b)
print(con_a & con_b)
print(con_a - con_b)
