/*
*	6kyu - Multiples of 3 or 5
*	https://www.codewars.com/kata/multiples-of-3-or-5/train/java
*/

public class Solution {

  public int solution(int number) {
    return sum(number-1, 3) + sum(number-1, 5) - sum(number-1, 15);
  }
  
  public int sum(int number, int mult){
    int sum = number/mult;
    return (sum*(sum+1)/2)*mult;
  }
}