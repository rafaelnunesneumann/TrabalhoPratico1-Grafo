import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Tarjan {
    static class Edge implements Comparable<Edge> {
        int src, dest, weight;

        public Edge(int src, int dest, int weight) {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.weight, other.weight);
        }
    }

    static class UnionFind {
        int[] parent, rank;

        public UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                rank[i] = 0;
            }
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);

            if (rootX != rootY) {
                if (rank[rootX] > rank[rootY]) {
                    parent[rootY] = rootX;
                } else if (rank[rootX] < rank[rootY]) {
                    parent[rootX] = rootY;
                } else {
                    parent[rootY] = rootX;
                    rank[rootX]++;
                }
            }
        }
    }

    // Função para gerar um grafo totalmente conectado com pesos aleatórios
    private static List<Edge> gerarGrafoCompleto(int numVertices) {
        List<Edge> arestas = new ArrayList<>();
        for (int i = 0; i < numVertices; i++) {
            for (int j = i + 1; j < numVertices; j++) {
                // Peso aleatório entre 1 e 10
                int peso = (int) (Math.random() * 10) + 1;
                arestas.add(new Edge(i, j, peso));
            }
        }
        return arestas;
    }

    public static List<Edge> kruskal(List<Edge> edges, int numVertices) {
        List<Edge> minimumSpanningTree = new ArrayList<>();
        UnionFind uf = new UnionFind(numVertices);
        Collections.sort(edges);

        for (Edge edge : edges) {
            int rootSrc = uf.find(edge.src);
            int rootDest = uf.find(edge.dest);

            if (rootSrc != rootDest) {
                minimumSpanningTree.add(edge);
                uf.union(rootSrc, rootDest);
            }
        }

        return minimumSpanningTree;
    }

    public static void main(String[] args) {
        List<Edge> edges = gerarGrafoCompleto(2500);

        long inicio = System.currentTimeMillis();
        List<Edge> minimumSpanningTree = kruskal(edges, 2500);
        long fim = System.currentTimeMillis();

        // Imprimir o tempo de execução
        System.out.println("Tempo de execução: " + (fim - inicio) + " milissegundos");

        int qualidade = 0;
        System.out.println("Árvore Geradora Mínima:");
        for (Edge edge : minimumSpanningTree) {
            System.out.println(edge.src + " -> " + edge.dest + " Peso: " + edge.weight);
            qualidade += edge.weight;
        }
        System.out.println("Qualidade da Árvore: " + qualidade);

    }
}
