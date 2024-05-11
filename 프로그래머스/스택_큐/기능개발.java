import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        Queue<Integer>queue = new LinkedList<>();
        Queue<Integer>speedQueue = new LinkedList<>();
        ArrayList<Integer>answers = new ArrayList<>();

        for(int i=0; i<progresses.length; i++){
            queue.add(progresses[i]);
            speedQueue.add(speeds[i]);
        }
            
        int turn = 0;
        while (!queue.isEmpty()){
            // step1. 큐.peek 이후 END 아닌 경우 speed만큼 작업 진행
            int end = 0;
            if(queue.peek() != 100){
                for(int i=0; i<speedQueue.size(); i++){
                    queue.add(Math.min(100, queue.poll() + speedQueue.peek()));
                    speedQueue.add(speedQueue.poll());
                }
            }
            
            // step2. 큐.peek 이후 END의 경우 이후 모든 end를 제거
            else{
                while (!queue.isEmpty() && queue.peek() == 100){
                    queue.poll();
                    speedQueue.poll();
                    end++;
                }
                answers.add(end);
            }
        }
        
        int[] answer = new int[answers.size()];
        for(int i=0; i<answers.size(); i++){
            answer[i] = answers.get(i);
        }
        
        return answer;
    }
}