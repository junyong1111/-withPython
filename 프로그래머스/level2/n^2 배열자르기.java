import java.util.*;
class Solution {
    static int[][] arr;
    static void setArr(int index){
        for(int i=0; i<=index; i++){
            for(int j=0; j<=index; j++){
                if(arr[i][j] ==0)
                    arr[i][j] = index+1;
            }
        }
    }
    static void MyPrint(int n){
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                System.out.print(arr[i][j] + " "); 
            }
            System.out.println();
        }
    }
    public int[] solution(int n, long left, long right) {
        int[] answer = {};
        System.out.println(4%8);
        
        long start = left+1L; 
        
        // step1. NxN 배열만큼 초기화
        // arr = new int[n][n];
        // for(int i=0; i<n; i++){
        //     for(int j=0; j<n; j++){
        //         arr[i][i] = 0;
        //     }
        // }
        
        // step2. 배열을 순회하면서 갱신
        // for(int i=0; i<n; i++)
        //     setArr(i);
        
        // step3. 배열 1열로 만들기
        // List<Integer>list = new ArrayList<>();
        // for(int i=0; i<n; i++){
        //     for(int j=0; j<n; j++){
        //         list.add(arr[i][j]);
        //     }
        // }
        
        // step4. 정답에 옮기기
        
        // int size = Long.valueOf(right-left).intValue();
        // int idx = 0;
        // answer = new int[size+1];
        // for(long i=left; i<=right; i++){
        //     answer[idx++] = list.get(Long.valueOf(i).intValue());
        // }
        // System.out.println(list.toString());
        // MyPrint(n);
        
        return answer;
    }
}