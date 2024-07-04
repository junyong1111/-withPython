import java.util.*;

class Solution {
    static void init(int[][] maps){
        for(int i=0; i<maps.length; i++){
            for(int j=0; j<maps[0].length; j++){
                grid[i][j] = maps[i][j];
                distance[i][j] = 0;
            }
        }
    }
    static void myprint(int n, int m){
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                System.out.print(distance[i][j] + " ");
            }
            System.out.println();
        }
    }
    static class Point{
        int x;
        int y;
        
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    static int[][] grid;
    static int[][] distance;
    static int dx[] = {0, 0, -1, 1};
    static int dy[] = {-1, 1, 0, 0};
    static boolean isRange(int x, int y, int N, int M){
        if(x < 0 || M<=x)
            return false;
        if(y < 0 || N<=y)
            return false;
        return true;
    }
    static void bfs(Point start){
        Queue<Point>q = new LinkedList<>();
        q.add(start);
        distance[start.y][start.x] = 1;
        
        while(!q.isEmpty()){
            Point p = q.poll();
            for(int i=0; i<4; i++){
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];
                
                if(isRange(nx, ny, grid.length, grid[0].length) == true 
                        && distance[ny][nx] == 0 && grid[ny][nx] == 1){
                    distance[ny][nx] = distance[p.y][p.x]+1; 
                    q.add(new Point(nx, ny));
                }
            }
        }
    }
    public int solution(int[][] maps) {
        grid = new int[maps.length][maps[0].length];
        distance = new int[maps.length][maps[0].length];
        
        init(maps);
        bfs(new Point(0, 0));
        int answer = distance[maps.length-1][maps[0].length-1];
        
        if(answer == 0)
            answer= -1;
        
        return answer;
    }
}