import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        // step1. 논문을 정렬
        Arrays.sort(citations);
        int size = citations.length;
        // step2. 정렬된 논문을 순회[0, 1, 3, 5, 6]
        int minValue = citations[0];
        int maxValue = citations[size-1];
        for(int value=minValue; value<=maxValue; value++){
            // int h = value;// h = 3이라고 가정한다면 
            for(int i=0; i<size; i++){
                if(value <= citations[i]){
                    int refer = size - i; // 3번 이상 인용된 논문의 개수    
                    int not_refer = i+1;
                    if(value <= refer && value <= not_refer)
                        answer =value;
                }
            }
        }
        
        return answer;
    }
}