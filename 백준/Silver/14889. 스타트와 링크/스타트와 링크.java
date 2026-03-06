import java.util.*;
import java.lang.*;
import java.io.*;

/*
- 의무 참석X => 이게 왜있는걸까?
- 스타트팀의 능력치 차이와, 링크 팀의 능력치 차이 최소화
- 두 그룹으로 나눌 때, 판단을 어떻게 해야할까 생각해보자
--> 일단, backtracking함수에서, 몇개가 가득차야 undo할지를 생각해보면, N/2겠지?
--> 그럼, N/2개의 리스트를 만들어서? => nowOrder > N/2 => 이러면, 그 경우의수는 다 고른거이므로 되돌리고..

- 그전에, 내가 항상 헷갈려하던 포인트 => 이건 순열 백트래킹이야, 조합 백트래킹이야?
 => 조합기준으로 하되, 뒤바꿔서도 세주면 되지 않나? (조합 백트래킹이 더 익숙해서...)

//두 개의 자료구조로, 1번그룹 능력치 담는 그릇 & 2번그룹 능력치 담는 그릇 관리하는거보다
// 하나만 관리하고, -> 나머지 그룹은 -> 전체능력치에서 빼도 되지않나..?(X. 대부분 실패한다고함 BY GPT)

=> 생각해보니... 대각선 기점으로 분리하고,, 1-> 2,3,4중 2개 택 2 -> 1,3,4중 2개 택.. 이런식
만약, 1 행 -> 2,3택하면(S12,S13) -> 곧바로 S21, S31도 능력치 합산 후, 선택지에서 없애버린다

*/

class Main {
    public static int n;
    public static int numberOfSameGroup;
    public static int[][] sGrid;
    //public static int total = 0;
    public static int[] startTeam;
    public static int[] linkTeam;
    public static boolean[] visited;
    public static int answer=Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        sGrid = new int[n][n];
        numberOfSameGroup = n/2;
        startTeam = new int[numberOfSameGroup+1];
        linkTeam = new int[numberOfSameGroup+1];
        visited = new boolean[n+1];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++){
                sGrid[i][j] = Integer.parseInt(st.nextToken());
                //total += sGrid[i][j];
                
            }
        }
        for(int num = 1; num<= n; num++){
            backtracking(1,num); //첫번째 순서부터 시작
        }

        System.out.println(answer);
        
    }

    public static void backtracking(int nowOrder,int startNum){
        if(startNum > n){
            return;
        }
        
        if (visited[startNum] == true) return;
        //종료조건 
        if(nowOrder > numberOfSameGroup){ //이미 리스트 완료된 상태
            int startTeamScore = 0;
            int linkTeamScore = 0;
            for(int i=1; i<=numberOfSameGroup; i++){
                int idx = startTeam[i];
                for(int j=i+1; j<=numberOfSameGroup; j++){
                    int a = startTeam[i]-1;
                    int b = startTeam[j]-1;

                    startTeamScore += sGrid[a][b] + sGrid[b][a];
                }
            }    

            int idx = 1;
            for(int i=1; i<=n; i++){
                if(!visited[i]){
                    linkTeam[idx++] = i;
                }
            }
            for(int i=1;i<=numberOfSameGroup;i++){
                for(int j=i+1;j<=numberOfSameGroup;j++){
                    int a = linkTeam[i]-1;
                    int b = linkTeam[j]-1;

                    linkTeamScore += sGrid[a][b] + sGrid[b][a];
                }
            }
            answer = Math.min(answer,Math.abs(startTeamScore-linkTeamScore));
            return;
                
        }

        //nowOrder< numberOfSameGroup 이지만, 벌써 학생 다 돌았다면 -> 종료
        

        //고른다
        visited[startNum] = true;
        startTeam[nowOrder] =  startNum;
        backtracking(nowOrder + 1,startNum+1);

        //안고른다
        visited[startNum] = false;
        backtracking(nowOrder,startNum+1);

    }
       
}