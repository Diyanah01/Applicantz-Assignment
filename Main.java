public class Main {

    public static String reverseWords(String str) {
        StringBuilder result = new StringBuilder();
        StringBuilder currWord = new StringBuilder();

        for (char ch : str.toCharArray()) {
            if (Character.isLetterOrDigit(ch)) {
                currWord.append(ch);
            } else {
                result.append(currWord.reverse());
                currWord.setLength(0);
                
                //if speace or punctuation
                result.append(ch); 
            }
        }
        //add last str if it does not end with punctuation
        result.append(currWord);

        return result.toString();
    }

    public static void main(String[] args) {

        //Test 1
        String testStrOne = "String; 2be reversed...";
        String expectedOne = "gnirtS; eb2 desrever...";

        //Test 2
        String testStrTw0 = "";
        String expectedTwo = "";

        //Test 3
        String testStrThree = "a b c";
        String expectedThree = "a b c";

        assert reverseWords(testStrOne).equals(expectedOne) : "Test 1 failed!";
        assert reverseWords(testStrTw0).equals(expectedTwo) : "Test 2 failed!";
        assert reverseWords(testStrThree).equals(expectedThree) : "Test 3 failed!";
        
        //System.out.println(reverseWords(testStrThree));
        System.out.println("All other tests passed!");
    }
}