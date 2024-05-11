import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        ArrayList<Integer>temp = new ArrayList<>();
        Queue<Integer>max_queue = new LinkedList<>();
        Queue<Integer>priori_queue = new LinkedList<>();
        Queue<Integer>index_queue = new LinkedList<>();
        ArrayList<Integer>answer_list = new ArrayList<>();
        
        for(int i=0; i<priorities.length; i++){
            priori_queue.add(priorities[i]);
            index_queue.add(i);
            temp.add(priorities[i]);
        }
        temp.sort(Comparator.reverseOrder());
        for(int i=0; i<temp.size(); i++)
            max_queue.add(temp.get(i));
        
        
        while(!index_queue.isEmpty()){
            // step1. 가장 높은 우선순위의 경우
            if(max_queue.peek() == priori_queue.peek()){
                answer_list.add(index_queue.poll());
                priori_queue.poll();
                max_queue.poll();
            }
            // step2. 우선순위가 가장 높지 않은 경우
            else{
                index_queue.add(index_queue.poll());
                priori_queue.add(priori_queue.poll());
            }
        }
        
        // 정답 인덱스를 순회하면서 로케이션에 맞게 반환
        int answer = 0;
        for(int i=0; i<answer_list.size(); i++){
            if(answer_list.get(i) == location){
                answer = i+1;
                break;
            }
        }
        
        return answer;
    }
}