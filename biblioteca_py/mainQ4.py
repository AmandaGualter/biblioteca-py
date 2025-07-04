# Dicionário8
biblioteca = {}
proximo_id = 1  # ID

def cadastrar_livro():
    print("\n-----Cadastrar livro-----")
    global proximo_id
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    biblioteca[proximo_id] = {"Título": titulo, "Autor": autor, "Editora": editora,}
    print(f"Livro cadastrado com sucesso! ID: {proximo_id}")
    proximo_id += 1

def consultar_livros():
    print("\n-----Consultar livros-----")
    print("\nEscolha uma opção de consulta:")
    print("1. Todos os livros")
    print("2. Por ID")
    print("3. Por Autor")
    print("4. Por Título")
    
    opcao = input("Opção: ")
    
    if opcao == "1": #Todos os livros
        if biblioteca:
            for id, info in biblioteca.items():
                print(f"ID: {id}")
                print(f"Título: {info['Título']}")
                print(f"Autor: {info['Autor']}")
                print(f"Editora: {info['Editora']}")
        else:
            print("Nenhum livro cadastrado.")
    
    elif opcao == "2": #Pesquisar por id
        id_busca = int(input("Digite o ID do livro: "))
        livro = biblioteca.get(id_busca)
        if livro:
            print(f"ID: {id_busca} - Título: {livro['Título']} - Autor: {livro['Autor']} - Editora: {livro['Editora']}")
        else:
            print("Livro não encontrado.")

    elif opcao == "3": #Por autor
        autor_busca = input("Digite o nome do autor: ")
        encontrados = [f"ID: {id} - Título: {info['Título']}" for id, info in biblioteca.items() if info["Autor"].lower() == autor_busca.lower()]
        if encontrados:
            print("\n".join(encontrados))
        else:
            print("Nenhum livro encontrado para esse autor.")

    elif opcao == "4": #por titulo
        titulo_busca = input("Digite o título do livro: ")
        encontrados = [f"ID: {id} - Autor: {info['Autor']}" for id, info in biblioteca.items() if info["Título"].lower() == titulo_busca.lower()]
        if encontrados:
            print("\n".join(encontrados))
        else:
            print("Nenhum livro encontrado com esse título.")

    else:
        print("Opção inválida.")

def remover_livro():
    """Remover livro da biblioteca"""
    print("\n-----Remover livro-----")
    id_remover = int(input("Digite o ID do livro a ser removido: "))
    if id_remover in biblioteca:
        del biblioteca[id_remover]
        print("Livro removido com sucesso.")
    else:
        print("ID não encontrado.")

def main():
    while True:
        print("\n-----Menu-----")
        print("Esscolha a opção desejada: ")
        print("1. Cadastrar livro")
        print("2. Consultar livros")
        print("3. Remover livro")
        print("4. Encerrar programa")
        
        opcao = input(">>> ")
        
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            consultar_livros()
        elif opcao == "3":
            remover_livro()
        elif opcao == "4":
            print("Programa encerrado")
            break
        else:
            print("Opção inválida. Tente novamente.")

#mensagem de boas vindas
nome = "Amanda"
sobrenome = "Gualter"
print(f"Bem vindo a biblioteca {nome} {sobrenome}")
# Executar
main()