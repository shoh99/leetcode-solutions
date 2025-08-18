package ArraysAndHashes;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DesignHashMap {
    public List<List<List<Integer>>> buckets = new ArrayList<>();
    public DesignHashMap() {
        for (int i=0; i<1000; i++) {
            buckets.add(new ArrayList<>());
        }
    }

    public void put(int key, int value) {
        Integer hashKey = hash(key);
        List<List<Integer>> bucket = buckets.get(hashKey);

        for (int i=0; i < bucket.size(); i ++) {
            List<Integer> currentBucket = bucket.get(i);
            if (currentBucket.get(0) == key) {
                currentBucket.remove(1);
                currentBucket.add(1, value);
                return;
            }
        }
        List<Integer> newBucket = new ArrayList<>();
        newBucket.add(key);
        newBucket.add(value);
        bucket.add(newBucket);
    }

    public int get(int key) {
        Integer hashKey = hash(key);
        List<List<Integer>> bucket = buckets.get(hashKey);

        for (List<Integer> currentBucket:  bucket) {
            if (currentBucket.get(0) == key) {
                return currentBucket.get(1);
            }
        }
        return -1;
    }

    public void remove(int key) {
        Integer hashKey = hash(key);
        List<List<Integer>> bucket = buckets.get(hashKey);

        for (int i=0; i<bucket.size(); i++) {
            List<Integer> currentBucket = bucket.get(i);
            if (currentBucket.get(0) == key) {
                bucket.remove(i);
                return;
            }
        }
    }

    private Integer hash(int key) {
        return key % 1000;
    }

    public static void main(String[] args) {
        DesignHashMap designHashMap = new DesignHashMap();
        designHashMap.put(1,1);
        System.out.println(designHashMap.get(1));
        designHashMap.remove(1);
        System.out.println(designHashMap.get(1));
        designHashMap.put(2,1);
        designHashMap.put(2, 3);
        System.out.println(designHashMap.get(2));
    }

}
