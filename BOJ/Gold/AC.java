import java.util.*;
import java.io.*;
public class AC{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String input[] = br.readLine().split(" ");
        int testcase = Integer.parseInt(input[0]);

        while(testcase !=0 ){
            testcase--;
            boolean flag = true; // true : front, false:back
            String operation[] = br.readLine().split(" ");
            input = br.readLine().split(" ");
            int n = Integer.parseInt(input[0]);

            Deque<Integer>dq = new ArrayDeque<>();
            input = br.readLine().split(" ");
            for(int i=0; i<=n*2; i++){
                if(i%2!=0){
                    dq.add((input[0].charAt(i))-48);
                }
                    
            }
            boolean isDone = false;
            for(int i=0; i<operation[0].length(); i++){
                if(operation[0].charAt(i) == 'R'){
                    flag = flag?false:true;
                }else if(operation[0].charAt(i) == 'D'){
                    if(dq.size() == 0){
                        bw.write("error");
                        isDone = true;
                        bw.newLine();
                        break;
                    }else{
                        if(flag == true){
                            dq.poll();
                        }else{
                            dq.pollLast();
                        }
                    }
                }
            } // for
            
            if(isDone == false){
                if(dq.size() == 0){
                    bw.write("[]");
                    bw.newLine();
                    continue;
                }
                bw.write("[");
                // System.out.print("[");
                while (!dq.isEmpty()) {
                    if(flag)
                        bw.write(String.valueOf(dq.poll()));
                        // System.out.print(dq.poll());
                    else
                        bw.write(String.valueOf(dq.pollLast()));
                        // System.out.print(dq.pollLast());
                    if(dq.size() !=0)
                        bw.write(",");
                        // System.out.print(",");
                }
                bw.write("]");
                bw.newLine();
                
                // System.out.println("]");
            }
            
        } //while
        bw.flush();
        bw.close();
    }
}