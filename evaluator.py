import turingarena as ta 
import random
import tempfile 
import bisect

goals = (("simulate_process_small", 100, 10), ("simulate_process_big", 1000000, 1000))

for goal in goals:
	W = goal[1]
	MAX_ANTS = goal[2]
	

	n_right = 0
	n_left = 0
	xs = [[], []]	# [x_left, x_right]
	for x in range(W//2):
		r = random.random()
		if r > MAX_ANTS*2/W: continue
		if r < MAX_ANTS/W:
			xs[0].append(x*2)
			n_left += 1
		else:
			xs[1].append(x*2)
			n_right += 1
		if (n_left+n_right >= MAX_ANTS): break

	name_right = [i*2+2 for i in range(n_right)]
	name_left = [i*2+1 for i in range(n_left)]

	#simulate_process callback
	def fall_off (time, border, name):
		d = 1-(name%2)
		index = [0, 0]
		index[d] = (name-1)//2
		index[1-d] = bisect.bisect (xs[1-d], xs[d][index[d]])-1+d
		if (index[0]<0 or index[0]>len(xs[0])) or (index[1]<0 or index[1]>len(xs[1])):
			ta.goals.setdefault(goal[0], False)
			return False
		
		overflow = (index[0]+index[1])>(len(xs[0])-1-1+d)
		
		if border != overflow:
			ta.goals.setdefault(goal[0], False)
			return False
		if overflow == 0:
			i = index[0]+index[1]+1-d
			if time != xs[0][i]+1:
				ta.goals.setdefault(goal[0], False)
				return False
		else:
			i = index[0]+index[1]-len(xs[0])+1-d
			if time != W-xs[1][i]:
				ta.goals.setdefault(goal[0], False)
				return False
		return True
		
	#for name in name_right: fall_off (0, 0, name)
	#for name in name_left: fall_off (0, 0, name)

	try:
		with ta.run_algorithm(ta.submission.source) as process:
			process.procedures.simulate_process(W,n_right,n_left,xs[1],xs[0],name_right,name_left,callbacks=[fall_off])
	except ta.AlgorithmError as e:
		ta.goals[goal[0]] = False
		print(e)

	ta.goals.setdefault(goal[0], True)
	print(f"{goal[0]}: {ta.goals[goal[0]]}")
