# ------ Modificado lista com Compression
usuarios = ["lucas", "willian", "pedro"]

usuários_prontos = [usr.title() for usr in usuarios]

print(usuários_prontos)

# ------ Filtrando com if e compression

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [n for n in numeros if n % 2 == 0]

print(pares)

# ------- Desafio 
# Modifica ou criar uma lista que monte uma lista que só tenha 5 letra no nome

pessoas = ["Carlos", "Ana", "Rita", "Willian", "Miguel", "Lucas", "Bia", "Léo"]

filtro_de_5_letras = [n for n in pessoas if len(n) == 5]

print(filtro_de_5_letras)
