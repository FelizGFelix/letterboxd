import os

nota0 = []
nota05 = []
nota1 = []
nota15 = []
nota2 = []
nota25 = []
nota3 = []
nota35 = []
nota4 = []
nota45 = []
nota5 = []

def clear_screen():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def main():
    print("Bem-vindo ao Letterboxd!")
    opcao = ""
    while opcao != 3:
        opcao = int(input("Qual opção deseja acessar?\n 1 - adicionar filmes a sua conta\n 2 - acessar notas da sua conta\n 3 - sair-> "))
        if opcao == 1:
            cadastrar_filme()
        
        elif opcao == 2:
            imprime_filmes()

        elif opcao == 3:
            clear_screen()
            print("Saindo do programa")
            break

        else:
            print("Valor inválido")
            input("Escreva qualquer valor para voltar: ")
            clear_screen()

def cadastrar_filme():
    filmenovo = input("Escreva o nome do filme: ")
    notafilmenovo = float(input("Escreva a nota desse filme: "))

    if notafilmenovo == 0:
        nota0.append(filmenovo)
        print(f"A nota do {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 0.5:
        nota05.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 1:
        nota1.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 1.5:
        nota15.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 2:
        nota2.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 2.5:
        nota25.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 3:
        nota3.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 3.5:
        nota35.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 4:
        nota4.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 4.5:
        nota45.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif notafilmenovo == 5:
        nota5.append(filmenovo)
        print(f"A nota de {filmenovo} é {notafilmenovo}")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    else:
        print("Só são aceitas notas de:\n0\n0.5\n1\n1.5\n2\n2.5\n3\n3.5\n4\n4.5\n5")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

def imprime_filmes():
    
    resposta = float(input("Qual lista de filme deseja acessar?: "))

    if resposta == 0:
        print(nota0)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif resposta == 0.5:
        print(nota05)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif resposta == 1:
        print(nota1)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()
            
    elif resposta == 1.5:
        print(nota15)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif resposta == 2:
        print(nota2)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif resposta == 2.5:
        print(nota25)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif resposta == 3:
        print(nota3)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif resposta == 3.5:
        print(nota35)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif resposta == 4:
        print(nota4)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif resposta == 4.5:
        print(nota45)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    elif resposta == 5:
        print(nota5)
        input("Escreva qualquer valor para voltar: ")
        clear_screen()

    else:
        print("Só existem listas de de:\n0\n0.5\n1\n1.5\n2\n2.5\n3\n3.5\n4\n4.5\n5")
        input("Escreva qualquer valor para voltar: ")
        clear_screen()
       
if __name__ == "__main__":
    main()