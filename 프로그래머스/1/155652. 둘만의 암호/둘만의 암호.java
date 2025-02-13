import java.util.*;

public class Solution {
    public static String solution(String s, String skip, int index) {
        // 알파벳 리스트를 생성
        List<Character> alphaList = new ArrayList<>(Arrays.asList(
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ));
        
        // skip에 포함된 문자 제거
        for (char ch : skip.toCharArray()) {
            alphaList.remove(Character.valueOf(ch));
        }
        
        // 결과 문자열을 저장할 StringBuilder
        StringBuilder answer = new StringBuilder();
        
        // 주어진 문자열 s를 순회하며 변환
        for (char ch : s.toCharArray()) {
            // 현재 문자의 인덱스를 찾기
            int idx = alphaList.indexOf(ch);
            // 변환할 문자 인덱스 계산
            int changeIdx = (idx + index) % alphaList.size();
            // 변환된 문자 추가
            answer.append(alphaList.get(changeIdx));
        }
        
        return answer.toString();
    }
    
    public static void main(String[] args) {
        // 테스트 실행
        System.out.println(solution("abc", "b", 2)); // 예시 테스트
    }
}
