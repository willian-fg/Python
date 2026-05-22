class ContaBancaria:
    def __init__(self, titular):
        self.__saldo = 0
        self.titular = titular


    # ---- GETTER: ----
    def exibir_saldo(self):
        print(f"O saldo atual de {self.titular} é R$ {self.__saldo}")



    # ---- SETTER: ----
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"O deposito de R$ {valor} realizado")
            
        else:
            print("Operação inválida: O valor depositado deve ser positivo ")



        # ----SETTER: ----
    def sacar(self, valor):
        if (valor > 0):
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f"O Saque de R$ {valor}")
            elif valor > self.__saldo:
                print(f"Saldo insuficiente para saque de R${valor}")

## ----- Testando o código --------

# -- Criando conta
minha_conta = ContaBancaria("willian")

# -- Testando Operaçoes Válidas
minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.exibir_saldo()

# -- Testando as defesa do encapsulamento
# Operação invalida
minha_conta.depositar(-1000)

# Sacando mais do que o saldo
minha_conta.sacar(1000)

## ------ Testando Encapsulamento ------
# Alterando o saldo  
minha_conta.__saldo = 9999999

# Acessando saldo
minha_conta.exibir_saldo()
        
