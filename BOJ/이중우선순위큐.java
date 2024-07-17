import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int testcase = Integer.parseInt(br.readLine());

        while (testcase-- > 0) {
            int operations = Integer.parseInt(br.readLine());
            PriorityQueue<Long> minHeap = new PriorityQueue<>();
            PriorityQueue<Long> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
            Map<Long, Integer> countMap = new HashMap<>();

            for (int i = 0; i < operations; i++) {
                String[] operation = br.readLine().split(" ");

                if (operation[0].equals("I")) {
                    long num = Long.parseLong(operation[1]);
                    minHeap.add(num);
                    maxHeap.add(num);
                    countMap.put(num, countMap.getOrDefault(num, 0) + 1);
                } else if (operation[0].equals("D")) {
                    if (minHeap.isEmpty() || maxHeap.isEmpty()) {
                        continue;
                    }
                    if (operation[1].equals("-1")) {
                        removeElement(minHeap, countMap);
                    } else {
                        removeElement(maxHeap, countMap);
                    }
                }
            }

            // 유효한 최소값과 최대값을 가져오기 위해 최종 정리
            cleanUpHeap(minHeap, countMap);
            cleanUpHeap(maxHeap, countMap);

            if (minHeap.isEmpty()) {
                bw.write("EMPTY\n");
            } else {
                bw.write(maxHeap.peek() + " " + minHeap.peek() + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }

    private static void removeElement(PriorityQueue<Long> heap, Map<Long, Integer> countMap) {
        while (!heap.isEmpty() && countMap.getOrDefault(heap.peek(), 0) == 0) {
            heap.poll();
        }

        if (!heap.isEmpty()) {
            long num = heap.poll();
            countMap.put(num, countMap.get(num) - 1);
            if (countMap.get(num) == 0) {
                countMap.remove(num);
            }
        }
    }

    private static void cleanUpHeap(PriorityQueue<Long> heap, Map<Long, Integer> countMap) {
        while (!heap.isEmpty() && countMap.getOrDefault(heap.peek(), 0) == 0) {
            heap.poll();
        }
    }
}
