package daily_challenges;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class problem_347 {

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequentElements = new HashMap<>();

        for (int i: nums) {
           frequentElements.put(i, frequentElements.getOrDefault(i, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(frequentElements.entrySet());
        entryList.sort(Map.Entry.<Integer, Integer>comparingByValue().reversed());

        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            result[i] = entryList.get(i).getKey();
        }

        return result;
    }

    public static void main(String[] args) {
        problem_347 problem347 = new problem_347();
        int[] nums = {1,1,1,2,2,3};
        int k = 2;

        int[] result =  problem347.topKFrequent(nums, k);

        for (int num: result) {
            System.out.print(num + " ");
        }
    }
}
