import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public String solution(String my_string) {
        String result = Arrays.stream(my_string.split(""))
            .filter(ch -> !"aeiou".contains(ch))
            .collect(Collectors.joining());
                          
        return result;
    }
}