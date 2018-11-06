package Chap2;

public class array {
	
	static void print_array(int a[]) {
		
		int i = 0;
		int len = a.length;
		
		for(i = 0;i < len;i++) {
			System.out.println(i + "번째 값: " + a[i]);
		}
	}

	public static void main(String[] args) {
		int[] a = new int[5];
		int b[] = new int[5];
		int c[] = new int[] {1,2,3,4,5};
		
		b = c.clone();
		a = c.clone();
		System.out.println("a의 배열 ");
		print_array(a);
		System.out.println("b의 배열 ");
		print_array(b);
		System.out.println("c의 배열 ");
		print_array(c);
	}

}
