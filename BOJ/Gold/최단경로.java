import java.util.*;
import java.io.*;
public class 최단경로 {

    static class Node implements Comparable<Node>{
        int node;
        int weight;

        public Node(int node, int weight){
            this.node = node;
            this.weight = weight;
        }
        @Override
        public int compareTo(Node other){
            return Integer.compare(weight, other.weight);
        }
        
    }

    static List<List<Node>>graph;
    static boolean visit[];
    static int distance[];
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input[] = br.readLine().split(" ");
        int V = Integer.parseInt(input[0]);
        int E = Integer.parseInt(input[1]);

        input = br.readLine().split(" ");
        int start = Integer.parseInt(input[0]);
        graph = new ArrayList<>();
        for(int i=0; i<= V; i++){
            graph.add(new ArrayList<>());
        }

        for(int i=0; i<E; i++){
            input = br.readLine().split(" ");
            int from = Integer.parseInt(input[0]);
            int to = Integer.parseInt(input[1]);
            int weight = Integer.parseInt(input[2]);

            graph.get(from).add(new Node(to, weight));
        }
        // 그래프 표현 

        // 최단거리 배열 생성
        distance = new int[V+1];
        visit = new boolean[V+1];
        for(int i=1; i<=V; i++){
            distance[i] = Integer.MAX_VALUE;
            visit[i] = false;
        }
        distance[start] = 0;

        shortestPath(start);
        for(int i=1; i<=V; i++){
            if(distance[i] != Integer.MAX_VALUE){
                bw.write(String.valueOf(distance[i]));
            }else{
                bw.write("INF");
            }
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
    static void shortestPath(int start){
        // 우선순위 큐 선언
        PriorityQueue<Node>pq  = new PriorityQueue<>();
        pq.add(new Node(start, 0));
        visit[start] = true;

        while(!pq.isEmpty()){
            Node n = pq.poll();
            if(distance[n.node] < n.weight)
                continue;
            
            for(int i=0; i<graph.get(n.node).size(); i++){
                int cost = n.weight + graph.get(n.node).get(i).weight;

                if(cost < distance[graph.get(n.node).get(i).node]){
                    distance[graph.get(n.node).get(i).node] = cost;
                    pq.add(new Node(graph.get(n.node).get(i).node, cost));
                }
            }
            
        }


    }
}
