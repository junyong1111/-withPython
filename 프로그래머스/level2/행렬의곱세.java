import java.util.*;

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int y = arr1.length;
        int x = arr2[0].length;
        int[][] answer = new int[y][x];
        
        for(int i=0; i<y; i++){ // Ay * Bx 이므로 Ay만큼
            for(int j=0; j<x; j++){ // Bx만큼
                int sum = 0;
                for(int k=0; k<arr1[0].length; k++){ // 둘이 중복되는 Ax 또는 By만큼 순회
                    sum += arr1[i][k] * arr2[k][j]; 
                }
                answer[i][j] = sum;
            }
        }
        return answer;
    }
}