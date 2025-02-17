import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        List<Integer> selectedType = new ArrayList<>();
        Map<Integer,Integer> hs = new HashMap<>();
        
        int typeNum = 0;
        int gotNum = 0;
        int PossibleNum = nums.length/2;
            
        for(int pocketmon : nums){
            hs.put(pocketmon,hs.getOrDefault(pocketmon,0)+1);
        }
        
        while (gotNum < PossibleNum){
            for (int type : hs.keySet()){
                if (gotNum == PossibleNum){
                break;
            } else{
                if (hs.get(type) > 0){
                    if (!selectedType.contains(type)){
                        typeNum++;
                        selectedType.add(type);
                    }
                    hs.put(type,hs.get(type)-1);
                    gotNum++;
                
                }
        
                }
                
            }
        }
        
        return typeNum;
    }
    
}