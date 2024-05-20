import java.util.*;

class Solution {
    public class Truck{
        private int weight;
        private int time;
        
        public Truck(int weight, int time){
            this.weight = weight;
            this.time = time;
        }
        public int getTime(){
            return this.time;
        } 
        
        public int getWeight(){
            return this.weight;
        }
        
        public void setTime(int time){
            this.time = time;
        }
        
        public void decreaseTime(){
            this.time --;
        }
        public void printMyTruck(){
            System.out.println("현재 트럭의 무게는 : " + this.weight);
            System.out.println("현재 트럭의 남은 시간은 : " + this.time);
            
        }
        
    } // Truck class
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int total_weight = 0;
        Queue<Integer>endQ = new LinkedList<>();
        Queue<Truck>readyQ = new LinkedList<>();
        Queue<Truck>ingQ = new LinkedList<>();
        
        for(int i=0; i<truck_weights.length; i++){
            Truck truck = new Truck(truck_weights[i], bridge_length);
            readyQ.add(truck);
        }
        
        
        while(endQ.size() < truck_weights.length){
            answer +=1; // 시간 증가
            
            //step1 : 현재 진행 큐에 차량이 있으면서 다리를 다 건넜다면 종료 큐로 넘겨줌
            if(!ingQ.isEmpty()){
                Truck temp = ingQ.peek();
                if(temp.getTime() == 0){
                    total_weight-= temp.getWeight(); // 다리에서 해당 트럭을 제거
                    endQ.add(temp.getWeight());
                    ingQ.poll();
                }
            }
            
            //step2. 현재 대기큐에 있는 트럭을 다리에 올릴 수 있다면 올림
            if(!readyQ.isEmpty()){
                Truck temp = readyQ.peek();
                if((total_weight+temp.getWeight()) <= weight){
                    total_weight += temp.getWeight();
                    ingQ.add(readyQ.poll());
                }
            }
            
            // step3. 다리위에 있는 모든 트럭들의 시간을 1씩 감소
            int size = ingQ.size();
            for(int i=0; i<size; i++){
                Truck temp = ingQ.poll();
                temp.decreaseTime();
                ingQ.add(temp);
            }
           
        }
    
        
        return answer;
    }
}