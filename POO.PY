class Livro():
    livros = []
    Contador = 0
    def __init__(self,nome, autor):
        self.nome = nome
        self.autor = autor
        self.emprestado = False
        Livro.Contador += 1
        self.id = Livro.Contador

def cadastrar_livro ():
    nome_livro = input('Digite o nome do livro a ser cadastrado:')
    autor_livro = input('Digite o nome do autor do livro:')
    novo_livro = Livro(nome_livro,autor_livro)
    Livro.livros.append(novo_livro)
    print('Livro cadastrado com sucesso!!')

def mostra_livro_cadastrado():
    if not Livro.livros:
        print( "Não existem livros Cadastrados!!")
    else:
        for livro in Livro.livros:
            emprestado = ""
            if not livro.emprestado:
                emprestado = "Livro disponîvel"
            else:
                emprestado = "Livro emprestado"

            print(f"ID:{livro.id}  | Nome:{livro.nome} | Autor:{livro.autor} | Status do livro: {emprestado}")

def empresta_livro():
    if Livro.livros:
        mostra_livro_cadastrado()
        id_procurado = int(input("Digite o ID do livro que deseja emprestar:"))
        for livro in Livro.livros:
            if livro.id == id_procurado:
                if livro.emprestado == True:
                    print("Este livro já está emprestado!")
                else:
                    livro.emprestado = True
                    print("Livro emprestado com sucesso!")
                return
    
        print("Digite um ID válido de livro!")
    else:
        print("Você precisa cadastrar um livro primeiro!")

def devolver_livro():
    if Livro.livros:
            mostra_livro_cadastrado()
            id_procurado = int(input("Digite o ID do livro que deseja devolver:"))
            for livro in Livro.livros:
                if livro.id == id_procurado:
                    if livro.emprestado == True:
                        livro.emprestado = False
                        print("Livro devolvido com sucesso!")
                    else:
                        print("Este livro não está emprestado!")
                    return
        
            print("Digite um ID válido de livro!")
    else:
        print("Você precisa cadastrar um livro primeiro!")




while True:
    resposta = int(input("""
    ======================================================
    |                Cdastro de livros                   |
    ======================================================
    |                1 - Cadastrar Livros                |
    |                2 - Mostrar Livros Cadastrados      |
    |                3 - Enprestar Livro                 |
    |                4 - Devolver Livro                  |
    |                5 - Sair                            |
    ======================================================     
    Qual Opção deseja:        
    """))
    if resposta > 5 or resposta < 0:
        print("Digite um numero válido!")
    elif resposta == 1 :
        cadastrar_livro()

    elif resposta == 2 :
        mostra_livro_cadastrado()

    elif resposta == 3 :
        empresta_livro()

    elif resposta == 4 :
        devolver_livro()

    elif resposta == 5:
        break

