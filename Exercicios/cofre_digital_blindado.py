class CofreBancario:
    def __init__(self, dono, senha):
        self.dono = dono
        self.__senha = senha
        self.__saldo = 0
        self.__bloqueio = True


    #SELTTER que destrava a conta
    def destravar(self, senha_digitada):
        if senha_digitada == self.__senha:
            print("Cofre aberto")
            self.__bloqueio = False
        else:
            print("Acesso negado: Cofre Bloqueado.")


    #GELTTER que exibe o saldo 
    def exibir_saldo(self):
        if self.__bloqueio == True:
            print("Acesso Negado")
            
        else:
            print(f"O Saldo da conta de {self.dono} é de R$ {self.__saldo}")

    
    #SELTTER que deposita
    def depositar(self, valor):
        if not self.__bloqueio:
            self.__saldo += valor
            print(f"Valor {valor} adicionado a conta.")

        else:
            print("Cofre trancado.")


    #SELTTER que saca do cofre
    def sacar(self, valor):
        if self.__bloqueio:
            print("Acesso negado.")

        elif not self.__bloqueio:
            self.__saldo -= valor
            print(f"Valor {valor} sacado.")


    #SELTTER que trava o cofre
    def travar(self):
        self.__bloqueio = True
 


# ---- contas Principal
cofre1 = CofreBancario("Lucas", "1234")

 # ---- LoopPrincipal           
while True:
    print(" -- Contas Python --")
    print("1: Destrava | 2.exibir_saldo | 3.Depositar | 4.sacar | 5.Travar | 6.Sair")
    botao_presionado = input("Digite o número da operação:")

    try:
        # ---- Destravando
        if botao_presionado == 1:
            senha_digitada = input("Digite a senha:")
            cofre1.destravar(senha_digitada)
        

        # ---- Exibindo saldo
        elif botao_presionado == 2:
            cofre1.exibir_saldo()
        
         
        # ---- Depositando
        elif botao_presionado == 3:
            valor_de_deposito = int(input("Digite o valor do depósito:"))
            cofre1.depositar(valor_de_deposito)
        

        # ---- Fazendo Saque  
        elif botao_presionado == 4:
            valor_de_saque = int(input("Digite o valor que deseja retirar:"))
            cofre1.sacar(valor_de_saque)
        

        # Travando o cofre    
        elif botao_presionado == 5:
            cofre1.travar()

        elif botao_presionado == 6:
            break

    except ValueError:
        print(" Por favor digite apenas o números.")

    finally:
        print("-----------------------")

