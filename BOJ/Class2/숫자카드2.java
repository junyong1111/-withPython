import java.lang.reflect.Array;
import java.util.*;
class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int [] data = new int[N+1];
        for (int i=0; i<N; i++){
            data[i] = sc.nextInt();
        }

        HashMap<Integer, Integer>numbers = new HashMap<>();
        
        System.out.println(numbers.get(1));

        for(int i=0; i<N; i++){
            if(numbers.get(data[i]) == null)
                numbers.put(data[i], 1);
            else
                numbers.put(data[i], numbers.get(data[i]) +1);
        }

        int M = sc.nextInt();
        int [] targets = new int[M];

        for(int i=0; i<M; i++){
            targets[i] = sc.nextInt();
        }

        for(int i=0; i<M; i++){
            if(numbers.containsKey(targets[i])){
                System.out.print(numbers.get(targets[i]));
            }
            else
                System.out.print(0);
            System.out.print(" ");
        }
 
    }
}
