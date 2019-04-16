import bisect

def calc_fall (name, xs, W, report):
	d = 1-(name%2)
	index = [0, 0]
	index[d] = (name-1)//2
	index[1-d] = bisect.bisect (xs[1-d], xs[d][index[d]])-1+d
	
	overflow = (index[d]+index[1-d])>(len(xs[0])-1-1+d)
	
	if overflow == 0:
		i = index[d]+index[1-d]+1-d
		return report (xs[0][i]+1, int(overflow), name)
	else:
		i = index[0]+index[1]-len(xs[0])+1-d
		return report (W-xs[1][i], int(overflow), name)

def simulate_process (W, n_right, n_left, x_right, x_left, name_right, name_left, report_a_fall_off):
	for i in range(n_left):
		if not calc_fall (name_left[i], (x_left, x_right), W, report_a_fall_off): return
	for i in range(n_right):
		if not calc_fall (name_right[i], (x_left, x_right), W, report_a_fall_off): return
		
