package daily_challenges;

import java.util.ArrayList;
import java.util.List;

public class problem_1920 {

    public int[] buildArray(int[] nums) {
       int[] list = new int[nums.length];

        for(int i=0; i < nums.length; i++) {
            list[i] = nums[nums[i]];
        }

        return list;
    }

    public static void main(String[] args) {
        int[] nums = {0,2,1,5,3,4};

        problem_1920 problem1920 = new problem_1920();
       for(int num: nums) {
           System.out.println(num);
       }

    }
}
