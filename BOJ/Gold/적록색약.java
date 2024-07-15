import java.util.*;
import java.io.*;
public class 적록색약 {
    public static String grid[][];
    public static boolean visit[][];

    public static int dx[] = {0, 0, -1, 1};
    public static int dy[] = {-1, 1, 0, 0};

    public static class Point {
        int x;
        int y;
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public static void myprint(int n, BufferedWriter bw) throws Exception{
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                bw.write(grid[i][j] + " ");
            }
            bw.newLine();
        }
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input[] = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);

        grid = new String[n][n];
        visit = new boolean[n][n];
        for(int i=0; i<n; i++){
            input = br.readLine().split("");
            for(int j=0; j<n; j++){
                grid[i][j] = input[j];
            }
        }
        // myprint(n, bw);

        int normal = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(visit[i][j] == false){
                    normal++;
                    dfs(new Point(j, i), grid[i][j]);
                }
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                visit[i][j] = false;
                if(grid[i][j].equals("R")){
                    grid[i][j] ="G";
                }
            }
                
        }

        int red = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(visit[i][j] == false){
                    red++;
                    dfs(new Point(j, i), grid[i][j]);
                }
            }
        }
        // myprint(n, bw);

        bw.write(String.valueOf(normal) + " ");
        bw.write(String.valueOf(red));
        bw.newLine();

        bw.flush();
        bw.close();


    }

    static void dfs(Point p, String target){
        visit[p.y][p.x] = true;
        Stack<Point>stack = new Stack<>();
        stack.push(p);

        while (!stack.isEmpty()) {
            Point point = stack.pop();

            for(int i=0; i<4; i++){
                int nx = point.x + dx[i];
                int ny = point.y + dy[i];

                if(isRange(nx, ny, grid.length) && visit[ny][nx] == false && grid[ny][nx].equals(target)){
                    visit[ny][nx] = true;
                    stack.push(new Point(nx, ny));
                }
            }
        }
    }

    static boolean isRange(int x, int y, int n){
        if(x < 0 || n <=x)
            return false;
        if(y < 0 || n <=y)
            return false;
        return true;
    }
}
