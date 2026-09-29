from src.grafo import Grafo
from src.articulacao import encontra_articulacao, eh_articulacao


def menu():

    print("========================================")
    print("         ANÁLISE DE REDE SOCIAL")
    print("========================================")
    print("1 - Informar ordem do grafo")
    print("2 - Informar tamanho do grafo")
    print("3 - Calcular densidade")
    print("4 - Informar vizinhos de um vértice")
    print("5 - Informar grau de um vértice")
    print("6 - Verificar se um vértice é articulação")
    print("0 - Sair")
    print("========================================")


arquivo = input("Digite o nome do arquivo do grafo: ")

grafo = Grafo(arquivo)

while True:

    menu()

    opcao = input("Digite a opção: ")

    if opcao == "1":

        print("Ordem do grafo:", grafo.ordem())

    elif opcao == "2":

        print("Tamanho do grafo:", grafo.tamanho())

    elif opcao == "3":

        print("Densidade do grafo:", grafo.densidade())

    elif opcao == "4":

        vertice = int(input("Digite o vértice: "))

        print("Vizinhos:", grafo.vizinhos(vertice))

    elif opcao == "5":

        vertice = int(input("Digite o vértice: "))

        print("Grau:", grafo.grau(vertice))

    elif opcao == "6":

        vertice = int(input("Digite o vértice: "))

        if eh_articulacao(grafo, vertice):
            print("O vértice", vertice, "é articulação.")
        else:
            print("O vértice", vertice, "não é articulação.")

    elif opcao == "0":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")