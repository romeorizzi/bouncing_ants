class Solution extends Skeleton {

    int is_solvable(int m, int n, Is_solvableCallbacks cb) {
        int[] first = new int[n + 1];
        int[] inv = new int[n + 1];
        
        for (int j = 1; j <= n; j++) {
            first[j] = cb.is_on(1, j);
            inv[j] = first[j] == 1 ? 0 : 1;
        }

        for (int i = 2; i <= m; i++) {
            if (cb.is_on(i, 1) == first[1]) {
                for (int j = 2; j <= n; j++) {
	                if (cb.is_on(i, j) != first[j])
	                    return 0;
                }
            } else {
                for (int j = 2; j <= n; j++) {
	                if (cb.is_on(i, j) != inv[j])
	                    return 0;
                }
            }
        }
        return 1;
    }
    
    void solve(int n, int m, SolveCallbacks cb) {
        for (int j = 1; j <= n; j++)
            if (cb.is_on(1, j) == 1)
                cb.switch_col(j);
        for(int i = 2; i <= m; i++)
            if(cb.is_on(i, 1) == 1)
                cb.switch_row(i);
    }
}
