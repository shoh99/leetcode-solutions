package ArraysAndHashes;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import static java.util.Arrays.stream;

public class RemoveElement {

    public int removeElement(int[] nums, int val) {
        int idx = 0;
        List<Integer> newArray = new ArrayList<>();

        for (int num : nums) {
            newArray.add(num);
        }

       while (newArray.size() > idx) {

           if (newArray.get(idx) == val) {
               newArray.remove(idx);
               continue;
           }
           idx ++;
       }

       for (int i=0; i<newArray.size(); i++) {
           nums[i] = newArray.get(i);
       }

        for (int num : nums) {
            System.out.println(num);
        }

       return newArray.size();
    }

    public static void main(String[] args) {
        RemoveElement removeElement = new RemoveElement();
        int[] input = {0,1,2,2,3,0,4,2};
        removeElement.removeElement(input, 2);
    }
}
