import java.util.ArrayList;

public class Main {
    public static void main(String[] args){
        System.out.println(isPalindrome(121));
    }

    public static boolean isPalindrome(int x) {
        class Solution {
            public boolean isPalindrome(int x) {
                // string으로 변환을 안한다면? -> 수식만으로 뒤집기
                if (x < 0) {
                    return false;
                }

                int reversed = 0;
                int temp = x;

                while(temp > 0) {
                    int digit = temp % 10;
                    reversed = reversed * 10 + digit;
                    temp /= 10;
                }

                return (reversed == x);


                // String[] strX = Integer.toString(x).split("");

                // for (int i = 0; i < strX.length/2; i++) {
                //     if (!strX[i].equals(strX[strX.length-1-i])) {
                //         return false;
                //     }
                // }

                // return true;
            }
        }
    }
}
