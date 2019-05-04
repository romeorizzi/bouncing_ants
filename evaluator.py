import turingarena as ta 
import random
import tempfile 
import bisect

goals = (("simulate_process_small", 100, 10), ("simulate_process_big", 100000000, 100))

for goal in goals:
	W = goal[1]
	MAX_ANTS = goal[2]
	
	ns = [0, 0]			# [n_left, n_right]
	xs = [[], []]		# [x_left, x_right]
	names = [[], []]	# [name_left, name_right]
	merged = []
	x = random.randint (0, W/MAX_ANTS/2)
	while ns[0]+ns[1]<MAX_ANTS and x<W:
		r = random.random()
		d = 0 if r<0.5 else 1
		xs[d].append(x)
		ns[d] += 1
		names[d].append(ns[d]*2-1+d)
		merged.append(ns[d]*2-1+d)
		x += int(W/MAX_ANTS + (r*2-1)*W/MAX_ANTS/2)
	
	solution = dict()		# name: [time, border, guessed]
	
	for i in range(ns[1]):
		solution[merged[-i-1]] = [W-xs[1][-i-1], 1, False]
	for i in range(ns[0]):
		solution[merged[i]] = [xs[0][i]+1, 0, False]

	#simulate_process callback
	def fall_off (time, border, name):
		if solution.get(name, None) == None or solution[name][0] != time or solution[name][1] != border:
			ta.goals.setdefault(goal[0], False)
			return False
		solution[name][2] = True
		return True

	try:
		with ta.run_algorithm(ta.submission.source) as process:
			process.procedures.simulate_process(W,ns[1],ns[0],xs[1],xs[0],names[1],names[0],callbacks=[fall_off])
			for key, value in solution.items():
				if not value[2]:
					ta.goals.setdefault(goal[0], False)
					break
		print (f"time usage: {process.time_usage*10**9}")
	except ta.AlgorithmError as e:
		ta.goals[goal[0]] = False
		print(e)

	ta.goals.setdefault(goal[0], True)
	print(f"{goal[0]}: {ta.goals[goal[0]]}")
