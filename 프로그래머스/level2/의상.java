import java.util.*;

class Solution {
    static int ans; 
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer>dict = new HashMap<>();
        System.out.println(clothes.length);
        
        for(int i=0; i<clothes.length; i++){
            String category = clothes[i][1];
            
            if(dict.getOrDefault(category, 0) == 0){
                dict.put(category, 1);
            }
            else{
                dict.put(category, dict.get(category) +1);
            }
        }
        ans=1;
        dict.forEach((key, value) -> {
           ans *= (value+1);  // 자기 자신도 포함
        });
        
        answer = ans-1; // 아무런 옷도 입지않은 상태는 제거
        
        return answer;
    }
}
