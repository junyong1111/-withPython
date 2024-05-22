import java.util.*;

class Solution {
    public static int totalnumber;
    public static char[] ALPHA = {'A', 'E', 'I', 'O', 'U'};
    public static String dictionary;
    public static int ans;
    
    public static void backtracking(int level, int index, String target){
        if(level == ALPHA.length){
            return;
        }
        
        for(int i=0; i<ALPHA.length; i++){
            dictionary += ALPHA[i];
            totalnumber++;
            if(dictionary.equals(target)){
                ans = totalnumber;
            }
            backtracking(level+1, i, target);
            dictionary = dictionary.substring(0, dictionary.length()-1); 
        }
    }
    
    public int solution(String word) {
        
        
        totalnumber = 0;
        
        // 모든 알파벳을 순회함 
        for(int i=0; i<ALPHA.length; i++){
            dictionary = "";
            dictionary += ALPHA[i];
            
            totalnumber++;
            if(dictionary.equals(word)){
                ans = totalnumber;
                break;
            }
            backtracking(1, i, word);
        }
        int answer = ans;
        return answer;
    }
}