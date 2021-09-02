// https://www.circuitbasics.com/what-is-digital-logic/

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class LogicLock {
  public static void main(String[] args) {
    for (int code = 0; code < 1 << 10; ++code) {
      int[] digits =
          String.format("%1$10s", Integer.toBinaryString(code).replace(' ', '0'))
              .chars()
              .map(ch -> ch - '0')
              .toArray();
      boolean[] inputs = new boolean[digits.length];
      for (int i = 0; i < inputs.length; ++i) {
        inputs[i] = digits[i] == 1;
      }

      if (check(inputs)) {
        System.out.println(
            String.format(
                "CTF{%s}",
                IntStream.range(0, inputs.length)
                    .filter(i -> inputs[i])
                    .mapToObj(i -> String.valueOf((char) (i + 'A')))
                    .collect(Collectors.joining())));
      }
    }
  }

  static boolean check(boolean[] inputs) {
    boolean ab = !(inputs[0] || !inputs[1]);
    boolean cd = !inputs[2] || inputs[3];
    boolean ef = inputs[4] || !inputs[5];
    boolean cdef = !(cd || ef);
    boolean abcdef = ab && cdef;
    boolean gh = !(inputs[6] || inputs[7]);
    boolean hi = inputs[7] ^ inputs[8];
    boolean ghi = gh && hi;
    boolean ij = inputs[8] && inputs[9];
    boolean ghij = ghi && ij;
    boolean output = abcdef && ghij;

    return output;
  }
}
