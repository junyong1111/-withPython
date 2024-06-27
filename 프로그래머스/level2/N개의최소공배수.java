import java.util.*;

class Solution {
    public int gcd(int a, int b){
        if(a < b){
            int temp = a;
            a = b;
            b = temp;
        }
        
        while(b!=0){
            int remainder = a % b; // 5
		    a = b; //15
		    b = remainder;//5
        }
        return a;
    }
    public int lcm(int a, int b){
        return (a * b) / gcd(a, b);
    }
    public int solution(int[] arr) {
        int answer = 0;
        // 앞에서부터 최소 공배수를 찾아감..?
        
        int start = arr[0];
        for(int i=1; i<arr.length; i++){
            start = lcm(start, arr[i]);
        }
        answer = start;
        
        return answer;
    }
}