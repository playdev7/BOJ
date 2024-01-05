import java.util.Scanner;
/**
 * solver: playdev7
 * profile: https://solved.ac/profile/playdev7
 * problem: 1427: 소트인사이드
 * summary: 숫자로 된 문자열이 입력되면 순열로서 내림차순 정렬하여 출력
 * */
public class Main {
	// 버블정렬 구현
	static void bubbleSort(char[] arr) {
		for (int i=0; i<arr.length-1; i++) {
			for (int j=0; j<arr.length-1; j++) {
				if (Character.getNumericValue(arr[j]) < Character.getNumericValue(arr[j+1])) {
					char temp = arr[j+1];
					arr[j+1] = arr[j];
					arr[j] = temp;
				}
			}
		}
	}
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		char n[] = sc.nextLine().trim().toCharArray();
		bubbleSort(n);
		System.out.print(n);
	}
}