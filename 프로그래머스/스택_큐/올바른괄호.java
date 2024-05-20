import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Stack<Character>stack = new Stack<>();
        
        // step1. 모든 문자열을 순회
        for(int i=0; i<s.length(); i++){
            // step2_1. 만약 현재 문자가 '(' 라면 스택에 넣음
            if(s.charAt(i) == '('){
                stack.add(s.charAt(i));
            }
            
            // step2_2. 만약 현재 문자가 ')'라면 and !stack.isEmpty()스택에서 제거
            else{
                if(stack.isEmpty()){
                    answer = false; 
                    break;
                }
                    
                stack.pop();
            }
        }
        if(stack.size() != 0){
            answer = false;
        }
    
        return answer;
    }
}