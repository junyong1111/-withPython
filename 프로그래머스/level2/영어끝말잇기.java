import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        Queue<Integer>queue = new LinkedList<>();
        Map<String, Integer>dict = new HashMap<>();
        int[] answer = new int[2];
        
        // step1. 사용자를 큐에 저장
        for(int i=1; i<=n; i++)
            queue.add(i);
        char[] lastWord = new char[1];
        for(int i=0; i< words.length; i++){
            int person = queue.poll();
            
            String word = words[i]; // 단어 가져옴
            if(word.length() == 1){ // 단어길이가 1개라면 끝
                answer[0] = person;
                answer[1] = (i/n)+1;
                break;
            }
            
            if(i == 0){ // 처음에는 그냥 넣어줌
                dict.put(word, 1);
                queue.add(person);
                lastWord[0] = word.charAt(word.length()-1);
                continue;
            }
            // 처음이 아닌 경우는 2가지 체크
            // 1번 중복단어인지 확인
            if(dict.get(word) != null){
                answer[0] = person;
                answer[1] = (i/n)+1;
                break;
            }
            
            // 단어가 다른경우 
            if(lastWord[0] != word.charAt(0)){
                answer[0] = person;
                answer[1] = (i/n)+1;
                break;
            }
            // 다 통과했다면
            dict.put(word, 1);
            queue.add(person);
            lastWord[0] = word.charAt(word.length()-1);
        }
        return answer;
    }
}
