import java.util.*;

class Solution {
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        
        // step1. 반복문
        int number = -1;
        int turn = 0;
        while(true){
            // step2.  0부터 숫자 증가 후 해당 숫자를 n진수로 변환
            number++;
            String base = Integer.toString(number, n).toUpperCase();
            // base 길이만큼 순회
            for(int i=0; i<base.length(); i++){
                if((turn%m)+1 ==p) // 자신의 턴인경우 추가
                    answer += base.charAt(i);
                if(answer.length() == t) // 원하는 길이가 나오면 종료
                    return answer;
                turn++;
            }      
        }
    }
}
