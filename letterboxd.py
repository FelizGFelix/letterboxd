import os

filmes = []
nota_permitidas = [1, 2, 3, 4, 5]

def limpar():

    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def voltar():

    print("----------------")
    print("Digite uma opção válida")
    input("Digite qualquer tecla para voltar: ")
    limpar()
    main()

def voltar_correto():

    print("----------------")
    input("Digite qualquer tecla para voltar: ")
    limpar()
    main()

def adicionar_filme():

    limpar()
    nome_filme = input("Digite o nome do filme: ")
    nota_filme = int(input("Digite a nota do filme: "))
    if nota_filme not in nota_permitidas:
        print("Só são permitidas notas de 1, 2, 3, 4 ou 5")
        input("Digite qualquer tecla para voltar: ")
        limpar()
        adicionar_filme()

    review_filme = input("Digite a review do filme: ")


    filme = {
        "nome" : nome_filme,
        "nota" : nota_filme,
        "review" : review_filme
    }

    filmes.append(filme)

    voltar_correto()
    return filme

def lista_filme():

    limpar()
    for i in filmes:
        print("----------------")
        print("Nome do filme: ", i["nome"])
        print("Nota do filme: ", i["nota"])
        print("Review do filme: ", i["review"])

    voltar_correto()


def main():
    resposta = ""
    
    try: 
        while resposta != 3:
            resposta = int(input("Selecione uma das opções abaixo:\n 1 - Adicionar filmes a sua conta\n 2 - Acessar sua lista de filmes\n 3 - Sair\n-> "))

            if resposta == 1:
                adicionar_filme()

            elif resposta == 2:
                lista_filme()

            elif resposta == 3:
                limpar()
                print("Saindo do programa...")
                break

            else:
                voltar()

    except:
        voltar()


if __name__ == "__main__":
    main()

