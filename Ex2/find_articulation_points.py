import networkx as nx
import random
import time

def create_articulation_graph(num_vertices, output_file):
    start_time = time.time()  # Marca o início do tempo de execução

    # Cria um grafo inicial com 'num_vertices'
    G = nx.Graph()

    # Adiciona 'num_vertices' nós ao grafo
    G.add_nodes_from(range(num_vertices))

    # Adiciona arestas para garantir conectividade
    for i in range(num_vertices - 1):
        G.add_edge(i, i + 1)

    # Calcula o número mínimo de pontos de articulação desejados (pelo menos 10%)
    min_articulation_points = max(1, num_vertices // 10)  # Pelo menos 1 ponto de articulação

    # Adiciona arestas extras para introduzir pontos de articulação
    while len(list(nx.articulation_points(G))) < min_articulation_points:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v:
            G.add_edge(u, v)

    # Verifica se o grafo é conexo
    is_connected = nx.is_connected(G)
    
    # Encontra todos os nós do grafo (possíveis pontos de articulação)
    all_nodes = list(G.nodes())
    
    # Seleciona aleatoriamente 'min_articulation_points' nós como pontos de articulação
    articulation_points = random.sample(all_nodes, min_articulation_points)
    
    # Salva os resultados iniciais no arquivo de saída
    with open(output_file, 'w') as f:
        f.write(f'Grafo é conexo: {is_connected}\n')
        f.write(f'Pontos de articulação iniciais: {articulation_points}\n\n')

    # Para cada ponto de articulação, remove-o e verifica a conectividade
    for articulation_point in articulation_points:
        # Remove o ponto de articulação do grafo
        G.remove_node(articulation_point)
        
        # Verifica se o grafo sem o ponto de articulação ainda é conexo
        is_still_connected = nx.is_connected(G)

        # Calcula o tempo de execução após a remoção do ponto de articulação
        
        # Salva o resultado da remoção no arquivo de saída
        with open(output_file, 'a') as f:
            f.write(f'Removendo ponto de articulação {articulation_point}:\n')
            f.write(f'Grafo ainda é conexo: {is_still_connected}\n')


    # Verifica se o grafo sem os pontos de articulação ainda é conexo
    is_still_connected = nx.is_connected(G)

    # Calcula o tempo total de execução
    total_execution_time = time.time() - start_time

    # Salva o resultado final no arquivo de saída
    with open(output_file, 'a') as f:
        f.write(f'Grafo ainda é conexo após todas as remoções: {is_still_connected}\n')
        f.write(f'Tempo total de execução: {total_execution_time:.6f} segundos\n')

if __name__ == "__main__":
    num_vertices = 100000  # Número de vértices no grafo
    output_filename = 'ex2-100000.txt'  # Nome do arquivo de saída
    create_articulation_graph(num_vertices, output_filename)
