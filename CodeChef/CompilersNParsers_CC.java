import java.util.*;

class CompilersNParsers_CC {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    for (int tc=0;tc<t;tc++) {
      Stack<String> stack = new Stack<String>();
      String s = null;
      int result = 0, counter = 0;
      s = (sc.next());
      for (int i=0; i<s.length(); i++) {
        if (s.charAt(i) == '<') {
          counter++;
        }
        else if (s.charAt(i) == '>') {
            counter--;
        }
        if (counter == 0) {
          result = i+1;
        }
        if (counter < 0) {
          break;
        }
        }
        System.out.println(result);
      }

    }
  }
