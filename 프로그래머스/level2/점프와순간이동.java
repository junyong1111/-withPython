import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;
        
        while(n !=0){
            // 순간이동이 가능하면 반 나눔
            if(n%2==0){
                n=n/2;
                continue;
            } 
            // 불가능하면 점프
            ans++;
            n--;
        }
        
        return ans;
    }
}