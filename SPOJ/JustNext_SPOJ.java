import java.util.*;
import java.io.*;

class JustNext_SPOJ {

  public static void main(String[] args) {
    try {
      Scanner sc = new Scanner(System.in);
      int t = sc.nextInt();
      for (int tc=0; tc<t; tc++) {
          int temp = 0;
          int counter = 0;
        int n = sc.nextInt();
        List<Integer> a = new ArrayList<Integer>();
        for (int i=0; i<n; i++) {
          a.add(sc.nextInt());
        }
        List<Integer> copy = new ArrayList<Integer>(a);
        Collections.reverse(a);
        for (int j=0; j<a.size(); j++) {
          if (counter == 0 && j != a.size()-1) {
            if (a.get(j) > a.get(j+1)) {
              temp = a.get(j);
              a.set(j, a.get(j+1));
              a.set(j+1, temp) ;
              counter = 1;
              break;
            }
          }
        }
        Collections.reverse(a);
        if (copy.equals(a)) {
        	System.out.print(-1);
        }
        else {
        	for (int j=0; j<a.size(); j++) {
            System.out.print(a.get(j));
        }
        }

      System.out.println();
    }
    }
    catch (Exception e) {
      return;
    }

}
}
