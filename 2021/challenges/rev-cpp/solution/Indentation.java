import java.util.Scanner;

public class Indentation {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int level = 0;
    while (sc.hasNextLine()) {
      String line = sc.nextLine();

      if (line.startsWith("#else") || line.startsWith("#endif")) {
        --level;
      }

      System.out.println(String.format("%s%s", " ".repeat(level * 2), line));

      if (line.startsWith("#if") || line.startsWith("#else")) {
        ++level;
      }
    }

    sc.close();
  }
}
