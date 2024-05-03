import java.util.*;
import java.io.*;

public class 케빈베이컨의법칙{

    public static int bfs(ArrayList<ArrayList<Integer>> graph, int sz, int start){
        Queue<Integer>queue = new LinkedList<>();
        int distance[] = new int[sz];
        for(int i=0; i<sz; i++) distance[i] = -1;
        distance[start] = 0;
        int ret = 0;
        
        queue.add(start);
        while(!queue.isEmpty()){
            int node = queue.poll();

            for(int i=0; i<graph.get(node).size(); i++){
                int edged_node = graph.get(node).get(i);

                if(distance[edged_node] == -1){
                    distance[edged_node] = distance[node]+1;
                    queue.add(edged_node);
                }
            }
        } // while
        for(int i=1; i<=sz-1; i++){
            ret+= distance[i];
        }
        // 연결된 
        return ret;
    }

    public static void myprint(ArrayList<ArrayList<Integer>> graph, int nodes){
        for(int i=0; i<=nodes; i++){
            System.out.print(i + " : ");
            for(int n : graph.get(i)){
                System.out.print(n + " ");
            }
            System.out.println();
        }
    }
    public static void main(String args[]) throws Exception{
        // System.setIn(new FileInputStream("input.txt"));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input[] = bf.readLine().split(" ");
        int nodes = Integer.parseInt(input[0]);
        int edges = Integer.parseInt(input[1]);

        
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i=0; i<=nodes; i++){
            graph.add(new ArrayList<>());
        }


        // 양방향 그래프 연결
        for(int i=0; i<edges; i++){
            input = bf.readLine().split(" ");
            int nodeA = Integer.parseInt(input[0]);
            int nodeB = Integer.parseInt(input[1]);

            graph.get(nodeA).add(nodeB);
            graph.get(nodeB).add(nodeA);
        }
        // myprint(graph, nodes);
        // 최단경로 탐색 시작
        int answer = Integer.MAX_VALUE;
        int answerIdx = -1;
    
        for(int i=1; i<=nodes; i++){
            int temp = bfs(graph, graph.size(), i);
            if(answer > temp){
                answer = temp;
                answerIdx = i;
            }
        }
        bw.write(answerIdx+"");
        bw.newLine();
        bw.flush();
        bw.close();
    }
}