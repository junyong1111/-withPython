import java.util.*;
import java.io.*;
public class 연구소 {
    public static  class Point{
        int x;
        int y;
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public static int grid[][];
    public static List<Point> points;
    public static List<Point> virus;
    public static int dx[] = {0, 0, -1, 1};
    public static int dy[] = {-1, 1, 0, 0};
    public static void myPrint(int n, int m, BufferedWriter bw) throws Exception{
        bw.write("======================================= my print ===============================\n");
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                bw.write(grid[i][j] + " ");
            }
            bw.newLine();
        }
        bw.newLine();

        bw.write("======================================= my print ===============================\n");
        for(int i=0; i<points.size(); i++){
            bw.write(points.get(i).x + " ," + points.get(i).y + "\n");
        }
        bw.newLine();
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input[] = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        grid = new int[N][M];
        points = new ArrayList<>();
        virus = new ArrayList<>();

        for(int i=0; i<N; i++){
            input = br.readLine().split(" ");
            for(int j=0; j<M; j++){
                grid[i][j] = Integer.parseInt(input[j]);
                if(grid[i][j] == 0){ // 빈 공간은 미리 추가
                    points.add(new Point(j, i)); //x y
                }
                if(grid[i][j] == 2)
                    virus.add(new Point(j, i));
            }
        }

        int answer = 0;
        // Step1. 벽 3개를 순차적으로 하나씩 세우면서 진행(배열 복사 후 진행)
        for(int i=0; i<points.size(); i++){
            for(int j=0; j<points.size(); j++){
                for(int k=0; k<points.size(); k++){
                    int copyGrid[][] = copyArray(N, M);
                    copyGrid[points.get(i).y][points.get(i).x] = 1;
                    copyGrid[points.get(j).y][points.get(j).x] = 1;
                    copyGrid[points.get(k).y][points.get(k).x] = 1;
                    answer = Math.max(dfs(copyGrid), answer);
                }
            }
        }
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
    public static int dfs(int[][] copyGrid){
        Stack<Point>stack = new Stack<>();
        boolean visit[][] = new boolean[copyGrid.length][copyGrid[0].length];
        for(int i=0; i<copyGrid.length; i++){
            for(int j=0; j<copyGrid[i].length; j++)
                visit[i][j] = false;
        }
        for(int i=0; i<virus.size(); i++){
            stack.push(virus.get(i));
            visit[virus.get(i).y][virus.get(i).x] = true;
        }

            while (!stack.isEmpty()) {
                Point p = stack.pop();
                for (int i = 0; i < 4; i++) {
                    int nx = p.x + dx[i];
                    int ny = p.y + dy[i];
                    if (isRange(nx, ny) == true && copyGrid[ny][nx] == 0 && visit[ny][nx] == false) {
                        visit[ny][nx] = true;
                        copyGrid[ny][nx] = 1;
                        stack.push(new Point(nx, ny));
                    }
                }
            }
        int cnt = 0;
        for(int i=0; i<copyGrid.length; i++){
            for(int j=0; j<copyGrid[i].length; j++){
                if(copyGrid[i][j] == 0){
                    cnt++;
                }
            }
        }
        return cnt;

    }
    public static boolean isRange(int x, int y){
        if(x < 0 || grid[0].length <=x)
            return false;
        if(y < 0 || grid.length <= y)
            return false;
        return true;
    }
    public static int[][] copyArray(int n, int m){
        int arr[][] = new int[n][m];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                arr[i][j] = grid[i][j];
            }
        }
        return arr;
    }
}