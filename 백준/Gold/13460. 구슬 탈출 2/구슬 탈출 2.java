import java.util.*;
import java.io.*;

class State{
    int rr,rc;
    int br,bc;
    int count;

    public State(int rr,int rc, int br, int bc, int count){
        this.rr = rr;
        this.rc = rc;
        this.br = br;
        this.bc = bc;
        this.count = count;
    }
}

class MoveResult{
    int r;
    int c;
    int moveCnt;

    public MoveResult(int r, int c, int moveCnt){
        this.r = r;
        this.c = c;
        this.moveCnt = moveCnt;
    }
}

class Main {
    public static int n,m;
    public static int redR, redC, blueR, blueC, holeR, holeC;
    public static char[][] grid;
    public static boolean[][][][] visited;
    public static int answer = -1;
    public static Queue<State> q = new LinkedList<>();
    public static int[] dr = new int[] {-1,1,0,0};
    public static int[] dc = new int[] {0,0,-1,1};
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        grid = new char[n][m];
        visited = new boolean[n][m][n][m];
        
        for(int i=0; i<n; i++){
            String line = br.readLine();
            for(int j=0; j<m; j++){
                char ch = line.charAt(j);
                if(ch == 'R'){
                    redR = i;
                    redC = j;
                } else if(ch == 'B'){
                    blueR = i;
                    blueC = j;
                    
                } else if(ch == 'O'){
                    holeR = i;
                    holeC = j;
                }
                grid[i][j] = ch;
            } 
        }

        q.add(new State(redR,redC,blueR,blueC,0));
        visited[redR][redC][blueR][blueC] = true;
        
        //bfs시작
        while(!q.isEmpty()){
            State cur = q.poll();
            if (cur.count >= 10) continue;
            
            for(int dir=0; dir<4; dir++){

                MoveResult redMove = move(cur.rr, cur.rc, dir);

                MoveResult blueMove = move(cur.br, cur.bc, dir);

                // blue가 구멍
                if(blueMove.r == holeR && blueMove.c == holeC)
                    continue; //이번 방향은 글렀다!

           
                if(redMove.r == holeR && redMove.c == holeC){
                    answer = cur.count + 1;
                    break;
                    
                }
                
                if(redMove.r == blueMove.r && redMove.c == blueMove.c){
                    if(redMove.moveCnt > blueMove.moveCnt){
                        redMove.r -= dr[dir];
                        redMove.c -= dc[dir];
                    } else {
                        blueMove.r -= dr[dir];
                        blueMove.c -= dc[dir];
                    }
                }

                //visited체크(4차원 visited -> Red와 Blue가 정확히 지금 위치일때 고려된적 있냐)
                int newRR = redMove.r;
                int newRC = redMove.c;
                int newBR = blueMove.r;
                int newBC = blueMove.c;
                
                if(!visited[newRR][newRC][newBR][newBC]){
                
                    visited[newRR][newRC][newBR][newBC] = true;
                
                    q.add(new State(newRR, newRC, newBR, newBC, cur.count + 1));
        }

            }
            
            if(answer != -1) break;
            
            
        }


    System.out.println(answer);
    }

    public static MoveResult move(int r, int c, int dir){
        int cnt = 0;

        while(grid[r + dr[dir]][c + dc[dir]] != '#'){
        r += dr[dir];
        c += dc[dir];
        cnt++;

        if(grid[r][c] == 'O') break;
    }

        return new MoveResult(r,c,cnt);
    }


}