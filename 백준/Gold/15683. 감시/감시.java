import java.util.*;
import java.lang.*;
import java.io.*;


class Dir{
    int dr,dc;
    public Dir(int dr, int dc){
        this.dr = dr;
        this.dc = dc;
    }
}
class CctvInfo {
    int r, c, type;

    CctvInfo(int r, int c, int type) {
        this.r = r;
        this.c = c;
        this.type = type;
    }
}

class Main {
    public static int n,m;
    public static int[][] grid;

    // CCTV 타입별 "회전 경우들의 목록"
    // rotationByType[type] = List<회전 경우>
    // 회전 경우 = List<Dir>
    public static List<List<Dir>>[] rotationByType; 
    

    public static List<CctvInfo> cctvList;

    static int answer = Integer.MAX_VALUE;

    // 상하좌우
    static final int MAX_GRID_SIZE = 8;
   
    
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        grid = new int[n][m];
        
        cctvList = new ArrayList<>();
        

    

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
                if (grid[i][j] == 1 || grid[i][j] == 2 || grid[i][j] == 3 || grid[i][j] == 4 || grid[i][j] == 5){
                    cctvList.add(new CctvInfo(i,j,grid[i][j]));
                }
                
                
            }
        }

        initialize();
        backTracking(0);
        System.out.println(answer);
    }

    public static void initialize(){
        rotationByType = new ArrayList[6]; //리스트 안에
        for(int i=1; i<=5; i++){
            rotationByType[i] = new ArrayList<>(); //리스트(우회)
        }

        // 1번 CCTV 값 채우기(4가지 경우의수)
        
        //rotationByType[1] -> 이미 리스트. 그 안에 또 4개의 리스트(방향정보) 넣겠다
        rotationByType[1].add(List.of(new Dir(0,1)));
        rotationByType[1].add(List.of(new Dir(-1,0)));
        rotationByType[1].add(List.of(new Dir(0,-1)));
        rotationByType[1].add(List.of(new Dir(1,0)));



        // 2번 CCTV 값 채우기 (2가지 경우의수)
        rotationByType[2].add(List.of(new Dir(0,-1), new Dir(0,1)));
        rotationByType[2].add(List.of(new Dir(-1,0), new Dir(1,0)));


        // 3번 CCTV 값 채우기(4가지 경우의수)
        rotationByType[3].add(List.of(new Dir(-1,0),new Dir(0,1)));
        rotationByType[3].add(List.of(new Dir(0,-1),new Dir(-1,0)));
        rotationByType[3].add(List.of(new Dir(1,0),new Dir(0,-1)));
        rotationByType[3].add(List.of(new Dir(0,1),new Dir(1,0)));


        // 4번 CCTV 값 채우기(4가지 경우의수)
        rotationByType[4].add(List.of(new Dir(0,-1),new Dir(-1,0),new Dir(0,1)));
        rotationByType[4].add(List.of(new Dir(0,-1),new Dir(1,0),new Dir(0,1)));
        rotationByType[4].add(List.of(new Dir(-1,0),new Dir(0,-1),new Dir(1,0)));
        rotationByType[4].add(List.of(new Dir(-1,0),new Dir(0,1),new Dir(1,0)));


        // 5번 CCTV 값 채우기(1가지 경우의수)
        rotationByType[5].add(List.of(new Dir(0,-1),new Dir(-1,0),new Dir(1,0),new Dir(0,1)));
    }


    public static boolean canGo(int newR, int newC){ //!visited[newR][newC] -> 포함 X 왜냐면, 방문 했더라도, 지나쳐서 나아갈수 있잖아. 막히는게 아니니까
        return (inRange(newR,newC)&& grid[newR][newC]!=6);
    }

    public static boolean inRange(int r,int c){
        return(0<=r && r<n && 0<=c && c<m);

    }

   //어떤 알고리즘을 써서, 감시를 진행해야할까? 백트래킹? BFS? DFS?
   // 목표: "사각 지대의 최소 크기" ==> 즉, 최대한 많은 영역을 감시하는 방향의 조합을 골라야함

   /*백트래킹.. -> cctv 1번~5번마다, 가능한 방향의 수는 서로 다른데, 최적의 조합(가장 많이 차지할 수 있는) 조합을 찾는거니까, 
      1번부터 cctv돌면서, 해당 방향을 선택했을 때, 2번cctv선택으로 넘어가고, 다시 방향 선택한거 취소하고.. 전형적이 백트래킹같음*/

    public static void backTracking(int idx){ //백트래킹은 3가지 절차가 중요했던거같은데,, (1. 종료조건 2.가지치기 3. 되돌리기)

        //1. 종료조건: 모든 CCTV에 대해 방향 선택 완료
        if(idx ==cctvList.size()){ //cctv 다 돌았다면 끝
            answer = Math.min(answer, countBlindSpot());
            return;
        }
        CctvInfo cctv = cctvList.get(idx);
        int r = cctv.r;
        int c = cctv.c;
        int type = cctv.type;

        
        // 이 CCTV 타입(1~5)이 가질 수 있는 모든  경우 시도
        for(List<Dir> dirs : rotationByType[type]){ //dirs 각각은, 독립적임

            // 되돌리기(undo)를 위해
            // 이번 CCTV로 새롭게 감시한 칸들만 저장
            List<int[]> changed = new ArrayList<>();

            // 한 회전 경우(dirs)에서 "동시에" 감시되는 모든 방향 처리
            for(Dir d : dirs){
                int nr = r;
                int nc = c;

                while(true){
                    nr = nr + d.dr;
                    nc = nc + d.dc;

                    if(!canGo(nr,nc)) break;

                    // 빈 칸(0)만 감시 표시
                    if(grid[nr][nc] == 0){
                        grid[nr][nc] = -1;
                        changed.add(new int[]{nr,nc}); //이번 시도 때, 변화시킨거 임시기록(나중에 복구위해)
                    } 
                }
            }

        //다음 idx를 cctvList에서 꺼내야함
        backTracking(idx+1);


        //되돌리기(이번 CCTV가 만든 변화만 원상복구do)
        for(int[] pos: changed){
            grid[pos[0]][pos[1]] = 0;

        }
       
        }

    }

    public static int countBlindSpot(){
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0) cnt++;
            }
        }
        return cnt;
    }
}