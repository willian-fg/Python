"""
O laço "for" é usado quando você sabe quantas vezes quer repeti.
"""
# Range -- a função range gera uma sequencia de números

#range(inicio, fim, passo)

for i in range(5):
    print(i)      # 0 a 4

for i in range(0, 10, 2):
    print(i)    # 0, 2, 4, 6, 8

# ----- Com Strings -----
for letra in "Python":
    print(letra)