import java.util.*;
import java.io.*;
public class 문제추천시스템Version {
    public static class Problem implements Comparable<Problem>{
        int number;
        int level;

        public Problem(int number, int level){
            this.number = number;
            this.level = level;
        }

        @Override
        public int compareTo(Problem other){
            if (this.level == other.level){
                if(this.number < other.number)
                    return 1;
                return -1;
            }else{
                if(this.level < other.level)
                    return 1;
                return -1;
            }
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input[] = br.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        Map<Integer, Integer>dict = new HashMap<>();
        PriorityQueue<Problem>min_pq = new PriorityQueue<>();
        PriorityQueue<Problem>max_pq = new PriorityQueue<>(Comparator.reverseOrder());

        for(int i=0; i<N; i++){
            input = br.readLine().split(" ");
            int number = Integer.parseInt(input[0]);
            int level = Integer.parseInt(input[1]);

            if(dict.get(number) == null){
                dict.put(number, level);

            }else{
                dict.put(number, level);
            }
            min_pq.add(new Problem(number, level));
            max_pq.add(new Problem(number, level));
        }

        input = br.readLine().split(" ");
        int M = Integer.parseInt(input[0]);

        for(int i=0; i<M; i++){
            input = br.readLine().split(" ");
            String order = input[0];
            if(order.equals("add")){
                int number = Integer.parseInt(input[1]);
                int level = Integer.parseInt(input[2]);
                if(dict.get(number) == null){
                    dict.put(number, level);
                    min_pq.add(new Problem(number, level));
                    max_pq.add(new Problem(number, level));
                }else{
                    dict.put(number, level);
                    min_pq.add(new Problem(number, level));
                    max_pq.add(new Problem(number, level));
                }
            }else{
                if(order.equals("solved ")){
                    dict.remove(Integer.parseInt(input[1]));
                }else{
                    if(input[1].equals("-1")){
                        Problem problem = min_pq.peek();
                        if(dict.get(problem.number) != null && dict.get(problem.number) == problem.level){
                            min_pq.poll();
                        }else{
                            
                        }
                    }
                }

            }




        }

        bw.flush();
        bw.close();
    }
}