/*
*	8kyu - Reversed Strings
*	https://www.codewars.com/kata/reversed-strings/solutions/java
*/

public class Kata {

  public static String solution(String str) {
    return new StringBuffer(str).reverse().toString();
  }

}
