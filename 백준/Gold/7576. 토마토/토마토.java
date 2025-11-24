import java.util.*;
import java.io.*;

public class Main{

  static int n,m;
  static int[][] box;
  static boolean[][] visited;

  static int[] dr = {-1,1,0,0};
  static int[] dc = {0,0,-1,1};

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    m = Integer.parseInt(st.nextToken());
    n = Integer.parseInt(st.nextToken());
    box = new int[n][m];
    Queue<int[]> q = new LinkedList<>(); 
    

    for(int i=0; i<n; i++){
      st = new StringTokenizer(br.readLine());
      for(int j=0; j<m; j++){
        box[i][j] = Integer.parseInt(st.nextToken());
        if(box[i][j] == 1){
          q.offer(new int[]{i,j}); //q.append((i,j))
        }     
      }
    }
    int day = bfs_tomato(q);
    for(int i=0; i<n; i++){
      for(int j=0; j<m;j++){
        if (box[i][j] ==0){
          System.out.println(-1);
          return;
        } 
      }
    }
    System.out.println(day);

    }
    

    static int bfs_tomato(Queue<int[]> q){
      int day = 0;
      while(!q.isEmpty()){
        int size = q.size();
        for(int s=0; s<size; s++){
          int[] cur = q.poll(); //q.popleft()
          int r = cur[0];
          int c = cur[1];

          for(int i=0; i<4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(0<=nr && nr<n && 0<=nc && nc<m){
              if (box[nr][nc] == 0){
                box[nr][nc] = 1;
                q.offer(new int[]{nr,nc});
              }
            }
          }
        }
         if(!q.isEmpty()){
          day++;
         }
      }
     return day;

    }
  }
