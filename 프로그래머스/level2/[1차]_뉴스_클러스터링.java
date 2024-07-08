import java.util.*;

public class Solution {
    // 문자열을 대문자로 변환
    static String toUpperCase(String str) {
        return str.toUpperCase();
    }

    // 2개의 문자씩 자른 집합을 생성
    static List<String> cutStr(String from) {
        List<String> s = new ArrayList<>();
        for (int i = 0; i < from.length() - 1; i++) {
            if (Character.isUpperCase(from.charAt(i)) && Character.isUpperCase(from.charAt(i + 1))) {
                s.add("" + from.charAt(i) + from.charAt(i + 1));
            }
        }
        return s;
    }

    // 교집합 및 합집합 계산
    static int clustering(List<String> s1, List<String> s2) {
        if (s1.size() < s2.size()) {
            List<String> tmp = s1;
            s1 = s2;
            s2 = tmp;
        }
        
        List<String> intersection = new ArrayList<>();
        List<String> union = new ArrayList<>(s1);
        
        for (String key : s2) {
            if (s1.contains(key)) {
                intersection.add(key);
                s1.remove(key);
            } else {
                union.add(key);
            }
        }

        double jaccardSimilarity = (double) intersection.size() / union.size();
        return (int) (jaccardSimilarity * 65536);
    }

    public int solution(String str1, String str2) {
        // 대문자로 변환
        str1 = toUpperCase(str1);
        str2 = toUpperCase(str2);

        // 두 문자씩 자른 집합 생성
        List<String> s1 = cutStr(str1);
        List<String> s2 = cutStr(str2);

        // 자카드 유사도 계산
        if (s1.isEmpty() && s2.isEmpty()) {
            return 65536;
        }
        if (s1.isEmpty() || s2.isEmpty()) {
            return 0;
        }

        return clustering(s1, s2);
    }

   
}
