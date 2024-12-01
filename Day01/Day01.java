import java.util.ArrayList;
import java.util.Scanner;
import java.util.HashMap;

public class Day01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean part1mode = false; // true = Part 1; false = Part 2

        // parse input
        ArrayList<Integer> l = new ArrayList<Integer>();
        ArrayList<Integer> r = new ArrayList<Integer>();
        String s = "";
        String[] numbers;
        while(sc.hasNext()) {
            s = sc.nextLine().trim().replaceAll(" +", " ");
            numbers = s.split(" ");
            l.add(Integer.parseInt(numbers[0]));
            r.add(Integer.parseInt(numbers[1]));
        }

        if(part1mode) {
            // PART 1
            long sum = 0;
            l.sort(null);
            r.sort(null);
            for(int i = 0; i < l.size(); i++) {
                sum += Math.abs(l.get(i) - r.get(i));
            }
            System.out.println(sum);
        } else {
            // PART 2
            long sum = 0;
            HashMap<Integer, Integer> counts = new HashMap<Integer, Integer>();
            for(Integer i: r) {
                counts.put(i, (counts.containsKey(i) ? counts.get(i) : 0) + 1);
            }
            for(Integer i: l) {
                sum += i * (counts.containsKey(i) ? counts.get(i) : 0);
            }
            System.out.println(sum);
        }

        sc.close();
    }
}