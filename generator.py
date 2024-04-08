import networkx as nx
import random

def main():
    # Parâmetros do grafo aleatório
    num_vertices = 100
    num_edges = num_vertices * 2  # Determinando o número de arestas

    # Criando um grafo aleatório com 'num_vertices' vértices e 'num_edges' arestas
    G = nx.gnm_random_graph(num_vertices, num_edges)

    # Obtendo a lista de arestas do grafo
    edges = list(G.edges())

    # Nome do arquivo para salvar o grafo
    output_file = "grafo_aleatorio.txt"

    # Escrevendo as informações do grafo no arquivo
    with open(output_file, 'w') as file:
        # Escrevendo o número de vértices e arestas no arquivo
        file.write(f"{num_vertices} {len(edges)}\n")

        # Escrevendo cada aresta no arquivo
        for edge in edges:
            file.write(f"{edge[0]} {edge[1]}\n")

    print(f"Grafo aleatório gerado e salvo em '{output_file}'.")

if __name__ == "__main__":
    main()
