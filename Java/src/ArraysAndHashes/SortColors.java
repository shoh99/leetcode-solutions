package ArraysAndHashes;

import java.util.Arrays;

public class SortColors {

    public void sortColors(int[] nums) {
        for (int i=0;i<nums.length;i++) {

            int minValue = nums[i];
            int minIndex = i;

            for (int j=i+1; j<nums.length; j++) {
                int currentNum = nums[j];
                if (currentNum < minValue) {
                    minValue = nums[j];
                    minIndex = j;
                }
            }
            nums[minIndex] = nums[i];
            nums[i] = minValue;
        }
        System.out.println(Arrays.toString(nums));
    }

    public static void main(String[] args) {
        SortColors sortArray = new SortColors();
        int[] nums = {2,0,1};
        sortArray.sortColors(nums);
    }
}
