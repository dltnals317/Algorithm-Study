import java.util.*;
import java.io.*;

public class Main {
    static int[][] gears = new int[4][8];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 1. 초기 톱니 상태 입력
        for (int i = 0; i < 4; i++) {
            String line = br.readLine();
            for (int j = 0; j < 8; j++) gears[i][j] = line.charAt(j) - '0';
        }

        int k = Integer.parseInt(br.readLine());
        
        // 2. K번의 명령 처리
        while (k-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int idx = Integer.parseInt(st.nextToken()) - 1; // 0-based
            int dir = Integer.parseInt(st.nextToken());

            // [결정 단계] 이번 명령에서 회전할 방향을 미리 확정
            int[] turnDirs = new int[4];
            turnDirs[idx] = dir;

            // 왼쪽 전파
            for (int i = idx; i > 0; i--) {
                if (gears[i][6] != gears[i - 1][2]) turnDirs[i - 1] = -turnDirs[i];
                else break; // 극이 같으면 전파 중단
            }
            // 오른쪽 전파
            for (int i = idx; i < 3; i++) {
                if (gears[i][2] != gears[i + 1][6]) turnDirs[i + 1] = -turnDirs[i];
                else break; // 극이 같으면 전파 중단
            }

            // [실행 단계] 결정된 방향대로 일괄 회전
            for (int i = 0; i < 4; i++) {
                if (turnDirs[i] != 0) rotate(i, turnDirs[i]);
            }
        }

        // 3. 최종 점수 계산 (모든 명령 종료 후 1번만)
        int ans = 0;
        for (int i = 0; i < 4; i++) {
            if (gears[i][0] == 1) ans += (1 << i); // 1, 2, 4, 8 점
        }
        System.out.println(ans);
    }

    // 배열을 한 칸씩 미는 실제 회전 메서드
    static void rotate(int idx, int dir) {
        if (dir == 1) { // 시계
            int tmp = gears[idx][7];
            for (int i = 7; i > 0; i--) gears[idx][i] = gears[idx][i - 1];
            gears[idx][0] = tmp;
        } else { // 반시계
            int tmp = gears[idx][0];
            for (int i = 0; i < 7; i++) gears[idx][i] = gears[idx][i + 1];
            gears[idx][7] = tmp;
        }
    }
}