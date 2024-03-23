import java.util.*;
public class 소수찾기 {

    public static boolean isPrime(int number){
        if(number <=1){
            return false;
        }
        // 1보다 작은 숫자들 처리
        for (int i =2; i<number; i++){
            // 자기 자신을 제외하고 나눠지는 수가 있다면 소수가 아님.
            if (number %i ==0){
                return false;
            }
        }
        return true;
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();

        ArrayList<Integer> numbers = new ArrayList<>();
        for (int i=0; i<number; i++){
            numbers.add(sc.nextInt());
        }

        long answer = 0;
        for (int i=0; i<number; i++){
            if(isPrime(numbers.get(i)) == true){
                answer +=1;
            }
        }

        System.out.println(answer);
    }
}
