package d1;

import java.util.Scanner;

public class Q2072 {
 public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int N = sc.nextInt();
	int arr[] = new int[10];
	for (int i = 0; i < N; i++) {
		int count = 0;
		for (int j = 0; j < arr.length; j++) {
			arr[j] = sc.nextInt();
			if(!(arr[j]%2 == 0)) {
				count += arr[j];
			}
			
		}System.out.println("#"+ (i+1) +" "+ count);
	}
}
}
