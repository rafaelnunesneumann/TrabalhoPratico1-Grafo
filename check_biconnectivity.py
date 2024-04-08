from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx
import time

def find_biconnected_components(G):
    # Encontrar os componentes biconexos no grafo
    biconnected_components = list(nx.biconnected_components(G))
    return biconnected_components

def find_disjoint_paths(G, component):
    # Encontrar arestas de corte (bridges) no componente biconexo
    bridges = list(nx.bridges(G.subgraph(component)))

    # Para cada par de vértices no componente, encontrar um caminho
    # que não utilize nenhuma das arestas de corte (bridges)
    disjoint_paths = []
    for u in component:
        for v in component:
            if u != v:
                # Encontrar um caminho entre u e v que não utilize bridges
                try:
                    path = nx.shortest_path(G, source=u, target=v)
                    if all((u, v) not in bridges for u, v in zip(path, path[1:])):
                        disjoint_paths.append(path)
                except nx.NetworkXNoPath:
                    continue

    return disjoint_paths

def main():
    # Número de vértices desejado para o grafo
    num_vertices = 1000

    # Gerar o grafo aleatório
    p = 0.3
    G = erdos_renyi_graph(num_vertices, p)

    # Medir o tempo de execução da função find_biconnected_components
    start_time = time.time()
    biconnected_components = find_biconnected_components(G)

    # Salvar o output no arquivo de saída
    output_filename = "ex1-1000.out"
    with open(output_filename, 'w') as f:
        # Para cada componente biconexo, encontrar e salvar os caminhos disjuntos
        f.write("Componentes Biconexos:\n")
        for component in biconnected_components:
            f.write(f"Componente: {component}\n")
            disjoint_paths = find_disjoint_paths(G, component)
            f.write("Caminhos Disjuntos:\n")
            for path in disjoint_paths:
                f.write(f"{path}\n")
            f.write("\n")
        end_time = time.time()
        execution_time = end_time - start_time
        f.write(f"Tempo de execucao (segundos): {execution_time}\n\n")

    print(f"Resultado salvo em '{output_filename}'")

if __name__ == "__main__":
    main()
