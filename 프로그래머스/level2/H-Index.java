import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        // step1. 논문을 정렬
        Arrays.sort(citations);
        int size = citations.length;
        // step2. 정렬된 논문을 순회[0, 1, 3, 5, 6]
        
        int maxValue = citations[size-1];
        for(int h=0; h<=maxValue; h++){ // h값 시작
            
            int ref = 0;
            int nref = 0;
            for(int i=0; i<size; i++){ // 왼쪽부터 이상 나오면 스탑
                int current = citations[i];
                if(h <= current){
                    ref = size - i;
                    break;
                    } // if
                }// for
            for(int i=0; i<size; i++){ // 왼쪽부터 작은거 나오면 스탑(따로 로직을 빼줘야 하는듯)
                int current = citations[i];
                if(h >= current){
                    nref = i+1;
                    break;
                    } // if
                }// for
            if(h <= ref && h>= nref){
                answer = Math.max(answer, h);
            }
        } // h for
        
        return answer;
    }
}