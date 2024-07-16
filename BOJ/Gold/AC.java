import java.util.*;
import java.io.*;
public class AC {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 입력받는 부분 수정
        int testcase = Integer.parseInt(br.readLine()); // 테스트 케이스 수 입력받기 수정

        while (testcase != 0) {
            testcase--;
            boolean flag = true; // true : front, false: back
            String operations = br.readLine(); // 연산자 입력받기 수정
            int n = Integer.parseInt(br.readLine()); // 배열 크기 입력받기 수정

            Deque<Integer> dq = new ArrayDeque<>();
            String arrayInput = br.readLine(); // 배열 입력받기 수정
            arrayInput = arrayInput.substring(1, arrayInput.length() - 1); // '['와 ']' 제거
            String[] elements = arrayInput.split(","); // ','를 기준으로 나누기 수정
            for (String element : elements) {
                if (!element.equals("")) { // 빈 문자열이 아닌 경우
                    dq.add(Integer.parseInt(element)); // 숫자로 변환하여 덱에 추가
                }
            }
            
            boolean isDone = false;
            for (char op : operations.toCharArray()) { // 연산자 하나씩 처리 (배열 순회 방식 변경)
                if (op == 'R') {
                    flag = !flag; // 뒤집기
                } else if (op == 'D') {
                    if (dq.isEmpty()) {
                        bw.write("error");
                        isDone = true;
                        bw.newLine();
                        break;
                    } else {
                        if (flag) {
                            dq.poll(); // 앞에서 제거
                        } else {
                            dq.pollLast(); // 뒤에서 제거
                        }
                    }
                }
            }
            
            if (!isDone) {
                if (dq.isEmpty()) { // deque의 크기가 0인지 확인하는 조건 수정
                    bw.write("[]");
                    bw.newLine();
                    continue;
                }
                bw.write("[");
                while (!dq.isEmpty()) { // deque를 출력하는 부분 수정
                    if (flag)
                        bw.write(String.valueOf(dq.poll()));
                    else
                        bw.write(String.valueOf(dq.pollLast()));
                    if (!dq.isEmpty()) // deque의 크기가 0인지 확인하는 조건 수정
                        bw.write(",");
                }
                bw.write("]");
                bw.newLine();
            }
        }
        bw.flush();
        bw.close();
    }
}
