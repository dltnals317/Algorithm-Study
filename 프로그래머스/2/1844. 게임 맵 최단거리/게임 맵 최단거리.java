import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        
        int[] dr = new int[]{0,1,0,-1};
        int[] dc = new int[]{-1,0,1,0};
        int n = maps.length;
        int m =maps[0].length;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 1}); // 큐에 배열 추가
        
        
        boolean [][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        List<Integer> possibleDistance = new ArrayList<>();
        
        while (!q.isEmpty()){
            int [] now = q.poll();
            int r = now[0];
            int c = now[1];
            int d = now[2];
            
            visited[r][c] = true;
            
            if (r==n-1 && c == m-1){
                possibleDistance.add(d);
            }
            
            for(int i=0; i<4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && maps[nr][nc] == 1){
                    if (visited[nr][nc] == false){
                        visited[nr][nc] = true;
                        q.add(new int[]{nr,nc,d+1});
                    }
                }
                
                }
            
        }
        if (possibleDistance.size() == 0){
                    return -1;
             }
            else{
                return Collections.min(possibleDistance); 
            }
    }  
   
}