import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        int[] comp = new int[n];
        comp[0] = -1;
        Integer[] a = new Integer[n];
        a[n - 1] = n - 1;
        comp[n - 1] = 3;
        String string="";
        for (int i = 0; i < n - 1; i++) {
            comp[i] = in.nextInt();
            string=string+String.valueOf(comp[i]);
            a[i] = i;
        }
        System.out.println(sequence(string));

    }
    public static int sequence(String S) {
        int len = S.length(), N = len + 1, mod = (int) 10e+7;
        int[][] dp = new int[N+1][N];

        for(int i = 0; i < N; i++) dp[1][i] = 1;

        for(int i = 1; i <= len; i++) {
            if(S.charAt(i-1) == '1') for(int j = N - i -1; j >= 0; j--) dp[i+1][j] = (dp[i+1][j+1] + dp[i][j+1])%mod;
            else  for(int j = 0; j <= N - i-1; j++) dp[i+1][j] = ((j > 0 ? dp[i+1][j-1] : 0) + dp[i][j])%mod;
        }

        return dp[N][0];
    }
}
