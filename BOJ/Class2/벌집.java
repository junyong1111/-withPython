import java.util.*;

public class 벌집 {
    public static int SIX = 6;
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int start = 1;
        int turn = 1;

        while (true){
            if(start >= N){
                System.out.println(turn);
                break;
            }
            start = start + (SIX* turn);
            turn +=1;
        }
    }
    
}
