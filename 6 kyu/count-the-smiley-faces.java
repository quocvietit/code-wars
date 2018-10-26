/*
*	6kyu - Count the smiley faces!
*	https://www.codewars.com/kata/count-the-smiley-faces/train/java
*/

import java.util.*;

public class SmileFaces {
  
  public static int countSmileys(List<String> arr) {
      int res = 0;
      for(String str: arr)
        if((str.charAt(0) == ':' || str.charAt(0)==';') 
            && (str.charAt(1) == '-' || str.charAt(1)=='~')
            && (str.charAt(2) == ')' || str.charAt(2)=='D')
            && str.length() == 3 
            ||
            (str.charAt(0) == ':' || str.charAt(0)==';') 
            && (str.charAt(1) == ')' || str.charAt(1)=='D')
            && str.length() == 2)
          res++;
      return res;
  }
}