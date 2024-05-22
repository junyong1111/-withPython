import java.util.*;

class Solution {
    public static boolean visit[];
    public static String number;
    public static Map<String, Integer>dic = new HashMap<>();
    public static int ans;
    
    public static boolean isPrime(int value){
        if(value <=1)
            return false;
        for(int i=2; i<value; i++){
            if(value % i == 0){
                return false;
            }
        }
        return true;
    }
    
    public static void backtracking(int level, int index, int sz, String numbers){
        if(level > sz)return;
        
        // 백트랙킹을 돌면서 만약에 최초 방문이면 문자열을 추가
        for(int i=0; i<sz; i++){ 
            if(i == index) continue;
            if(visit[i] == false){
                
                visit[i] = true;
                number += numbers.charAt(i);
                if(isPrime(Integer.parseInt(number)) == true){ // 소수이면서 처음이라면 푸쉬
                    if(dic.get(number) == null){dic.put(number, 1); ans+=1;}
                }
                // System.out.println(number);
                
                backtracking(level+1, i, sz, numbers);
                number = number.substring(0, number.length() - 1);
                visit[i] = false;
                
                
            }// 처음 방문이라면 
        }
        
    }
    public int solution(String numbers) {
        int sz = numbers.length();
        
        // 전역 변수로 설정
        visit  = new boolean[sz];
        number = "";
        ans = 0;
        
        for(int i=0; i<sz; i++)
            visit[i] = false;
        
        for(int i=0; i<sz; i++){
            if(numbers.charAt(i) == '0')continue; // 시작이 0이면 버림
            number = "";
            number += numbers.charAt(i);

            if(isPrime(Integer.parseInt(number)) == true){ // 소수이면서 처음이라면 푸쉬
                if(dic.get(number) == null){dic.put(number, 1); ans+=1;}
            }
            
            visit[i] = true;
            backtracking(1, i, sz, numbers);
            visit[i] = false;
        }
        
    
        int answer = ans;
        return answer;
    }
}