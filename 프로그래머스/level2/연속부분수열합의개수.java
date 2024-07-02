import java.util.*;
class Solution {
    static int getTotal(int[] elements){
        int sum = 0;
        for(int i=0; i<elements.length; i++){
            sum += elements[i];
        }
        return sum;
    }
    public int solution(int[] elements) {
        Queue<Integer>prefixSumQueue = new LinkedList<>();
        Queue<Integer>prefixQueue = new LinkedList<>();
        
        int sz = elements.length;
        for(int i=0; i<sz; i++){
            prefixSumQueue.add(elements[i]);
            prefixQueue.add(elements[i]);
        }
        int answer = 0;
        
        Map<Integer, Integer>dict = new HashMap<>();
        for(int len = 0; len<sz-1; len++){ // 수열의 길이만큼(마지막은 1개 추가니깐 따로 처리)
            
            for(int i=0; i<sz; i++){ // 큐를 돌면서 처리
                int e = elements[i];
                if(len == 0) { // 처음은 따로 처리
                    if(dict.get(e) == null)
                        dict.put(e, 1);
                }else{ // 처음이 아닌 경우
                    int sum =  prefixQueue.peek() + prefixSumQueue.poll();
                    prefixSumQueue.add(sum);
                    prefixQueue.add(prefixQueue.poll());
                    
                    if(dict.get(sum) == null){
                        dict.put(sum, 1);
                    }
                }
            }
            // 큐 한칸 전진
            prefixQueue.add(prefixQueue.poll());
        }
        // 마지막은 전체 합
        int sum = getTotal(elements);
       
        if(dict.get(sum) == null)
            dict.put(sum, 1);
        answer = dict.size();
        return answer;
    }
}
