import java.util.*;

class Solution {
    public String solution(String my_string, int n) {
       StringBuilder sb = new StringBuilder();
       
       for(int i = 0; i<my_string.length(); i++){
        char ch = my_string.charAt(i);
        sb.append(String.valueOf(ch).repeat(n));
       }
        String result = sb.toString();
        return result;
       }
        
    }