import java.util.*;

class Solution {
    
    public static class stock{
        private int price;
        private int day;
        private boolean changed;
        
        private stock(int price, int day, boolean changed){
            this.price = price;
            this.day = day;
            this.changed = changed;
        }
        public static stock of(int price, int day, boolean changed){
            return new stock(price, day, changed);
        }
        
        public void setDay(){
            this.day++;
        }
        public int getDay(){
            return this.day;
        }
        public void setChanged(){
            this.changed = false;
        }
        public boolean getChanged(){
            return this.changed;
        }
        public int getPrice(){
            return this.price;
        }
        
        
    } // stock 클래스
    
    public int[] solution(int[] prices) {
        Queue<stock>queue = new LinkedList<>();
        
        queue.add(stock.of(prices[0], 0, true));
        for(int i=1; i<prices.length; i++){
            // step1. 현재 날짜에 주식 가격을 가지고 옴
            int price = prices[i];
            
            // step2. 큐를 순회하면서 현재 주식가격이 떨어졌는지 확인
            int sz = queue.size();
            for(int j=0; j<sz; j++){
                stock s = queue.poll();
                if(s.getChanged() == true){ // 비교 대상만 비교
                    if(s.getPrice() > price){ // 떨어졌으면 더이상 비교 안하기
                        s.setChanged();
                    }
                    else{ // 안떨어졌다면 day 1 증가
                        s.setDay();                        
                    }
                }
                // 다시 집어넣기
                queue.add(s);
            }
            
            //step3. 큐에 현재 가격 삽입
            queue.add(stock.of(price, 0, true));    
        }
    
        int[] answer = new int[queue.size()];
        
        for(int i=0; i<answer.length; i++){
            stock s = queue.poll();
            if(s.getChanged() == true){
                answer[i] = s.getDay();
            }
            else{
                answer[i] = s.getDay()+1;
            }
        }
        
        return answer;
    }
}