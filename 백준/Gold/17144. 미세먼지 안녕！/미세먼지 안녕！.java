import java.util.*;
import java.lang.*;
import java.io.*;



/*
Task1) 미세먼지 확산하기
- 주의 : /5하며 계산하는 과정이 -> original 양에서 바뀐 기준으로 하면 안됨. 즉, 처음 정해진 미세먼지 양 기준으로 확산되는양 & 남는양 계산한 채 => 모든 좌표에 대해 동시에 확산해야함
- 확산 범위 볼 때 dr,dc 테크닉 사용하되, 벽이거나 or 공기청정기라면 확산 x

- 초기상태의 grid와, spreadArea기록 반영해나가는 grid 별도로 두어야함. Task2 공기청정기 작동은 두 번째 grid기준!


Task2) 공기청정기 작동
공기청정기 두 칸중 -> 위칸은 반시계방향 & 아래칸을 시계방향
- 영역 테두리에 없는 공간은, 공기청정기의 영향을 받지 않는다
-- 먼저, 윗 영역 -> 테두리만 1차원 배열에 넣고 반시계회전 -> 다시 윗영역 테두리에 대입 
-- 이어서, 아래 영역 -> 테두리만 1차원 배열에 넣고 반시계회전 -> 다시 아래 영역 테두리에 대입
=> 이렇게 회전 결과 테두리에 다시 대입
=> 이 때, idx=0 를 공기청정기 놓인 영역으로 보고 -> 회전 결과 idx=0에 양수 값이 있다면 -> 그 값은 0으로 만든다

이 Task1 + Task2를 T초동안 반복 -> t 갱신하기 전에, grid를 spreadArea로 업데이트
*/
class Main {
    public static int r,c,t;
    public static int[][] grid;
    public static int[][] spreadArea;
    public static int[][] vacuumList = new int[2][2];
    public static int[] dr = new int[]{-1,1,0,0};
    public static int[] dc = new int[]{0,0,-1,1};
    public static int answer = 0;
    public static void main(String[] args) throws IOException{
       
    

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    r = Integer.parseInt(st.nextToken());
    c = Integer.parseInt(st.nextToken());
    t = Integer.parseInt(st.nextToken());

    grid = new int[r][c];
    spreadArea = new int[r][c];

    //original grid 초기화
    int vaccumCnt = 0;
    for(int i=0; i<r; i++){
      st = new StringTokenizer(br.readLine());
      for(int j=0; j<c; j++){
        grid[i][j] = Integer.parseInt(st.nextToken());
        if(grid[i][j] > 0){
          spreadArea[i][j] = grid[i][j];
        }
         
         if(grid[i][j] == -1 && vaccumCnt==0){
          vacuumList[0][0] = i;
          vacuumList[0][1] = j;

          vacuumList[1][0] = i + 1;
          vacuumList[1][1] = j;

          vaccumCnt++;
        }
      }
    }
 for(int time=0; time<t; time++){
  for (int i = 0; i < r; i++) {
    for (int j = 0; j < c; j++) {
        if (grid[i][j] == -1) spreadArea[i][j] = -1;
        else spreadArea[i][j] = grid[i][j];
    }
    }
  checkAndUpdateDustArea();
  // 두 영역 boundary 추출한 뒤, 회전시키는 함수(이게 좀 어려울듯)
  // 회전 결과 기반 spreadArea 업데이트한 후, 그걸 original grid에 대입하며 이번 턴 종료

  runVaccum();
  for(int i=0; i<r; i++){
    for(int j=0; j<c; j++){
      grid[i][j] = spreadArea[i][j];
    }
  }

  }


  //이중 for문 -> 남은 dust합산하는 함수
  for(int i=0; i<r; i++){
    for(int j=0; j<c; j++){
      if(grid[i][j]>0){
        answer+=grid[i][j];
      }
    }
  }

  System.out.println(answer);


}

  public static void checkAndUpdateDustArea(){
    for(int i=0; i<r; i++){
      for(int j=0; j<c; j++){
        if(grid[i][j]>0){
        int cnt=0;
        int spreadVal = grid[i][j]/5;
          for(int d=0; d<4; d++){
            int nr = i + dr[d];
            int nc = j + dc[d];
            
            if(inRange(nr,nc)){ //확산 가능
              spreadArea[nr][nc] += spreadVal;
              cnt++;
            }
          }
          spreadArea[i][j] -= spreadVal * cnt;
        }
      }
    }
  } //전역변수 spreadArea 업데이트 완료(이번 t에 한함)

