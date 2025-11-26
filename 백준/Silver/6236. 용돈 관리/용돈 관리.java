import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    static int n,m;
    static int price;
    static int cnt;
    static int[] pricePlanes;

    public static int withdrawCountCheck(int k){ // k>= max(pricePlanes) //최소 인출 횟수
        int count = 1;
        int currentMoney = k;

        for(int price : pricePlanes){
            if(currentMoney < price){ //부족하면 인출
                count++;
                currentMoney = k;
            }
            currentMoney -=price;
            // 뽑을 수 있는 금액k보다 가격이 큰 상황은 발생하지 않음(main에서 left를 최대 price로 설정했으므로)(뽑으면 무조건 계산 가능)
            
        }
        return count;
    }
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        pricePlanes = new int[n];

        int maxPrice = 0; //leftBound
        int totalSum = 0; //rightBound
        
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            pricePlanes[i] = Integer.parseInt(st.nextToken());

            maxPrice = Math.max(maxPrice,pricePlanes[i]);
            totalSum += pricePlanes[i];
        }

        int left = maxPrice;
        int right = totalSum;
        int answer = totalSum; //가능한 가장 큰 k로 초기화
        
        while(left<=right){
            int mid = (left+right) / 2;

            int count = withdrawCountCheck(mid);
            if(count <=m){ //mid가 유효한 k후보라는 뜻 -> 일단 저장하고, 더 작은 k를 탐색하기 위해, 범위를 좀힘
                answer = mid;
                right = mid - 1;   
            }else{ //count > m : 인출 횟수를 줄이려면, k를 높여야함
                left = mid + 1;      
            }
        }
        System.out.println(answer);
            }
            
        }  
