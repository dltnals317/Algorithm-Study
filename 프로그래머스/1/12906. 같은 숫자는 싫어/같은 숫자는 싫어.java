import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        
        
        ArrayList<Integer> lst = new ArrayList<>();
        
        for(int num : arr){
            if (lst.isEmpty() || lst.get(lst.size()-1) != num){
                lst.add(num);
            }
        }
        
        int[] answer = new int[lst.size()];
        for (int i=0; i<lst.size(); i++){
            answer[i] = lst.get(i); //i번째 인덱스 원소 가져오기
        }
        
        return answer;
    }
}