                        ''' ------ Encapsulamento ------ '''
''' É o mecanismo que esconde ou tranca os dados internos
de um objeto para protegelo de alteraçoes indevida ou maliciosas
feitas de fora da classe. Em termos simples: é colocar uma "capsula"
de proteção em volta das suas variáveis.'''

    """ O Problema (Sem Encapsulamento)"""

"""Se deixamos o código aberto, qualquer um pode quebrar as regras de negócio do sistema 
direto pelo terminal:
"""


conta = ContaBancaria()
conta.saldo = -5000000 # O Python aceita isso direto!


        """ ---- Sintax ---- """

class ContaBancariaComCapsula:
    def __init__(self, saldo):
        self.__saldo = saldo # Dois (__) antes do nome das variáveis. Assim somente a classe pode alterar o valor.

    GETTER: #Permite ver o saldo
        def exibir_saldo(self):
            return self.__saldo

    
    SETTER:
        def depositar(self, valor):
            if valor > 0:
                self.__saldo += valor
            else:
                Print("Você não pode depositar um valor negativo!")
