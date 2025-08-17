package ArraysAndHashes;

import java.security.cert.CertSelector;
import java.util.HashMap;
import java.util.Map;

public class MajorityElement {

    public int majorityElement(int[] nums) {
        Map<Integer, Integer> elementMap = new HashMap<>();

        for(Integer num: nums) {
            if (!elementMap.containsKey(num)) {
                elementMap.put(num, 1);
                continue;
            }

            elementMap.put(num, elementMap.get(num) +1);
        }

        int majorityNum = 0;
        int majorityKey = 0;

        for(Integer key: elementMap.keySet()) {
            Integer currentNum = elementMap.get(key);
            if (currentNum > majorityNum) {
                majorityNum = currentNum;
                majorityKey = key;
            }
        }

        return majorityKey;
    }

    public int improvedMajorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;

        for (int i=0; i<nums.length; i++) {
            if (i == 0) {
                candidate = nums[i];
                count++;
                continue;
            }

            if (candidate == nums[i]) {
                count ++;
            } else{
                count --;
                if (count <= 0) {
                    candidate = nums[i];
                    count=1;
                }
            }
        }

        return candidate;
    }

    public static void main(String[] args) {
        MajorityElement majorityElement = new MajorityElement();

        int[] nums = {1,3,1,1,4,1,1,5,1,1,6,2,2};
        int response = majorityElement.improvedMajorityElement(nums);
        System.out.println(response);
    }
}
