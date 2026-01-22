import java.io.*;
import java.util.*;

/*
point 1) 현재 지점(r,c) 에서 -> 상,하,좌,우로 이동하는 경우 => 직선이동 (100원)

point2) 코너는 언제냐
(r과 c를 동시에 증가시키는 경우, 즉 대각선 이동은 없으므로)
현재 변화가되는 기준이 r인지 c인지 추적하면서,
변화기준이 바뀌는 순간 -> 코너

(0,5) -> (0,5+1=6) -> (0+1=1,6)
변화기준이 c에서, r로 바뀌었으므로 코너


(3,6) -> (3+1=4,6) -> (4,6-1=5) 
기준:r     기준:c <코너>  기준:c    

(4,5) -> (4,5-1=4) -> (4+1=5,4)
기준:c     기준:r <코너> 기준:r   
=> 즉, 기준이 전환되는 기점이, 코너의 꼭지점이됨

- (while q)
  (r,c)의 네 방향 탐색
  q에는 뭘 넣냐면
  (nr,nc,이전 기준(r또는c),누적 금액(100추가 r->r이거나, c->c면 100 추가 & 전환되면-> 100+500(코너비용)추가 ))
  
(point4)
구해야하는게 "최소 비용" 이지, 최단거리가 아닌 상황
=> visited로 방문을 차단하면, dp처럼, 다른 경우로부터 더 적은 비용으로 해당 지점에 도달할 수 있는 가능성이 차단되는거 아닌가?
이미 방문 했을 때 -> 지금 방문이 더 최소비용인지 확인해야하나? (그럼 dp인데,,)


*/
class Solution {
    static final int ROW_DIRECTION_NUM = 0;
    static final int COL_DIRECTION_NUM = 1;
    static class PosInfo {
        int r, c ,preDir,totalExp;
        PosInfo(int r, int c, int preDir, int totalExp) {
            this.r = r;
            this.c = c;
            
            // r : -1 , c: 1
            this.preDir = preDir; //(0,0)의 경우 PosInfo(0,0,ROW_DIRECTION_NUM,0) , PosInfo(0,0,COL_DIRECTION_NUM,0) 으로 초기화
            this.totalExp = totalExp;
        }
    }
    int n;
    int[][] board;
    int[] dr,dc;
    boolean[][] visitedAsStartSpot;
    int[][][] expenseDP;
    //PosInfo[][] posArr;
    Queue<PosInfo> q;
    int answer;
    
    
    
    public int solution(int[][] input) {
        board = input;
        n = board.length;
        dr = new int[]{-1,1,0,0};
        dc = new int[]{0,0,-1,1};
        
        //posArr = new PosInfo[n][n];
        expenseDP = new int[n][n][2];
        answer = Integer.MAX_VALUE;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                expenseDP[i][j][0] = Integer.MAX_VALUE;
                expenseDP[i][j][1] = Integer.MAX_VALUE;
            }
        }
        q = new ArrayDeque<>();
        q.add(new PosInfo(0,0,ROW_DIRECTION_NUM,0));
        q.add(new PosInfo(0,0,COL_DIRECTION_NUM,0));
        
        bfsByDp();
        
        
        return answer;
    }
    
    
    boolean canGo(int r, int c){
        
            
        return (inRange(r,c) && board[r][c]==0); //!visited[r][c] 일단 삭제
    }
    
    boolean inRange(int r,int c){
        return(0<=r && r<n && 0<=c && c<n);    
    }
    
    void bfsByDp(){
        while(!q.isEmpty()){
            PosInfo now = q.poll();
            int r = now.r;
            int c = now.c;
            int preDir = now.preDir;
            int totalExp = now.totalExp;
        
            
            
            if(r==n-1 && c==n-1){
                answer = Math.min(answer,expenseDP[r][c][preDir]);
            }
            //if(visitedAsStartSpot[r][c]) continue;
            //딜레마 : (nr,nc)가 (0,0)을 다시 돌아오는걸 방지하기 위해, 방문처리 해줘야할거같긴 한데
            //방문처리 해주다보면, 최소값을 구하기 어려워질 수 있는데..
            
            for(int i=0; i<4; i++){ //상,하
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if(!canGo(nr,nc)) continue;
                
                int newExp = totalExp + 100;
                int dir = (i<2) ? ROW_DIRECTION_NUM : COL_DIRECTION_NUM;
                if(r==0 && c==0){
                    preDir = dir;
                }
                
                // System.out.println("(r,c) = "+ r + "," + c);
                // System.out.println("preDir = "+ preDir);
                // System.out.println("totalExp = "+ totalExp);
                // System.out.println("(nr,nc) = "+ nr + "," + nc);
                // System.out.println("newDir = "+ dir);
                // System.out.println("==================");
                if(isCorner(preDir, dir)){
                    newExp+=500;
                }
                
                if(expenseDP[nr][nc][dir] > newExp){
                    expenseDP[nr][nc][dir] = newExp;
                    q.add(new PosInfo(nr,nc,dir,expenseDP[nr][nc][dir]));
                } 
            }

            }
            
    }    
    boolean isCorner(int prevD,int nowD){
        if(prevD==nowD){
            return false;
        }else{
            return true;
        }
    } 
        
}