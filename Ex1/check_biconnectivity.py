import networkx as nx
import random
import time

def create_random_graph(num_vertices):
    """ Cria um grafo aleatório com o número especificado de vértices. """
    
    k = 2  # Grau médio dos nós
    p = 0.1  # Probabilidade de reorganização das arestas

    G = nx.connected_watts_strogatz_graph(num_vertices, k, p)

    return G

def find_biconnected_components(G):
    """ Encontra os blocos biconexos no grafo G. """
    return [tuple(component) for component in nx.biconnected_components(G)]

def has_disjoint_paths(G, component):
    """ Verifica se existem caminhos disjuntos dentro do componente biconexo. """
    result = False

    nodes = list(component)
    n = len(nodes)
    
    # Verificar todas as combinações de pares de vértices dentro do componente
    for i in range(n):
        for j in range(i + 1, n):
            disjoint_paths = nx.node_disjoint_paths(G, nodes[i], nodes[j])
            if disjoint_paths:
                result = True  # Existe pelo menos um par de vértices sem caminho conectando-os    
    return result,

def save_results_to_file(filename, biconnected_components, has_disjoint_paths, execution_time):
    """ Salva os resultados em um arquivo especificado pelo usuário. """
    with open(filename, 'w') as f:
        f.write(f"Tempo total de execucao: {execution_time:.6f} segundos\n\n")
        for idx, component in enumerate(biconnected_components):
            f.write(f"Bloco Biconexo {idx + 1}: {component}\n")
            f.write(f"Possui caminhos disjuntos: {has_disjoint_paths[idx][0]}\n")
            f.write("\n")

def main():
    num_vertices = 100000
    output_file = "ex1-100000.out" 
    
    # Criar o grafo aleatório
    G = create_random_graph(num_vertices)
    
    # Início da medição do tempo de execução
    start_time = time.time()
    
    # Encontrar os blocos biconexos
    biconnected_components = find_biconnected_components(G)
    
    # Verificar se cada bloco biconexo possui caminhos disjuntos e quais vértices não têm caminhos disjuntos
    has_disjoint_paths_list = []
    for component in biconnected_components:
        has_disjoint_paths_list.append(has_disjoint_paths(G, component))
    
    # Fim da medição do tempo de execução
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Salvar os resultados no arquivo especificado
    save_results_to_file(output_file, biconnected_components, has_disjoint_paths_list, execution_time)
    print(f"Resultados salvos em: {output_file}")

if __name__ == "__main__":
    main()
