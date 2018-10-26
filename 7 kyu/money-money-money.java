/*
*	7kyu - money-money-money
*	https://www.codewars.com/kata/money-money-money/solutions/java
*/

public class Money {
  public static int calculateYears(double principal, double interest,  double tax, double desired) {
    return (int)Math.ceil(Math.log(desired/principal) / Math.log(1+interest-interest*tax));
  }
}