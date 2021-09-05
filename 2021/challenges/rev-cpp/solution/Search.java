import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Search {
  static final String FILE_NAME = "cpp.c";
  static final String[] ALPHABET = {
    "CHAR_a",
    "CHAR_b",
    "CHAR_c",
    "CHAR_d",
    "CHAR_e",
    "CHAR_f",
    "CHAR_g",
    "CHAR_h",
    "CHAR_i",
    "CHAR_j",
    "CHAR_k",
    "CHAR_l",
    "CHAR_m",
    "CHAR_n",
    "CHAR_o",
    "CHAR_p",
    "CHAR_q",
    "CHAR_r",
    "CHAR_s",
    "CHAR_t",
    "CHAR_u",
    "CHAR_v",
    "CHAR_w",
    "CHAR_x",
    "CHAR_y",
    "CHAR_z",
    "CHAR_A",
    "CHAR_B",
    "CHAR_C",
    "CHAR_D",
    "CHAR_E",
    "CHAR_F",
    "CHAR_G",
    "CHAR_H",
    "CHAR_I",
    "CHAR_J",
    "CHAR_K",
    "CHAR_L",
    "CHAR_M",
    "CHAR_N",
    "CHAR_O",
    "CHAR_P",
    "CHAR_Q",
    "CHAR_R",
    "CHAR_S",
    "CHAR_T",
    "CHAR_U",
    "CHAR_V",
    "CHAR_W",
    "CHAR_X",
    "CHAR_Y",
    "CHAR_Z",
    "CHAR_0",
    "CHAR_1",
    "CHAR_2",
    "CHAR_3",
    "CHAR_4",
    "CHAR_5",
    "CHAR_6",
    "CHAR_7",
    "CHAR_8",
    "CHAR_9",
    "CHAR_LBRACE",
    "CHAR_RBRACE",
    "CHAR_UNDERSCORE"
  };
  static final String PREFIX = "  #define FLAG_26 ";

  public static void main(String[] args) throws Throwable {
    for (String ch : ALPHABET) {
      modifyFile(ch);

      if (!execCmd().contains("INVALID_FLAG")) {
        System.out.println(String.format("Found %s!", ch));

        break;
      }
    }
  }

  static void modifyFile(String ch) throws Throwable {
    Scanner sc = new Scanner(new File(FILE_NAME));

    StringBuilder content = new StringBuilder();
    while (sc.hasNextLine()) {
      String line = sc.nextLine();
      if (line.startsWith(PREFIX)) {
        line = String.format("%s%s", PREFIX, ch);
      }

      content.append(line).append("\n");
    }

    BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME));
    writer.write(content.toString());

    writer.close();
  }

  static String execCmd() throws Throwable {
    ProcessBuilder builder =
        new ProcessBuilder("gcc", "-Wfatal-errors", "cpp.c").directory(new File("."));
    builder.redirectErrorStream(true);
    Process process = builder.start();
    InputStream is = process.getInputStream();
    BufferedReader reader = new BufferedReader(new InputStreamReader(is));

    StringBuilder result = new StringBuilder();
    String line = null;
    while ((line = reader.readLine()) != null) {
      result.append(line).append("\n");
    }

    return result.toString();
  }
}
