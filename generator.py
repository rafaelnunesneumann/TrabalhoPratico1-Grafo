from networkx.generators.random_graphs import erdos_renyi_graph

def generate_random_graph(num_vertices, filename):
    p = 0.0001
    g = erdos_renyi_graph(num_vertices, p)
    with open(filename, 'w') as file:
        file.write(f"{num_vertices} {len(g.edges)}")

        for idx, (u, v) in enumerate(g.edges):
            file.write(f"\n{u} {v}")

    print(f"Grafo com {num_vertices} vértices e {len(g.edges)} arestas foi salvo em '{filename}'.")

# Número de vértices desejado
num_vertices = 10000

# Nome do arquivo de saída
output_filename = "grafo_aleatorio-100000.txt"

# Gera o grafo aleatório e salva no arquivo
generate_random_graph(num_vertices, output_filename)
