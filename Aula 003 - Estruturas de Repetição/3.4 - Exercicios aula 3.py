import time
# ----- Program 1 -----
numero = 1

while numero != 0:
    numero = int(input("Digite um Número(0 para sair):"))

print("Programa encerrado")


# ----- Program 2 -----

for i in range(1,11):
    print(i)


# ----- Program 3 -----

for i in range(2, 22, 2):
    print(i)


# ----- Program 4 -----

for i in reversed(range(1, 11)):
    print(i)
    time.sleep(1)