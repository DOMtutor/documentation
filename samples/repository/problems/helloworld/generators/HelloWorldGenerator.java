import java.util.Random;
import java.util.Scanner;


public class HelloWorldGenerator {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		Random r = new Random(sc.nextLong());
		int length = sc.nextInt();
		System.out.println(t);
		for (int i = 0; i < t; i++) {
			for (int j = 0; j < length; j++) {
				System.out.print((char) ((int) 'a' + r.nextInt(26)));
			}
			System.out.println();
		}
		sc.close();
	}

}
