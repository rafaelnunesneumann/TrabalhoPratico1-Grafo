import networkx as nx
import time

def find_biconnected_components(G):
    return list(nx.biconnected_components(G))

def find_disjoint_paths(G, component):
    bridges = list(nx.bridges(G.subgraph(component)))
    disjoint_paths = []
    
    for u in component:
        for v in component:
            if u != v:
                try:
                    path = nx.shortest_path(G, source=u, target=v)
                    if all((u, v) not in bridges for u, v in zip(path, path[1:])):
                        disjoint_paths.append(path)
                except nx.NetworkXNoPath:
                    continue
    
    return disjoint_paths

def find_blocks(G, biconnected_components):
    blocks = []
    
    for component in biconnected_components:
        disjoint_paths = find_disjoint_paths(G, component)
        
        for path in disjoint_paths:
            # Verifica se o caminho forma um bloco
            subgraph = G.subgraph(path)
            if nx.is_biconnected(subgraph):  # O caminho forma um bloco
                blocks.append(subgraph.edges())
    
    return blocks

def main():
    num_vertices = 1000
    num_edges = num_vertices * 2

    G = nx.gnm_random_graph(num_vertices, num_edges, directed=False)

    start_time = time.time()
    biconnected_components = find_biconnected_components(G)
    
    output_filename = "ex1-100.out"
    with open(output_filename, 'w') as f:
        f.write("Blocos Encontrados:\n")
        blocks = find_blocks(G, biconnected_components)
        for i, block_edges in enumerate(blocks):
            f.write(f"Bloco {i + 1}:\n")
            for edge in block_edges:
                f.write(f"{edge}\n")
            f.write("\n")
        
        end_time = time.time()
        execution_time = end_time - start_time
        f.write(f"Tempo de execucao (segundos): {execution_time}\n\n")

    print(f"Resultado salvo em '{output_filename}'")

if __name__ == "__main__":
    main()
