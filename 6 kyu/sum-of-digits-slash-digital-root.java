/*
*	6kyu - Sum of Digits / Digital Root
*	https://www.codewars.com/kata/sum-of-digits-slash-digital-root/train/java
*/ 

public class DRoot {
  public static int digital_root(int n) {
    int sum = 0;
    while(n>0){
      sum+= n%10;
      n/=10;
      if(sum>=10)
        sum = sum%10+sum/10;
    }
    return sum;
  }
}