import java.util.*;
import java.io.*;


public class Main{
  static int n;
  static int[][] area;
  static boolean[][] visited;
  static int[] dr = {-1,1,0,0};
  static int[] dc = {0,0,-1,1};

  public static void main(String[] args) throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    area = new int[n][n];

    int maxHeight = 0;

    for(int i=0; i<n; i++){
      st = new StringTokenizer(br.readLine());
      for(int j=0; j<n; j++){
        area[i][j] = Integer.parseInt(st.nextToken());
        maxHeight = Math.max(maxHeight, area[i][j]);
      }
    }

    int answer = 1;
    for (int rain=0; rain<=maxHeight; rain++){
      visited = new boolean[n][n]; // 매 강수량마다 방문 배열 초기화
      int totalCount = 0; //특정 강수량에서, 안전영역의 총 개수
      for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
          if (!visited[i][j] && area[i][j] > rain){ 
            //이 지점으로부터 안전영역 덩어리(?) 찾기
            bfs(i,j,rain);
            totalCount++;
          }
        }
      }
      answer = Math.max(answer,totalCount);
    }
    System.out.println(answer);
  }
  static boolean inRange(int r, int c) {
        return r >= 0 && r < n && c >= 0 && c < n;
    }
    
  static void bfs(int rr, int cc, int rain){
    Queue<int[]> q = new LinkedList<>();
    q.offer(new int[]{rr,cc});
    visited[rr][cc] = true;


    while(!q.isEmpty()){
      int [] cur = q.poll();
      int r = cur[0];
      int c = cur[1];
      for(int i=0; i<4; i++){
        int nr = r + dr[i];
        int nc = c + dc[i];
        
        if (inRange(nr,nc)){
          if(!visited[nr][nc] && area[nr][nc] > rain){ //안전영역
              visited[nr][nc] = true;
              q.offer(new int[]{nr,nc});
          }
        }
      }
    }
  }
}