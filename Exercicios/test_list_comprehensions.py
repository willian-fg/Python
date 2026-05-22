notas = {"lucas": 8, "Pedro": 5, "Willian": 9, "Ana": 4}

aprovados = {nome: nota for nome, nota in notas.items() if nota >= 7}

#aprovados = {nome: nota                      for nome, nota     in notas.items() if nota >= 7}
#Tradução = {(crie um par de "nome : nota"   para nome, nota   em notas.items() if nota >= 7}

print(aprovados)

