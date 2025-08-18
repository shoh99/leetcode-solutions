package ArraysAndHashes;

import java.util.Arrays;
import java.util.List;

public class SortArray {

    public int[] sort(int[] nums) {
        if (nums.length <= 1) {
            return nums;
        }

        int middleIndex = nums.length / 2;

        int[] leftHalf = Arrays.copyOfRange(nums, 0, middleIndex);
        int[] rightHalf = Arrays.copyOfRange(nums, middleIndex, nums.length);

        System.out.println(Arrays.toString(leftHalf));
        System.out.println(Arrays.toString(rightHalf));

        int[] sortedLeft = sort(leftHalf);
        int[] sortedRight = sort(rightHalf);

        return merge(sortedLeft, sortedRight);
    }

    public int[] merge(int[] leftHalf, int[] rightHalf) {
        int i = 0;
        int j = 0;

        int[] result = new int[leftHalf.length + rightHalf.length];
        int index = 0;
        while(i < leftHalf.length && j < rightHalf.length) {
            if (leftHalf[i] < rightHalf[j]) {
                result[index] = leftHalf[i];
                i++;

            } else {
                result[index] = rightHalf[j];
                j++;
            }
            index++;
        }

        while(i < leftHalf.length) {
            result[index] = leftHalf[i];
            i++;
            index++;
        }

        while(j<rightHalf.length) {
            result[index] = rightHalf[j];
            j++;
            index++;
        }

        return result;
    }

    public static void main(String[] args) {
        SortArray sortArray = new SortArray();
//        int[] leftHalf = {2,8};
//        int[] rightHalf = {1,5,9};
//
//        int[] result = sortArray.merge(leftHalf, rightHalf);
//
//        System.out.println(Arrays.toString(result)  );
        int[] nums = {5,1,1,2,0,0};
        int[] result = sortArray.sort(nums);

        System.out.println(Arrays.toString(result));
    }
}
