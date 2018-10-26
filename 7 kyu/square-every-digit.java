/*
*	7kyu - Square Every Digit
*	https://www.codewars.com/kata/square-every-digit/solutions/java
*/

public class SquareDigit {

  public int squareDigits(int n) {
    String str = "";
    while(n>0){
      int number = n%10;
      str = (number*number) + str;
      n/=10;
    }
    return Integer.parseInt(str);
  }

}