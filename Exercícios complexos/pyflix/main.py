from modelos import Catalogo, Filme

def exibir_menu():
    print("\n" + "="*30)
    print("      🎬 MENU PYFLIX 🎬      ")
    print("="*30)
    print("1 - Cadastrar Filme")
    print("2 - Buscar Filmes por Género")
    print("3 - Salvar Catálogo em Arquivo")
    print("4 - Sair")
    print("="*30)

def main():
    catalogo = Catalogo()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "1":
            print("\n--- 📝 CADASTRAR FILME ---")
            titulo = input("Título do filme: ")
            genero = input("Género do filme: ")
            
            # loop de proteção para a nota usando try/except
            while True:
                try:
                    nota = float(input("Nota do filme (0.0 a 10.0): "))
                    break  # Se a conversão funcionou, sai do loop da nota
                except ValueError:
                    print("❌ Erro: Por favor, digite um número válido para a nota!")

            # Criamos a namedtuple e adicionamos ao catálogo
            novo_filme = Filme(titulo=titulo, genero=genero, nota=nota)
            catalogo.adicionar_filmes(novo_filme)
            print(f"✅ '{titulo}' adicionado com sucesso!")
            print(catalogo) # Aciona o teu método mágico __str__

        elif opcao == "2":
            print("\n--- 🔍 BUSCAR POR GÉNERO ---")
            busca = input("Digite o género que procura: ")
            resultados = catalogo.buscar_por_genero(busca)

            if resultados:
                print(f"\n🍿 Filmes encontrados de {busca.capitalize()}:")
                for f in resultados:
                    print(f"🎬 {f.titulo} | Nota: {f.nota}")
            else:
                print(f"⚠️ Nenhum filme do género '{busca}' encontrado.")

        elif opcao == "3":
            print("\n--- 💾 A SALVAR CATÁLOGO ---")
            filmes_para_salvar = catalogo.obter_todos()

            if not filmes_para_salvar:
                print("⚠️ O catálogo está vazio. Nada para salvar.")
                continue

            # I/O: Escrita de arquivo blindada com o Context Manager 'with'
            with open("catalogo.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write("=== MEU CATÁLOGO PYFLIX ===\n\n")
                for f in filmes_para_salvar:
                    arquivo.write(f"Filme: {f.titulo} | Género: {f.genero} | Nota: {f.nota}\n")
            
            print("💾 Sucesso! Arquivo 'catalogo.txt' gerado/atualizado na pasta.")

        elif opcao == "4":
            print("\n🍿 Obrigado por usar o PyFlix. Até à próxima!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
