import java.util.*;

public class Edmonds {

    static class Aresta {
        int origem, destino, peso;

        public Aresta(int origem, int destino, int peso) {
            this.origem = origem;
            this.destino = destino;
            this.peso = peso;
        }
    }

    public static List<Aresta> algoritmoEdmonds(List<Aresta> arestas, int numVertices, int raiz) {
        List<Aresta> resultado = new ArrayList<>();
        int[] distancias = new int[numVertices];
        int[] predecessores = new int[numVertices];
        Arrays.fill(distancias, Integer.MAX_VALUE);
        Arrays.fill(predecessores, -1);
        distancias[raiz] = 0;

        for (int i = 0; i < numVertices - 1; i++) {
            for (Aresta aresta : arestas) {
                if (distancias[aresta.origem] + aresta.peso < distancias[aresta.destino]) {
                    distancias[aresta.destino] = distancias[aresta.origem] + aresta.peso;
                    predecessores[aresta.destino] = aresta.origem;
                }
            }
        }

        for (Aresta aresta : arestas) {
            if (distancias[aresta.origem] + aresta.peso < distancias[aresta.destino]) {
                throw new RuntimeException("O grafo contém um ciclo negativo.");
            }
            resultado.add(aresta);
        }

        return resultado;
    }

    public static void imprimirArvoreGeradoraMinima(List<Aresta> arvoreGeradoraMinima) {
        System.out.println("Árvore Geradora Mínima:");
        int qualidade = 0;

        for (Aresta aresta : arvoreGeradoraMinima) {
            //Nao gera a árvore pelo tempo de execução
            //System.out.println(aresta.origem + " -> " + aresta.destino + " Peso: " + aresta.peso); 
            qualidade += aresta.peso;
        }

        System.out.println("Qualidade da Árvore: " + qualidade);
    }

    public static void main(String[] args) {
        // Geração de um grafo totalmente conectado com pesos aleatórios
        List<Aresta> arestas = gerarGrafoCompleto(2500);

        // Execução do algoritmo de Edmonds
        long inicio = System.currentTimeMillis();
        List<Aresta> arvoreGeradoraMinima = algoritmoEdmonds(arestas, 2500, 0);
        long fim = System.currentTimeMillis();

        // Imprimir o tempo de execução
        System.out.println("Tempo de execução: " + (fim - inicio) + " milissegundos");

        // Imprimir a árvore geradora mínima e sua qualidade
        imprimirArvoreGeradoraMinima(arvoreGeradoraMinima);
    }

    // Função para gerar um grafo totalmente conectado com pesos aleatórios
    private static List<Aresta> gerarGrafoCompleto(int numVertices) {
        List<Aresta> arestas = new ArrayList<>();
        for (int i = 0; i < numVertices; i++) {
            for (int j = i + 1; j < numVertices; j++) {
                // Peso aleatório entre 1 e 10
                int peso = (int) (Math.random() * 10) + 1;
                arestas.add(new Aresta(i, j, peso));
            }
        }
        return arestas;
    }
}
