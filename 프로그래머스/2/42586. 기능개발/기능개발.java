import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        List<Integer> answerList = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        
        for (int i=0; i< progresses.length; i++){
            int remain_pg = 100-progresses[i];
            
            int need_time = remain_pg / speeds[i];
            
            if (remain_pg % speeds[i] !=0){
                need_time +=1;
            }
            
            q.add(need_time);
        
        }
        
//         int[] answer = new int[q.size()];
//         for (int i=0; i<q.size(); i++){
//             answer[i] = q.get(i);
//         }
        
        int cnt = 1;
        int pivot = q.poll(); //popleft와 같은..
        
        while (!q.isEmpty()){
            int now = q.poll();
            
            if (now <= pivot){
                cnt+=1;
            }
            else{
                answerList.add(cnt);
                cnt = 1;
                pivot = now;
            }
        }
        answerList.add(cnt);
        int [] answer = new int[answerList.size()];
        for(int i=0 ; i<answerList.size(); i++){
            answer[i] = answerList.get(i); //arrayList에서 값을 뽑아오려면, answerList[i]하면 에러가 남. 꼭 get으로 뽑아와야함
        }
        return answer;
    }
}