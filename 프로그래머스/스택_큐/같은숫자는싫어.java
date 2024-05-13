import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer;
        Stack<Integer>stack = new Stack<>();
        
        
        if(arr.length == 0){
            answer = new int[1];
            return answer;
        }
        
        
        stack.add(arr[0]);
        for(int i=1; i<arr.length; i++){
            // step1. 스택에서 peek 한 후 현재 값이 같으면 넘어감
            if(stack.peek() == arr[i]){
                continue;
            }
            // step2. 다르면 push
            stack.add(arr[i]);
        }
        answer = new int[stack.size()];
        ArrayList<Integer>temp = new ArrayList<>();
        
        while (!stack.isEmpty()){
            temp.add(stack.pop());
        }
        
        int idx = temp.size()-1;
        for(int i=0; i<temp.size(); i++){
            answer[i] = temp.get(idx-i);
        }
       

        return answer;
    }
}