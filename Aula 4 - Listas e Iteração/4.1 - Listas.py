"""
Lista no python é uma estrutura de dado, que armazena varios valores em uma única variável,
é "Ordenada", "Mutavel", e aceita "Tipos Mistos"

"""
numeros = [1, 2, 3, 4, 5]
nomes = ["Ana", "João", "Maria"]
mistura = [1, "texto", True, 3.14]

# -- lista usam indices iniciando em 0
print(nomes[0]) #Ana
print(nomes[1]) #João
print(nomes[2]) #Maria

# -- Indices negativos
print(nomes[1]) #Maria


# ------ Alterando Valores em uma Lista -----

nomes[1] = "Carlos"
print(nomes)

# ----- Percorrendo Listas -----
# --Com For
for nome in nomes:
    print(nome)

# -- Com Índice
for i in range(len(nomes)):
    print(i, nomes[i])

# ---------- Principais Métodos em listas

# -- Append() - Adiciona ao final
nomes.append("pedro")

# -- Insert() - Adiciona em posição especifica
nomes.insert(1, "Lucas")

# -- Remove() - Remove pelo valor
nomes.remove("Ana")

# -- Pop() - Remove pelo índice
nomes.pop(0)

# -- Len() - Tamanho da Lista
print(len(nomes))



# ---------- Verificando se um Elemento Existe

if "Maria" in nomes:
    print("Maria está na lista")


numeros_vazios = []

for i in range(5):
    numeros_usuario = int(input("Digite um Numero: "))
    numeros_vazios.append(numeros_usuario)
    print(numeros_vazios)
    