  public static boolean inRange(int nr, int nc){
    boolean notWall = (0<=nr && nr < r && 0<=nc && nc < c);
    boolean notVacuumList = true;
    for(int x=0; x<2; x++){
      int rr = vacuumList[x][0];
      int cc = vacuumList[x][1];
      if (rr == nr && cc == nc){
        notVacuumList = false;
        break;
      }
    }
    return(notWall && notVacuumList);
  }


  // 두 영역 boundary 추출한 뒤, 회전시키는 함수(이게 좀 어려울듯)
  public static void runVaccum(){
    //area를 위,아래로 나눠야하고, 청소기 위치(vaccumList에 있는 값)에 따라, 크기가 다름

    // int r1 = vacuumList[0][0];
    // int c1 = vacuumList[0][1];

    // int r2 = vacuumList[1][0];
    // int c2 = vacuumList[1][1];

    int firstRow = vacuumList[0][0];   // 위쪽 청소기 row
    int secondRow = vacuumList[1][0];  // 아래쪽 청소기 row

  //c*2 + (r-1)*2
  //c*2 + (r-r2-2)*2
   
    
     //청소기 위치는 항상 0 -> 안전하게 추가
      spreadArea[firstRow][0] = 0;
      spreadArea[secondRow][0] = 0;

      //위쪽 영역
      List<Integer> upperFlat  = extractBorder(spreadArea,0,0,firstRow,c-1);
      Collections.rotate(upperFlat,-1); //반시계
      applyBorder(spreadArea,0,0,firstRow,c-1,upperFlat);
   

      //아래쪽 영역
      List<Integer> lowerFlat  = extractBorder(spreadArea,secondRow,0,r-1,c-1);
      Collections.rotate(lowerFlat,1);
      applyBorder(spreadArea,secondRow,0,r-1,c-1,lowerFlat);


      //청소기 위치는 항상 0
      spreadArea[firstRow][0] = 0;
      spreadArea[secondRow][0] = 0;

  }

  public static void applyBorder(int a[][], int firstRow,int firstCol, int secondRow,int secondCol, List<Integer> flat){
    
    int idx = 0;
    //위쪽 채우기
    for(int c=firstCol; c<=secondCol; c++){
      int val = flat.get(idx);
      idx++;
      spreadArea[firstRow][c] = val;
    }


    //오른쪽 채우기
    for(int r=firstRow+1; r<=secondRow-1; r++){
      int val = flat.get(idx);
      idx++;
      spreadArea[r][secondCol] = val;
    }



    //아래쪽 채우기
     for(int c=secondCol; c>=firstCol; c--){
      int val = flat.get(idx);
      idx++;
      spreadArea[secondRow][c] = val;
    }
    

    //왼쪽 채우기
      for(int r=secondRow-1; r>=firstRow+1; r--){
      int val = flat.get(idx);
      idx++;
      spreadArea[r][firstCol]= val;
    }
    
  }


  //시계방향 flat(모서리(코너)를 중복해서 넣지 않기 위한 장치 필요) (first,second로 변수명 정한 이유는 -> 위쪽 영역과 아래쪽영역이 이 함수로 공유가능)
  public static List<Integer> extractBorder(int[][]a, int firstRow,int firstCol, int secondRow,int secondCol){
    List<Integer> flatList = new ArrayList<>();

    //위쪽(좌->우) : 코너 포함
    for(int c = firstCol; c<=secondCol; c++){
      flatList.add(a[firstRow][c]);

    }

    //오른쪽(위-> 아래)
    for(int r = firstRow+1; r<=secondRow-1; r++){
      flatList.add(a[r][secondCol]);

    }

    //아래(우->좌)
    for(int c = secondCol; c>=firstCol; c--){
      flatList.add(a[secondRow][c]);

    }

    //왼(아래->위)
    for(int r = secondRow-1; r>=firstRow+1; r--){
      flatList.add(a[r][firstCol]);

    }
    return flatList;
  }

}