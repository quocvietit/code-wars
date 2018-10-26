/*
*	7kyu - Exes and Ohs
*	https://www.codewars.com/kata/exes-and-ohs/solutions/java
*/

public class XO {
  
  public static boolean getXO (String str) {
    return (str.length()- str.replace("o","").length()-str.replace("O","").length()) == (str.length()-str.replace("x","").length()- str.replace("X","").length());
  }
}