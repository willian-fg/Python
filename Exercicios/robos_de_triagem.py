class RoboDeTriagem:
    def __init__(self, nome):
        self.nome = nome
        self.total_de_pecas_aprovadas = 0   
        self.total_de_pecas_reprovadas = 0
        self.peso_total_processado = 0

    def processar_esteira(self, lista_de_pesos):

        self.lista_de_pesos = []

        for peso in lista_de_pesos:

            resto_da_divisão_do_peso = peso % 2
            if (peso >= 100) and (peso <= 300):
                if resto_da_divisão_do_peso == 0:
                    print(f"Peso {peso}, Aprovado")
                    self.total_de_pecas_aprovadas += 1
                    self.peso_total_processado += peso
                
                else:
                    print(f"Peso {peso} reprovado (é ímpar).")
                    self.total_de_pecas_reprovadas += 1
                    self.peso_total_processado += peso

            elif (peso == 99) or (peso == 333):
                    print("Alerta, Peso crítico detectado. Travando esteira!")
                    break

            else:
                print("Pesso {peso} reprovado.")
                self.total_de_pecas_reprovadas += 1
                self.peso_total_processado += peso


    def relatorio(self):
        print(f"""
        Total de Peças Aprovadas: {self.total_de_pecas_aprovadas}
        Trotal de Peças Reprovadas {self.total_de_pecas_reprovadas}
        Total de Peso Processado {self.peso_total_processado}
        """)


robo = RoboDeTriagem("Robo")

esteira_da_fabrica = [120, 250, 85, 302, 144, 99, 200]

robo.processar_esteira(esteira_da_fabrica)
robo.relatorio()









