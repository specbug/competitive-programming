import java.util.*;

class ChefNRainbowArray_CC {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int tc = sc.nextInt();
    List<Integer> defaultL = new ArrayList<Integer>(Arrays.asList(1,2,3,4,5,6,7,6,5,4,3,2,1));
      for (int t=0; t<tc; t++) {
        int n = sc.nextInt();
        int[] a = new int[n];
        int tempC = -1;
        boolean result = false;
        for (int i=0; i<n; i++) {
          a[i] = sc.nextInt();
        }
        int counter = -1, countS = 0;;
        int after = 0;
        List<Integer> set = new ArrayList<Integer>();
        List<Integer> set1 = new ArrayList<Integer>();
        List<Integer> left = new ArrayList<Integer>();
        List<Integer> right = new ArrayList<Integer>();

        for (int j : a) {
            counter++;
          if (j <=7 && !set.contains(j)) {
            set.add(j);

          }

          else if (set.contains(j) && set.contains(7) && j< 7) {

              if (!set1.contains(j)) {
                  if(j==6) {
                      after = counter;
                  }
                  set1.add(j);
              }

          }
        }

        set.addAll(set1);

        if (set.size() == 13 && set.equals(defaultL)) {
            for (int i=0; i<a.length; i++) {

            }
            for (int l=0; l<a.length; l++) {
              if (l<after) {
                  if (a[l] != 7) {
                      left.add(a[l]);
                  }
                  else {
                      countS++;
                  }

              }
              else if (l >= after) {
                right.add(a[l]);
              }
            }
        List<Integer> sleft = new ArrayList<Integer>(left);
        List<Integer> sright = new ArrayList<Integer>(right);

            Collections.sort(sleft);
            Collections.reverse(sright);

            if (left.size() == right.size() && left.equals(sleft)) {
              if (left.equals(sright)) {
                result = true;
              }
            }
        }
        if (result) {
          System.out.println("yes");
        }
        else {
          System.out.println("no");
        }
       }
  }
}
