import java.util.*;
class Solution {
    static int DEFINE_SIZE = 10;
    static boolean flag;
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        // step1. 현재 want와 number를 사전에 저장
        Map<String, Integer>dict = new HashMap<>();
        for(int i=0; i<want.length; i++){
            dict.put(want[i], number[i]);
        }
        for(int i=0; i<=discount.length-DEFINE_SIZE; i++){ // N-10 N의 시간복잡도
            Map<String, Integer>dis = new HashMap<>();
            for(int j=i; j<i+DEFINE_SIZE; j++){ // O(1)의 시간복잡도(항상 상수)
                //할인정보를 딕셔너리에 넣기
                String key = discount[j];
                if(dis.getOrDefault(key, 0) == 0){
                    dis.put(key, 1);
                }else{
                    dis.put(key, dis.get(key)+1);
                }
            }
            // 검증 로직
            flag = false;
            dict.forEach((key, value) -> {
                if(dis.getOrDefault(key, -1) < value){
                    flag = true;
                }
            });
            if(flag == false){ //할인 받을 수 있다면 증가
                answer++;
            }
        }
        return answer;
    }
}
