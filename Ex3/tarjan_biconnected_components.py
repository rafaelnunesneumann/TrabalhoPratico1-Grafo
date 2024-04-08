import networkx as nx
from tarjan import tarjan
import time

def nx_to_tarjan_graph(G):
    # Converter o grafo networkx em um formato compatível com tarjan
    tarjan_graph = {}
    for u, v in G.edges():
        if u not in tarjan_graph:
            tarjan_graph[u] = []
        if v not in tarjan_graph:
            tarjan_graph[v] = []
        tarjan_graph[u].append(v)
        tarjan_graph[v].append(u)
    return tarjan_graph

def main():
    # Parâmetros do grafo aleatório
    num_vertices = 100000
    num_edges = num_vertices * 2  # Determinando o número de arestas

    # Gerar um grafo aleatório com o número especificado de vértices
    G = nx.gnm_random_graph(num_vertices, num_edges, directed=False)

    # Converter o grafo networkx em um formato compatível com tarjan
    tarjan_graph = nx_to_tarjan_graph(G)

    # Medir o tempo de execução
    start_time = time.time()

    # Encontrar componentes biconexos no grafo gerado usando o algoritmo de Tarjan
    biconnected_components = tarjan(tarjan_graph)

    end_time = time.time()
    execution_time = end_time - start_time

    # Nome do arquivo de saída
    output_filename = "ex3-100000.out"

    # Escrever os componentes biconexos no arquivo de saída
    with open(output_filename, 'w') as f:
        f.write("Componentes biconexos:\n")
        for component in biconnected_components:
            f.write(f"{component}\n")
        f.write(f"\nTempo de execucao (segundos): {execution_time:.8f}\n")

    print(f"Os componentes biconexos foram salvos em '{output_filename}'.")

if __name__ == "__main__":
    main()
