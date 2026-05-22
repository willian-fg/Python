# ---- Funçoes

def dividir(n1, n2):
    return n1 / n2 


# ------ Loop Principal

while True:
    print(" ---- Menu de Divisão ----")
    print("Digite sair a qualquer momento para encerrar")


    try:
        # Pega as entradas do usuário
        entrada1 = input("Digite o primeiro número")
        if entrada1.lower() == "sair":
            break

        entrada2 = input("Digite o segundo número")
        if entrada1.lower() == "sair":
            break
        

        #Convertendo para numeros flutantes
        num1 = float(entrada1)
        num2 = float(entrada2)

        # Fazendo a divizão (Possivel erro)
        resultado = dividir(num1, num2)


    except ValueError: # Caso o usuário digite letras.
        print("Erro: Entrada inválida! Por favor, digite apenas número.")

    except ZeroDivisionError: # Caso o usuário digite zero
        print("Erro: O universo colapsou! Não é possivel dividir por zero (0).")

    else:
        print(f"Sucesso! O resultado de {num1} / {num2} é: {resultado}")

    finally:
        print("------------------------------------")

print("O programa foi encerrado com sucesso!")

         

