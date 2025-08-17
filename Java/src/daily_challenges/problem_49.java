package daily_challenges;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class problem_49 {

    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> mapGroup = new HashMap<>();

        for (String str : strs) {

            String sorted = Stream.of(str.split("")).sorted().collect(Collectors.joining());
            System.out.println(sorted);
            mapGroup.computeIfAbsent(sorted, k -> new ArrayList<>()).add(str);
        }

        mapGroup.forEach((k, v) -> result.add(v));
        return result;
    }

    public static void main(String[] args) {
        String[] strs = {"eat","tea","tan","ate","nat","bat"};

        problem_49 problem49 = new problem_49();
        List<List<String>> result = problem49.groupAnagrams(strs);
    }
}
