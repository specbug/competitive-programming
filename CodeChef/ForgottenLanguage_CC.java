import java.util.*;

class ForgottenLanguage_CC {

  static String isContained(String s, List<String> dict) {
    for (String i : dict) {
      if (i.equals(s)) {
        return "YES";
      }
    }
    return "NO";
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    for (int tc=0; tc<t; tc++) {
      int n = sc.nextInt();
      int k = sc.nextInt();
      String[] dict = new String[n];
      for(int i=0; i<n; i++) {
        dict[i] = sc.next();
      }
      List<String> phrases = new ArrayList<String>();
      List<String> result = new ArrayList<String>();
      for (int f=0; f<k; f++) {
        int l = sc.nextInt();
        for (int j=0; j<l; j++) {
          phrases.add(sc.next());
        }
      }
      for (int k1=0; k1<n; k1++) {
        result.add(isContained(dict[k1], phrases));
      }
      for (String r : result) {
        System.out.print(r + " ");
      }
      System.out.println();
    }
  }
}
