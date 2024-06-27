import java.util.*;

class Solution {
    public static int dx[] = {0, 0, -1, 1};
    public static int dy[] = {-1, 1, 0, 0};
    
    public static int start[] = {0, 0};
    
    public static boolean isPossible(int x_sz, int y_sz, int nx, int ny){
        if(nx < 0 || x_sz <= nx)
            return false;
        if(ny < 0 || y_sz <= ny)
            return false;
        return true;
    }
    
    public static boolean isObstacle(char item){
        if(item == 'X')
            return true;
        return false;
    }
    public int[] solution(String[] park, String[] routes) {
        int[] answer = new int[2];
        int x_sz = park[0].length();
        int y_sz = park.length;
        
        
        for(int i=0; i<park.length; i++){
            for(int j=0; j<park[i].length(); j++){
                if(park[i].charAt(j) == 'S'){
                    start[0] = j;
                    start[1] = i;
                }
            }
        }
        
        for(int i=0; i<routes.length; i++){
            String input[] = routes[i].split(" ");
            
            char dir = input[0].charAt(0);
            int count = Integer.parseInt(input[1]);
            
            int temp[] = new int[2];
            for(int copy = 0; copy<2; copy++){
                temp[0] = start[0];
                temp[1] = start[1];
            }
            boolean flag = false;
            
            for(int cnt = 0; cnt< count; cnt++){
                if(dir == 'N'){
                    int nx = temp[0] + dx[0];
                    int ny = temp[1] + dy[0];
                    
                    if(isPossible(x_sz, y_sz, nx, ny) &&
                            isObstacle(park[ny].charAt(nx))== false){  
                            temp[0] = nx;
                            temp[1] = ny;
                        }
                    else{
                        flag = true;
                        break;
                    }
                } // N
                else if(dir == 'S'){
                    int nx = temp[0] + dx[1];
                    int ny = temp[1] + dy[1];
                    
                    if(isPossible(x_sz, y_sz, nx, ny) &&
                            isObstacle(park[ny].charAt(nx))== false){  
                            temp[0] = nx;
                            temp[1] = ny;
                        }
                    else{
                        flag = true;
                        break;
                    }
                } // S
                
                else if(dir == 'W'){
                    int nx = temp[0] + dx[2];
                    int ny = temp[1] + dy[2];
                    
                    if(isPossible(x_sz, y_sz, nx, ny) &&
                            isObstacle(park[ny].charAt(nx))== false){  
                            temp[0] = nx;
                            temp[1] = ny;
                        }
                    else{
                        flag = true;
                        break;
                    }
                } //W
                
                else if(dir == 'E'){
                    int nx = temp[0] + dx[3];
                    int ny = temp[1] + dy[3];
                    
                    if(isPossible(x_sz, y_sz, nx, ny) &&
                            isObstacle(park[ny].charAt(nx))== false){ 
                        
                            temp[0] = nx;
                            temp[1] = ny;
                        }
                    else{
                        flag = true;
                        break;
                    }
                } // E
            } // 횟수 포문
            if(flag == false) {
                for(int copy = 0; copy<2; copy++){
                    start[0] = temp[0];
                    start[1] = temp[1];
                }
            }
        }
        
        answer[0] = start[1];
        answer[1] = start[0];
        
        return answer;
    }
}