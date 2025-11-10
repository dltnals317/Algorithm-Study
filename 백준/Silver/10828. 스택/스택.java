import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        for(int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
                
            if (command.equals("push")){
                int x = Integer.parseInt(st.nextToken());
                stack.push(x);
                
            }else if(command.equals("pop")){
                System.out.println(stack.empty() ? -1 : stack.pop()); 
                
            }else if(command.equals("size")){
                System.out.println(stack.size());
                
            }else if(command.equals("empty")){
                System.out.println(stack.empty() ? 1 : 0);
                
            }else{
                System.out.println(stack.empty() ? -1 : stack.peek());
                
            }
        }
    }
}