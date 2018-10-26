/*
*	7kyu - Breaking chocolate problem
*	https://www.codewars.com/kata/breaking-chocolate-problem/solutions/java
*/

public class Chocolate{
  public static int breakChocolate(int n, int m) {
    return n*m-1>0?n*m-1:0;
  }
}