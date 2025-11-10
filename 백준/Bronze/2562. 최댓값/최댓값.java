import java.io.*;
import java.util.*;


public class Main{
  public static void main(String[] args) throws IOException{
    BufferedReader  br = new BufferedReader(new InputStreamReader(System.in));
    ArrayList<Integer> lst = new ArrayList<>();
    for (int i=0; i<9; i++){
      int num = Integer.parseInt(br.readLine());
      lst.add(num);
    }
    ArrayList<Integer> original_lst = new ArrayList<>(lst);
    Collections.sort(lst);
    int max_num = lst.get(lst.size()-1);
    System.out.println(max_num);
    System.out.println(original_lst.indexOf(max_num)+1);
    
    
  }
}