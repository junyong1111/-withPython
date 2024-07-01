import java.util.*;
class Solution {
    static class MyClass implements Comparable<MyClass>{
        int number;
        int count;
        
        public MyClass(int number, int count){
            this.number = number;
            this.count = count;
        }
        
        @Override
        public int compareTo(MyClass other){
            return Integer.compare(this.count, other.count);
        }
    }
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer>dict = new HashMap<>(); 
        
        for(int i=0; i<tangerine.length; i++){
            int key = tangerine[i];
            if(dict.get(key) == null){
                dict.put(key, 1);
            }
            else{
                dict.put(key, dict.get(key) + 1);
            }
        }
        
        PriorityQueue<MyClass>pq = new PriorityQueue<>(Comparator.reverseOrder());
        
        dict.forEach((key, value) ->{
            pq.add(new MyClass(key, value));
        });
        // 사전을 순회하면서 해당 키값과 value값을 우선순위 큐에 저장
        
        int cnt = 0;
        int answer = 0;
        while(pq.size() !=0){
            MyClass myclass = pq.poll();
            cnt += myclass.count;
            answer ++;
            if(k <= cnt){
                break;
            }
            // System.out.println(myclass.number + "   " + myclass.count);
        }
        
        return answer;
    }
}
