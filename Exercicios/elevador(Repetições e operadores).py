andar_atual = 0
fila_requisicoes = [3, 8, 2, 9, 1, 5]
gasto_do_gerador = 0
freio_de_emergencia = False
for andar in fila_requisicoes:
    if andar > andar_atual:
        print(f"Proximo andar: {andar} (subindo)")

        while andar_atual < andar:
            andar_atual += 1
            gasto_do_gerador += 2
            print(f"andar {andar_atual}")
            if andar_atual == 5:
                print("Passando pelo andar 5 ativando freio de emergencia!")
                gasto_do_gerador += 10


     
    if andar < andar_atual:
        print(f"Proximo andar: {andar} (descendo)")

        while andar_atual > andar:
            andar_atual -= 1
            gasto_do_gerador += 3
            print(f"andar {andar_atual}")
            if andar_atual == 5:
                print("Passando pelo andar 5 ativando freio de emergencia!")
                gasto_do_gerador += 10

print(f"Gasto total: {gasto_do_gerador}")
