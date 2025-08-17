package ArraysAndHashes;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ConcatenationOfArray {

    public int[] getConcatenation(int[] nums) {
        return IntStream.concat(Arrays.stream(nums), Arrays.stream(nums)).toArray();
    }
 }
