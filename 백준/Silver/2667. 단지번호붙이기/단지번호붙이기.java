import java.util.*;
import java.lang.*;
import java.io.*;

/*
DFS로 풀어보자

- bfs가 아닌데도, visited로 방문기록 해야하나? (다른건 몰라도, 이건 여러개의 dfs기반 묶음이 만들어질 수 있고, 각 이웃은 하나의 단지에만 포함되어야하므로 필요하겠지..?)
- 좌표 돌면서 -> 상하좌우 탐색 -> 1인애들 BFS재귀호출 => 재귀 최종적으로 빠져나왔을 때, 마을 수 기록
*/

class Main {
    public static int n;
    public static int[][] grid;
    public static boolean[][] visited;
    public static int[] dr = new int[] {-1,1,0,0};
    public static int[] dc = new int[] {0,0,-1,1};
    public static int totalNum = 0;
    public static int tempCnt = 1;
    public static List<Integer> numList = new ArrayList<>();

    public static void main(String[] args) throws IOException{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    n = Integer.parseInt(st.nextToken());
    grid = new int[n][n];
    visited = new boolean[n][n];
    for(int i=0; i<n; i++){
        String line = br.readLine();
        for(int j=0; j<n; j++){
            grid[i][j] = line.charAt(j) - '0';
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            
            if(grid[i][j]==1 && visited[i][j] == false){
                totalNum++;
                tempCnt = 0;
                BFS(i,j);
                //빠져나오면
                numList.add(tempCnt);         
            }
        }
    }
    Collections.sort(numList);
    System.out.println(totalNum);
    for(int x=0; x<numList.size(); x++){
        System.out.println(numList.get(x));
    }


    }

    public static void BFS(int r, int c){ //grid[r][c] == 1임이 호출 전 검증된다고 가정
        tempCnt++;
        visited[r][c] = true;
        for(int i=0; i<4; i++){
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(inRange(nr,nc)){
                BFS(nr,nc);
            }
        }
    }
    public static boolean inRange(int r, int c){
        return(0<=r && r<n && 0<=c && c<n && !visited[r][c] && grid[r][c]==1);
    }
}