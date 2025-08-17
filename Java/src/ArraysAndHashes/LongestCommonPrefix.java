package ArraysAndHashes;

public class LongestCommonPrefix {

    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        } else if (strs.length == 1) {
            return strs[0];
        }

        StringBuilder prefix = new StringBuilder(strs[0]);

        for (int i=1; i<strs.length; i++) {
            String currentWord = strs[i];

            while(!currentWord.startsWith(prefix.toString())) {
                prefix.deleteCharAt(prefix.length()-1);

                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }

        return prefix.toString();
    }

    public static void main(String[] args) {
        LongestCommonPrefix problem = new LongestCommonPrefix();
        String[] strs = {"a"};
        String response = problem.longestCommonPrefix(strs);

        System.out.println(response);
    }
}
