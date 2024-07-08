import java.util.*;
class Solution {
    static int ans;
    static boolean visit[];
    
    public int solution(int k, int[][] dungeons) {
        // step0. 기본 셋팅(정답, 방문 배열)
        ans = 0;
        visit = new boolean[dungeons.length];
        for(int i=0; i<dungeons.length; i++)
            visit[i] = false;
        
        // step1. 재귀적으로 탐색
        recursion(dungeons, k, 0);
        int answer = ans;
        return answer;
    }
    static void recursion(int[][] dungeons, int k, int answer){
        // 모든 던전을 순회
        for(int i=0; i<dungeons.length; i++){
            // 방문한적이 없고 던전을 탐험할 수 있다면 진행
            if(visit[i] ==false && isPossible(dungeons[i], k) == true){ 
                // 정답 갱신 + 방문 체크 -> 다음 던전 탐색
                ans = Math.max(ans, answer+1);
                visit[i] = true;
                recursion(dungeons, k-dungeons[i][1], answer+1);
                visit[i] = false;
            }
        }
    }
    
    static boolean isPossible(int[] dungeon, int k){
        if(dungeon[0] <= k){ // 필요 피로도가 존재 하면 진행
            return true;
        }
        return false;
    }
}
