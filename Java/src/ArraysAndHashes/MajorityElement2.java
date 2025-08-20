package ArraysAndHashes;

import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class MajorityElement2 {
    public List<Integer> findMajorityElement(int[] nums) {
        int candidate1 = 0, candidate2 = 0;
        int count1 = 0, count2 = 0;

        for(int num: nums) {
            if(count1 == 0 && num != candidate2) {
                candidate1 = num;
                count1 = 1;
            } else if(count2 == 0 && num != candidate1) {
                candidate2 = num;
                count2 = 1;
            } else if (candidate1 == num) {
                count1 ++;
            } else if(candidate2 == num) {
                count2 ++;
            } else {
                count1 --;
                count2 --;
            }
        }

        count1 = 0;
        count2 = 0;

        for (int num: nums) {
            if (num == candidate1) {
                count1 ++;
            } else if (num == candidate2)  {
                count2++;
            }
        }

        List<Integer> majorityElements = new ArrayList<>();
        int threshold = nums.length / 3+1;

        if (threshold <= count1) {
            majorityElements.add(candidate1);
        }

        if(threshold <= count2) {
            majorityElements.add(candidate2);
        }

        return majorityElements;
    }

    public static void main(String[] args) {
        MajorityElement2 majorityElement2 = new MajorityElement2();

        int[] nums = {1,2,3};
        System.out.println( majorityElement2.findMajorityElement(nums).toString());
    }
}
