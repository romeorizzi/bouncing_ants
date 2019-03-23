int is_solvable(int m, int n, int is_on(int row, int col)) {
  int firstRow[n+1];
  int invFirstRow[n+1];
  for(int j=1; j<=n; j++) {
    firstRow[j] = is_on(1, j);
    invFirstRow[j] = 1-firstRow[j];
  }
  for(int i=2; i<=m; i++)
    if(is_on(i, 1) == firstRow[1]) {
      for(int j=2; j<=n; j++) {
	if(is_on(i, j) != firstRow[j])
	  return 1;
      }
    }  
    else {
      for(int j=2; j<=n; j++) {
	if(is_on(i, j) != invFirstRow[j])
	  return 1;
      }
    }
  return 0;  
}
void solve(int n, int m, int is_on(int row, int col), void switch_row(int row), void switch_col(int col)) {
  for(int j=1; j<=n; j++)
    if(is_on(1, j))
      switch_col(j);
  for(int i=2; i<=m; i++)
    if(is_on(i, 1))
      switch_row(i);
}
