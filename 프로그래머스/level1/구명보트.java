import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {

        int answer = 0;        
        ArrayList<Integer> arr = new ArrayList<>();
        for (int person : people)  
            arr.add(person);
        // --- init ---
        
        // step1. 오름차순 정렬 후 1개씩 선택
        arr.sort(Comparator.naturalOrder());
        
        // step2. 가장 작은값과 가장 큰값을 선택해서 제거
        int left = 0;
        int right = arr.size()-1;

        int cnt = 0;
        while(left <= right){
            cnt+=1;
            // 왼쪽 하나 오른쪽 하나 선택
            int leftValue = arr.get(left);
            int rightValue = arr.get(right);
            
            // 우선 오른쪽 값이 limit보다 크거나 같거나 or 두 명의 몸무게가 넘어가버리면 무거운 사람만 보트로
            if(rightValue >= limit || (leftValue + rightValue > limit)){
                answer++; // 구명보트 추가하고
                right--; // 한 칸 이동
                continue;
            }
            // 2명이 세이프인 경우
            answer++; // 구명보트 추가하고
            // 2명 내림
            left++; 
            right--;
        }

        
        return answer;
    }
}
