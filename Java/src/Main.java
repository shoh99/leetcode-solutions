public class Main {

    public static Boolean isPalindrome(String s) {

        String clean = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int l = clean.length()-1;
        int r = 0;

        while(l > r) {
            char currentLeft = clean.charAt(l);
            char currentRight = clean.charAt(r);

            if(currentLeft != currentRight) {
                System.out.println("Not Palindrome");
                return false;
            }

            l -= 1;
            r += 1;
        }
        System.out.println("Palindrome");
        return true;
    }
    public static void main(String[] args) {

        isPalindrome("A man, a plan, a canal: Panama");
    }



}