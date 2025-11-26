import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {

    static int n;
    static int[] prices;
    static int m;

    public static boolean budgetcheck(int k){
        int total = 0;
        for (int i=0; i<n; i++){
            if (prices[i]>k){
                total += k;
            }
            else{
                total += prices[i];
            }    
        }
        if (total<=m){
            return true;
        }
        return false;
        
    }
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        prices = new int[n];

        int maxPrice = 0;
        int totalBudget = 0;

        st = new StringTokenizer(br.readLine()); //N개의 예산 요청을 한 줄로 읽고 StringTokenizer를 만듭니다.
        for(int i=0; i<n; i++){
            prices[i] = Integer.parseInt(st.nextToken());
            maxPrice = Math.max(maxPrice,prices[i]);
            totalBudget += prices[i];
        }
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());


        //1. 총 예산이 충분한지 예외처리
        if(totalBudget<=m){
            System.out.println(maxPrice);
            return;
        }

        //2. 총 예산이 부족한 경우에만 이분 탐색
        // 탐색 범위 : (1~요청 금액 중 최댓값)
        int left = 1;
        int right = maxPrice;
        int answer = 0;

        while(left<=right){
            int mid = (left+right) / 2;
            if(budgetcheck(mid)){ //가능하면 -> 상한 더 늘려도됨
                left = mid+1;
                answer = mid;
            }
            else{
                right = mid-1;
        }
            
    }
        System.out.println(answer);
}
}