import turingarena as ta 
import random
import tempfile 
import bisect

W = None
MAX_ANTS = None
ns = None
xs = None
merged = None
solution = None

random_name = None
random_ant = None

goal = None

def build_enviroment (width, max_ants):
	global W, MAX_ANTS, ns, xs, names, merged, random_name, random_ant
	W = width
	MAX_ANTS = max_ants
	ns = [0, 0]
	xs = [[], []]
	names = [[], []]
	merged = []
	random_ant = None
	
	x = random.randint (0, W/MAX_ANTS/2//2)
	while ns[0]+ns[1]<MAX_ANTS and x<W//2:
		r = random.random()
		d = 0 if r<0.5 else 1
		xs[d].append(x*2)
		x += max(int(W/MAX_ANTS/2 + (r*2-1)*W/MAX_ANTS/2/2), 1)
		if r<1/MAX_ANTS or ((ns[0]+ns[1]>=MAX_ANTS-1 or x>=W//2) and random_ant == None): random_ant = [len(merged), ns[0], ns[1], ns[d]*2+1+d]
		
		ns[d] += 1
		names[d].append(ns[d]*2-1+d)
		merged.append(ns[d]*2-1+d)
		

def process_solution ():
	global solution
	solution = dict()		# name: [time, border, guessed]
	for i in range(ns[1]):
		solution[merged[-i-1]] = [W-xs[1][-i-1], 1, False]
	for i in range(ns[0]):
		solution[merged[i]] = [xs[0][i]+1, 0, False]
		
def ant_solution ():
	print (xs, random_ant)
	global solution
	solution = dict()
	side = 1-random_ant[3]%2
	lastPos = xs[1-random_ant[3]%2][random_ant[2-random_ant[3]%2]]
	while True:
		random_ant[2-side] += side*2-1
		if not 0<=random_ant[1]<ns[0] or not 0<=random_ant[2]<ns[1]: break
		newPos = xs[1-side][random_ant[2-side]]
		solution[abs(lastPos-newPos)//2] = [merged[random_ant[0]+side*2-1], (lastPos+newPos)//2, False]			# time: [name, position, guessed]
		lastPos = newPos
		side = 1-side
	print (solution)
	
#simulate_process callback
def fall_off (time, border, name):
	if solution.get(name, None) == None or solution[name][0] != time or solution[name][1] != border:
		ta.goals.setdefault(goal, False)
		return False
	solution[name][2] = True
	return True
	
def bounch (name, time, pos):
	if solution.get(name, None) == None or solution[name][0] != time or solution[name][1] != pos:
		ta.goals.setdefaut(goal, False)
		return False
	solution[name][2] = True
	return True 

def run (before, script, w, max_ants, g, interface_path = None):
	global goal
	goal = g
	build_enviroment (w, max_ants)
	before ()
	try:
		with ta.run_algorithm (ta.submission.source, interface_path) as p:
			script (p)
	except ta.AlgorithmError as e:
		ta.goals[goal] = False
		print (e)
	ta.goals.setdefault(g, True)
	print(f"{g}: {ta.goals[g]}")
	
def evaluate_process (process):
	process.procedures.simulate_process(W,ns[1],ns[0],xs[1],xs[0],names[1],names[0],callbacks=[fall_off])
	for key, value in solution.items():
		if not value[2]:
			ta.goals.setdefault(goal, False)
			break
			
def evaluate_ant (process):
	process.procedures.simulate_ant(W,ns[1],ns[0],xs[1],xs[0],names[1],names[0],callbacks=[bounch])
	for key, value in solution.items():
		if not value[2]:
			ta.goals.setdefault(goal, False)
			break
	
run (process_solution, evaluate_process, 100, 10, "simulate_process_small", "interface_process.txt")
run (process_solution, evaluate_process, 100000000, 100, "simulate_process_big", "interface_process.txt")

run (ant_solution, evaluate_ant, 100, 20, "simulate_one_ant_small", "interface_ant.txt")
#run (ant_solution, evaluate_ant, 1000000, 100, "simulate_one_ant_middle", "interface_ant.txt")
#run (ant_solution, evaluate_ant, 100000000, 10000, "simulate_one_ant_big", "interface_ant.txt")

