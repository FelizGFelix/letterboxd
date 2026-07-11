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

def voltar_correto():
    print("----------------")
    input("Digite qualquer tecla para voltar: ")
    limpar()

def adicionar_filme():
    limpar()
    class Filme():
        def __init__(self):
            self.filme = ""
            self.nota = 0
            self.review = ""

        def preencher(self):
            self.filme = input("Digite o nome do filme: ")
            self.nota = int(input("Digite a nota do filme: "))
            self.review = input("Digite a review do filme: ")


            if self.nota not in nota_permitidas:
                print("Nota inválida, só são permitidas notas de 1 a 5: ")
                self.nota = int(input("Insira a nota novamente: "))


            filme = {
                "nome" : self.filme,
                "nota" : self.nota,
                "review" : self.review
                }

            filmes.append(filme)


    adicionar = Filme()
    adicionar.preencher()

    voltar_correto()
    return filmes
        

def lista_filme():

    limpar()
    for i in filmes:
        print("----------------")
        print("Nome do filme: ", i["nome"])
        print("Nota do filme: ", i["nota"])
        print("Review do filme: ", i["review"])

    voltar_correto()


def main():
    resposta = 0
    
    while resposta != 3:
            
        try:
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