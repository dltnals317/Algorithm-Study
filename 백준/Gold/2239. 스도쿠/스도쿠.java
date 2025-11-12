import java.io.*;
import java.util.*;

public class Main {
    static int[][] board = new int[9][9];
    static boolean[][] rowUsed = new boolean[9][10];
    static boolean[][] colUsed = new boolean[9][10];
    static boolean[][] subUsed = new boolean[9][10];
    static List<int[]> blanks = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 9; i++) {
            String line = br.readLine().trim();
            for (int j = 0; j < 9; j++) {
                board[i][j] = line.charAt(j) - '0';
                int num = board[i][j];
                if (num == 0) {
                    blanks.add(new int[]{i, j});
                } else {
                    rowUsed[i][num] = true;
                    colUsed[j][num] = true;
                    subUsed[getSubIndex(i, j)][num] = true;
                }
            }
        }

        solve(0);
    }

    static int getSubIndex(int r, int c) {
        return (r / 3) * 3 + (c / 3);
    }

    static void solve(int idx) {
        if (idx == blanks.size()) {
            printBoard();
            System.exit(0); // 첫 번째 해답 출력 후 종료
        }

        int[] pos = blanks.get(idx);
        int r = pos[0];
        int c = pos[1];

        for (int num = 1; num <= 9; num++) {
            if (!rowUsed[r][num] && !colUsed[c][num] && !subUsed[getSubIndex(r, c)][num]) {
                board[r][c] = num;
                rowUsed[r][num] = true;
                colUsed[c][num] = true;
                subUsed[getSubIndex(r, c)][num] = true;

                solve(idx + 1);

                board[r][c] = 0;
                rowUsed[r][num] = false;
                colUsed[c][num] = false;
                subUsed[getSubIndex(r, c)][num] = false;
            }
        }
    }

    static void printBoard() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append(board[i][j]);
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}
