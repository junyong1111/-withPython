import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        
        for(int i=1; i<triangle.length; i++){
            // 삼각형의 높이만큼 진행
            for(int j=0; j<triangle[i].length; j++){
                // 해당 행만큼 진행
                if(j==0 || j== triangle[i].length-1){ //처음과 끝인 경우 자신의 위만
                    triangle[i][j] = triangle[i-1][Math.max(j-1, 0)] + triangle[i][j];
                    continue;
                }
                triangle[i][j] = Math.max(triangle[i-1][j] , triangle[i-1][j-1]) + triangle[i][j];                
            }
        }
        int answer = 0;
        for(int i=0; i<triangle[triangle.length-1].length; i++)
            answer = Math.max(answer, triangle[triangle.length-1][i]);
        
        return answer;
    }
}