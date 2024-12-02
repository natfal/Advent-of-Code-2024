import java.util.ArrayList;
import java.util.Scanner;

public class Day02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean part1mode = false; // true = Part 1; false = Part 2
        int result = 0;

        // parse input
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        String[] inputLine;
        boolean currentLineResult;
        while(sc.hasNext()) {
            inputLine = sc.nextLine().split(" ");
            for(String s: inputLine) {
                numbers.add(Integer.parseInt(s));
            }
            currentLineResult = checkList(numbers, 0, 1, 2, part1mode);
            if (currentLineResult) result++;

            numbers.clear();
        }
        System.out.println(result);
        sc.close();
    }

    public static boolean checkList(ArrayList<Integer> l, int ind1, int ind2, int ind3, boolean numberRemoved) {

        if(ind3 >= l.size()) return true;

        boolean checkPairs = checkPairs(l, ind1, ind2, ind3);

        if(numberRemoved && !checkPairs) return false;

        // the 3 steps are ok
        if(checkPairs) return checkList(l, ind1 + 1, ind2 + 1, ind3 + 1, numberRemoved);

        // prepare arraylist copies to remove one of the steps
        ArrayList<Integer> lCopy1 = new ArrayList<Integer>();
        ArrayList<Integer> lCopy2 = new ArrayList<Integer>();
        ArrayList<Integer> lCopy3 = new ArrayList<Integer>();

        for (Integer i: l) { lCopy1.add(i); lCopy2.add(i); lCopy3.add(i); }

        lCopy1.remove(ind1); lCopy2.remove(ind2); lCopy3.remove(ind3); 

        // removefirst, second, or third step
        return checkList(lCopy1, ind1, ind2, ind3, true)
            || checkList(lCopy2, ind1, ind2, ind3, true)
            || checkList(lCopy3, ind1, ind2, ind3, true);
    }

    public static boolean checkPairs(ArrayList<Integer> l, int ind1, int ind2, int ind3) {
        int lowerIntervalCheck = checkInterval(l.get(ind1), l.get(ind2));
        int higherIntervalCheck = checkInterval(l.get(ind2), l.get(ind3));
        return lowerIntervalCheck != 0 && lowerIntervalCheck == higherIntervalCheck; 
    }

    public static int checkInterval(int a, int b) {
        // between 1 and 3 (inclusive)
        int rawDiff = b - a;
        int difference = Math.abs(rawDiff);
        return (difference >=1 && difference <= 3) ? rawDiff / difference : 0; 
        // 0 = interval doesn't pass
        // 1 = ascending
        // -1 = descending
    }
}