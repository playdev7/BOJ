import java.util.Scanner;
/**
    * https://solved.ac/profile/playdev7
    * 1236 - 성지키기
*/
public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		String inp[] = sc.nextLine().split(" ");
		
		int res1 = 0;
		int res2 = 0;
		
		// 세로가 n, 가로가 m
		int n = Integer.parseInt(inp[0]);
		int m = Integer.parseInt(inp[1]);
		
		char castle[][] = new char[n][m];
		
		for (int i=0; i < n; i++) {
			String row = sc.nextLine();
			castle[i] = row.toCharArray();
		}
		
		// X가 존재하지 않는 행의 개수 탐색
		for (int i=0; i<n; i++) {
			boolean isNone = true;
			for (int j=0; j<m; j++) {
				if (castle[i][j] == 88) {
					isNone = false;
					break;
				}
			}
			if (isNone==true) {
				res1 += 1;
			}
		}
		
		// X가 존재하지 않는 열의 개수 탐색 
		for (int i=0; i<m; i++) {
			boolean isNone = true;
			for (int j=0; j<n; j++) {
				if (castle[j][i] == 88) {
					isNone = false;
					break;
				}
			}
			if (isNone==true) {
				res2 += 1;
			}
		}
			
		// 최대값 출
		if (res1 >= res2) {
			System.out.println(res1);
		}
		else {
			System.out.println(res2);
		}

	}
}