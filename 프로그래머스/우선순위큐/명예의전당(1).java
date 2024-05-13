import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer;
        PriorityQueue<Integer>pq = new PriorityQueue<>();
        ArrayList<Integer>s = new ArrayList<>();
        
        for(int i=0; i<score.length; i++){
            // step1. K날짜 만큼은 그냥 넣어줌
            if(i < k){
                pq.add(score[i]);
                if(score[i] <= pq.peek())
                    s.add(score[i]);
                else
                    s.add(pq.peek());
            }
            // step2. 명예의 전당 밀어내기
            // 현재 들어온 값이 명예의 전당안에 있는 최솟값보다 크다면 밀어내기
            else{
                if(score[i] >= pq.peek()){
                    pq.poll();
                    pq.add(score[i]);
                    s.add(pq.peek());
                }
                else{
                    s.add(pq.peek());
                }
            }
        }
        answer = new int[s.size()];
        for(int i=0; i<s.size(); i++)
            answer[i] = s.get(i);
        return answer;
    }
}