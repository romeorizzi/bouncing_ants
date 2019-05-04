name_merged = []
		
def merge (x_right, x_left, name_right, name_left):
	x1 = 0
	x2 = 0
	for _ in range(len(x_right)+len(x_left)):
		if x2>=len(x_right) or (x1<len(x_left) and x_left[x1] < x_right[x2]):
			name_merged.append(name_left[x1])
			x1 += 1
		else:
			name_merged.append(name_right[x2])
			x2 += 1
		
		
	

def simulate_process (W, n_right, n_left, x_right, x_left, name_right, name_left, report_a_fall_off):
	merge (x_right, x_left, name_right, name_left)
	
	for i in range(n_right):
		if not report_a_fall_off (W-x_right[-i-1], 1, name_merged[-i-1]): return
	for i in range(n_left):
		if not report_a_fall_off (x_left[i]+1, 0, name_merged[i]): return
