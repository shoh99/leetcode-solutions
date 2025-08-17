package ArraysAndHashes;

import java.util.ArrayList;
import java.util.List;

public class DesignHashSet {

    static class MyHashSet {
        public List<List<Integer>> buckets = new ArrayList<>();

        public MyHashSet() {
            for (int i=0; i<1000; i++) {
                List<Integer> bucket = new ArrayList<>();
                buckets.add(bucket);
            }
        }

        public void add(int key) {
            if(!contains(key)) {
                int hashKey = key % 1000;
                List<Integer> bucket =  buckets.get(hashKey);
                bucket.add(key);
            }
        }

        public void remove(int key) {
            if (contains(key)) {
                int hashKey = key % 1000;
                List<Integer> bucket = buckets.get(hashKey);
                bucket.remove((Integer) key);
            }
        }

        public boolean contains(int key) {
            int hashKey = key % 1000;
            List<Integer> bucket = buckets.get(hashKey);

            for (Integer value: bucket) {
                if(value == key) {
                    return true;
                }
            }

            return false;
        }

    }

    public static void main(String[] args) {
        MyHashSet myHashSet = new MyHashSet();

        myHashSet.add(1);
        myHashSet.add(2);
        System.out.println(myHashSet.contains(1));
        System.out.println(myHashSet.contains(3));
        myHashSet.add(2);
        System.out.println(myHashSet.contains(2));
        myHashSet.remove(2);
        System.out.println(myHashSet.contains(2));
    }
}
