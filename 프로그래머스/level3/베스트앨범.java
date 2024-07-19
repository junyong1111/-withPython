import java.util.*;

class Solution {
    public static class Music {
        int plays;
        int index;
        
        public Music(int plays, int index){
            this.plays = plays;
            this.index = index;
        }
    }
    public static class Album implements Comparable<Album>{
        String genre;
        int plays;
        
        public Album(String genre, int plays){
            this.genre = genre;
            this.plays = plays;
        }
        @Override
        public int compareTo(Album other){
            if(this.plays < other.plays)
                return 1;
            return -1;
        }
    }
    public int[] solution(String[] genres, int[] plays) {
        Map<String, List<Music>> dict = new HashMap<>();
        Map<String, Integer> dict_pq = new HashMap<>();
        
        int size = genres.length;
        for(int i=0; i<size; i++){
            String key = genres[i];
            if(!dict.containsKey(key)){
                List<Music> temp = new ArrayList<>();
                temp.add(new Music(plays[i], i));
                dict.put(key, temp);
                dict_pq.put(key, plays[i]);
            }else{
                List<Music> temp = dict.get(key);
                temp.add(new Music(plays[i], i));
                dict.put(key, temp);
                dict_pq.put(key, dict_pq.get(key) + plays[i]);
            }
        }
        
        PriorityQueue<Album> pq = new PriorityQueue<>();
        dict_pq.forEach((key, value) -> {
            pq.add(new Album(key, value));
        });
        
        List<Integer> result = new ArrayList<>();
        
        while(!pq.isEmpty()){
            Album album = pq.poll();
            String key = album.genre;
            List<Music> list = dict.get(key);
            
            // plays를 기준으로 내림차순 정렬
            list.sort((a, b) -> b.plays - a.plays);
            
            // 상위 2개의 곡 선택
            for(int i = 0; i < Math.min(2, list.size()); i++) {
                result.add(list.get(i).index);
            }
        }
        
        int[] answer = result.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}
