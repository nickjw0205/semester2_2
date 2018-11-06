package Chap1;

import java.util.Scanner;

public class Find_Max {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("세 정수를 입력해주세요.");
		System.out.print("a를 입력해주세요: "); int a = scan.nextInt();
		System.out.print("b를 입력해주세요: "); int b = scan.nextInt();
		System.out.print("c를 입력해주세요: "); int c = scan.nextInt();
		
		int max = a;
		if(max < b) {
			if(max < c) {
				max = c;
			}
			
			else {
				System.out.println("else_max = " + max);
				max = b;
			}
			
		}
		System.out.println("max = " + max);

	}

}
