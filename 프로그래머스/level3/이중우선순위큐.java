import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        // step1. 반복문을 돌면서 연산 수행
        for(int i=0; i<operations.length; i++){
            String input[]  = operations[i].split(" ");
            
            // 연산과 value로 나누고
            String order = input[0];
            int value = Integer.parseInt(input[1]);

            // 각각 따로 처리
            if(order.equals("I")){
                pq.add(value);
            } 
            else if(!pq.isEmpty() &&order.equals("D")){
                if(value == 1){ // 최댓값 연산
                    pq.remove(Collections.max(pq));
                }else pq.remove(Collections.min(pq));// 최솟값 연산
            } 
        } // for
        
        
        
        if(pq.isEmpty()){ // pq가 비었으면 0
            answer[0] = 0;
            answer[1] = 0;
            return answer;
        }
        // 정답 옮겨담고 최댓값 최솟값
        List<Integer>ans = new ArrayList<>();
        while(!pq.isEmpty())
            ans.add(pq.poll());
        answer[0] = ans.get(ans.size()-1); 
        answer[1] = ans.get(0);
        
        return answer;
    }
}