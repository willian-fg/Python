# ----- Programa 1 -----

lista_de_nomes = ["Ana", "Bruna", "Carlos", "Diego", "Estefany"]
for i in range(len(lista_de_nomes)):
    print(i, lista_de_nomes[i])

# ----- Programa 2 -----
lista_de_numeros_digitados_pelo_usuario = []
for i in range(2):
    numeros_digitados = int(input("Digite um Numero: "))
    lista_de_numeros_digitados_pelo_usuario.append(numeros_digitados)
    print(lista_de_numeros_digitados_pelo_usuario)
soma = lista_de_numeros_digitados_pelo_usuario[0] + lista_de_numeros_digitados_pelo_usuario[1]
print(soma)

# ----- Programa 3 -----
lista_maior_menor = [35, 56, 1000, 22, 0,2]
maior_da_lista = max(lista_maior_menor)
menor_da_lista = min(lista_maior_menor)
print(f"Maior é {maior_da_lista}, o menor é {menor_da_lista}")

# ----- Programa 4 -----

lista_de_nomes_2 = []
novos_nomes = []
while True:
    novo_nome = input("Digite um nome ou 0 para sair: ")
    if novo_nome == "0":
        break
    lista_de_nomes_2.append(novo_nome)
    print(lista_de_nomes_2)

print("Lista final:", lista_de_nomes_2)