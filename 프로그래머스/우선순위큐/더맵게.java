import java.util.*;

class Solution {
    
    public int makeScoville(int first, int second){
        return first + (second *2);
    }
    public int solution(int[] scoville, int K) {
        // 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 *2)
        PriorityQueue<Integer>pq = new PriorityQueue<>();
        
        for(int i=0; i<scoville.length; i++){
            pq.add(scoville[i]);
        }
        
        
        int answer = 0;
        
        
        // step1. 우선순위큐를 순회
        while(!pq.isEmpty()){
            // step2. 만약 스코빌 지수를 만족한다면 패스
            if(pq.peek() >= K){
                return answer;
            }
            
            // step3. 새로운 스코빌 지수 만들기  
            // 그렇게 하기 위해서는 우선 2개를 pop 해야함
            int first = pq.poll();
            if(pq.isEmpty()){break;}
            int second = pq.poll();
        
            pq.add(makeScoville(first, second));
            answer ++; 
        }
        // step4. 반복문으로 해결이 안되었다면 그냥 답 없음
        answer = -1;
        return answer;
    }
}
