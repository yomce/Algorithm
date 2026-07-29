package d1;

import java.util.Scanner;

public class Q2071 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int arr[] = new int[10];
		for (int i=0; i < N; i++) {
			int sum = 0;
			int avg = 0;
			for(int j = 0; j < arr.length; j++) {
				arr[j] = sc.nextInt();
				sum += arr[j];
				avg = sum / arr.length;
				if((sum%10) >=5 ) {
					++avg;
				}
				
			}
			System.out.println("#"+ (i+1) +" "+ avg);
		}
	}
}
