package d1;

import java.util.Scanner;

public class Q2070 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int arr[] = new int[2];
		
		for (int i=0; i<N; i++) {
			String result = new String();
			for (int j = 0; j <arr.length; j++) {
				arr[j] = sc.nextInt();
				}
			if ( arr[0] > arr[1]) {
				result = ">";
			}else if ( arr[0] == arr[1]) {
				result = "=";
			}else {
				result = "<";
			}
			System.out.println("#"+(i+1)+" "+result);
		}
	}
}
