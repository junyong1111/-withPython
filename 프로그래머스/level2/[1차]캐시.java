import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Queue<String>LRUqueue = new LinkedList<>();
        Map<String, Integer>dict = new HashMap<>();
        
        if (cacheSize == 0) {
            return cities.length * 5;
        }
        // step1. 미리 사전에 갈 수 있는 도시들을 셋팅
        for(int i=0; i<cities.length; i++){
            String key = cities[i].toUpperCase(); // 대문자로 변환
            if(dict.getOrDefault(key, -1) == -1){
                dict.put(key, 0);
            }
        }
        
        // step2. 도시들을 순회하면서 해당 도시가 사전에서 0인지 1인지 확인
        for(int i=0; i<cities.length; i++){
            String city = cities[i].toUpperCase(); // 대문자로 변환
            
            if(dict.get(city) == 0){ // 만약 0이라면 cache miss
                dict.put(city, 1); // 캐시에 저장
                answer +=5; 
                
                if(LRUqueue.size() == cacheSize){ // 캐시큐 크기가 꽉 찼다면 오래된 캐시 삭제
                    String cache = LRUqueue.poll();
                    dict.put(cache, 0); 
                }
                LRUqueue.add(city); // 캐시큐에 저장
            }else{ //만약 1이라면 cache hit
                answer +=1;
                LRUqueue.remove(city);
                LRUqueue.add(city);
                // 캐시큐에 최신 큐를 반영
            }
        }
        
        return answer;
    }
}
