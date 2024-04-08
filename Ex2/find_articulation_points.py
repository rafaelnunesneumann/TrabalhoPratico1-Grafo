import networkx as nx
import random
import time

def generate_random_graph_with_articulation_points(num_vertices):
    num_edges = num_vertices * 2
    G = nx.gnm_random_graph(num_vertices, num_edges, directed=False)
    num_articulation_points = random.randint(2, num_vertices // 2)
    articulation_points = random.sample(list(G.nodes()), num_articulation_points)
    for node in articulation_points:
        G.add_node(node)  

    return G

def check_component_connectivity(G, nodes):
    # Verifica a conectividade apenas dos nós fornecidos (componente específico)
    subgraph = G.subgraph(nodes)
    return nx.is_connected(subgraph)

def find_and_output_articulation_points_with_removals(G):
    start_time = time.time()
    original_graph = G.copy()
    articulation_points = list(nx.articulation_points(G))
    
    with open('ex2-10000.out', 'a') as f:
        f.write("Initial Articulation Points:\n")
        f.write(f"{articulation_points}\n\n")
        
        # Verifica a conectividade dos componentes que incluem os pontos de articulação originais
        initial_component_connectivity_results = []
        for articulation_point in articulation_points:
            component_nodes = list(nx.node_connected_component(original_graph, articulation_point))
            is_connected = check_component_connectivity(original_graph, component_nodes)
            initial_component_connectivity_results.append(is_connected)
        
        f.write("Initial Articulation Points Connectivity:\n")
        f.write(f"{initial_component_connectivity_results}\n\n")
    
    for articulation_point in articulation_points:
        G_removed = G.copy()
        G_removed.remove_node(articulation_point)
        
        articulation_points_removed = list(nx.articulation_points(G_removed))
        
        if articulation_point in G_removed:
            # Encontra o componente conectado que inclui o ponto de articulação removido
            component_nodes = list(nx.node_connected_component(G_removed, articulation_point))
            is_connected = check_component_connectivity(G_removed, component_nodes)
        else:
            # Se o ponto de articulação não estiver mais no grafo, componente está vazio ou desconectado
            is_connected = False
        
        with open('ex2-100000.out', 'a') as f:
            f.write(f"Removed articulation point {articulation_point}:\n")
            f.write(f"New Articulation Points: {articulation_points_removed}\n")
            f.write(f"Component Connectivity: {is_connected}\n\n")
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    with open('ex2-100000.out', 'a') as f:
        f.write(f"Total Execution Time: {execution_time:.6f} seconds\n")
    
    return execution_time

if __name__ == "__main__":
    num_vertices = 100000
    graph = generate_random_graph_with_articulation_points(num_vertices)
    execution_time = find_and_output_articulation_points_with_removals(graph)
