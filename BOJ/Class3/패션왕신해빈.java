import java.util.*;
// import java.io.FileInputStream;
public class 패션왕신해빈 {

    public static int Factorial(int value){
        int result = 1;

        while (value != 0) {
            result *= value;
            value--;
        }
        return result;
    }

    public static void main(String args[]) throws Exception{
        // System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);

        int testcase = sc.nextInt();

        while (testcase != 0) {
            testcase-=1;
            // n만큼 사전에 저장
            int N = sc.nextInt();
            Map<String, Integer>dictionary = new HashMap<String, Integer>();

            // step.1 : 사전에 있다면 이전 value와 함께 추가
            for(int i=0; i<N; i++){ 
                String _value = sc.next(); // 입력만 받고 사용은 하지 않음
                String key = sc.next();

                if(dictionary.get(key) == null)
                    dictionary.put(key, 1);
                else
                    dictionary.put(key, (dictionary.get(key)+1));
            }

            // step.2 : Key, value에 맞게 계산 
            int answer = 1; 
            for(int value : dictionary.values()){
                // 조합식 안입는 경우도 포함해야 하므로 +1 nCr
                int n = value+1 ;
                int r = 1;
                // n! /(n-r)!* r!

                // r은 항상 1이므로 결국 n값만을 이용
                // answer *= Factorial(n) / Factorial(n-r) * Factorial(r);
                answer *= n;

            }
            // 맨몸의 경우는 제외해야 하므로 경우의 수 1 제외
            System.out.println(answer-1);
        }        
    }
    
}
