import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] data = new int[n];
		for (int i = 0; i < n; i++) {
			data[i] = sc.nextInt();
		}
		int result = n-1;
		for (int i = 1; i < n - 1; i++) {
			int j = i - 1;
			int k = i + 1;
			if ((data[i] - data[j] != 0)) {
				if (data[i] - data[k] == 0) {
					result = j;
				} else {
					result = i;
				}
			}
		}
        result = result +1;
		System.out.println(result);
	}
}