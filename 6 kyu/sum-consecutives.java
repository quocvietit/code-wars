/*
*	6kyu - Sum consecutives
*	https://www.codewars.com/kata/sum-consecutives/train/java
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Consecutives {
    
    public static List<Integer> sumConsecutives(List<Integer> s) {
       List<Integer> sum = new ArrayList<Integer>();
       int j = 0;
       sum.add(j,s.get(j));
       
       for(int i=1 ; i<s.size(); i++){
         if(s.get(i) == s.get(i-1)){
           sum.set(j,s.get(i)+sum.get(j));
         }else{
           j++;
           sum.add(j,s.get(i));
         }
       }
       return sum;
    }

}