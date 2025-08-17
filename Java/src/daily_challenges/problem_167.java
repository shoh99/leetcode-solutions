package daily_challenges;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class problem_167 {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (right > left) {
            int sum = numbers[left] + numbers[right];

            if (sum == target) {
                break;
            } else if(sum > target) {
                right --;
            } else {
                left ++;
            }
        }

        return new int[]{left + 1, right + 1};
    }

    public static void main(String[] args) {
        problem_167 problem167 = new problem_167();
        int[] numbers = new int[]{2,3,4};
        int target = 6;

        int[] res = problem167.twoSum(numbers, target);

        System.out.println(Arrays.toString(res));
    }
}


