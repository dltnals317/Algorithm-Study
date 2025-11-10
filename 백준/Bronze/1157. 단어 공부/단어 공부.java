import java.util.*;
import java.lang.*;
import java.io.*;


class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        s = s.toLowerCase();
        HashMap<Character,Integer> map = new HashMap<>();

        for(char c: s.toCharArray()){
            map.put(c,map.getOrDefault(c,0)+1);
        }

        int max_cnt = 0;
        int max_val = 0;
        Character max_char='?';
    

        for (Map.Entry<Character,Integer> e : map.entrySet()){
            if (e.getValue() > max_val){
                max_cnt = 1;
                max_val = e.getValue();
                max_char = e.getKey();
            } else if(e.getValue() == max_val){
                max_cnt +=1;
            }
        }
        if (max_cnt == 1){
            System.out.println(Character.toUpperCase(max_char));}
        else{
            System.out.println("?");}
    }
}