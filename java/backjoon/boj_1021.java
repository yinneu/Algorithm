package backjoon;

import java.util.*;
import java.io.*;

public class boj_1021 {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    Deque<Integer> deque = new LinkedList<>();
    for (int i = 0; i < n; i++) {
      deque.add(i+1);
    }

    int count = 0;

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < m; i++) {
      int target = Integer.parseInt(st.nextToken());

      int index = 0;
      for (int num : deque) {
        if (num == target) break;
        index++;
      }

      int left = index;
      int right = deque.size() - index;

      if (left <= right) {
        for (int j = 0; j < left; j++) {
          deque.offer(deque.poll());
        }
        count += left;
      } else {
        for (int j = 0; j < right; j++) {
          deque.offerFirst(deque.pollLast());
        }
        count += right;
      }
      deque.poll();
    }
    System.out.println(count);
  }
}
