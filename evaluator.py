import turingarena as ta 
import random
import tempfile 


def random_start(n_right, n_left, W):
    points = [2*i for i in range(1,W/2)]
    starts = random.choice(points,n_right + n_left)
    x_right = starts[0:n_right]
    x_left = starts[n_right:]
    name_right = [2*i for i in range(n_right)]
    name_left = [2*i+1 for i in range(n_left)]
    return (n_right,n_left,x_right,x_left,name_right,name_left)


def print_situation(n_right,n_left,x_right,x_left,name_right,name_left):
    print(n_right,n_left,x_right,x_left,name_right,name_left)


def eval_simulate(n_right,n_left,x_right,x_left,name_right,name_left):
    print(f"Checking simulate on starting situation")
    print_situation(n_right,n_left,x_right,x_left,name_right,name_left)
    
    with ta.run_algorithm(ta.submission.source) as p:
        p.procedures.is_solvable(n, m, callbacks=[is_on]))
         
    solvable = is_solvable(pirellone, n, m)
    if res == solvable:
        print("Correct!")
        return True 
    if res:
        print("You said that the pirellone was solvable, but it is not, take a look")
    else:
        print("You said that the pirellone was not solvable, but it is, take a look")

    if n <= 50:
        print_pirellone(pirellone)
    send_pirellone_file(pirellone)
    return False

def eval_solve(n, m):
    print(f"Getting solution for {n}x{m}")

    pirellone = random_pirellone(n, m, solvable=True)

    count = 0
    read = [[False for j in range(m + 1)] for i in range(n + 1)]
    def is_on(i, j):
        nonlocal count 
        if read[i][j]:
            ta.goals["solve_no_double_read"] = False
        read[i][j] = True

        count += 1
        if count > n + m - 1:
            ta.goals["solve_minimum_reads"] = False
        p.check(1 <= i <= n, "row index out of range")
        p.check(1 <= j <= m, "column index out of range")
        return pirellone[i - 1][j - 1]

    def switch_row(i):
        i -= 1
        for j in range(m):
            pirellone[i][j] = int(not pirellone[i][j])

    def switch_col(j):
        j -= 1
        for i in range(n):
            pirellone[i][j] = int(not pirellone[i][j])
 
    with ta.run_algorithm(ta.submission.source) as p:
        p.procedures.solve(n, m, callbacks=[is_on, switch_row, switch_col])

    solved = not any(any(pirellone[i][j] for j in range(m)) for i in range(n))
    if not solved:
        print("You didn't turn off all the lights. Take a look")
        if n <= 50:
            print_pirellone(pirellone)
        send_pirellone_file(pirellone)
    else:
        print("Correct!")
    return solved


def main():
    ta.goals.check("decision_exponential", lambda: eval_is_solvable(10, 10))
    ta.goals.check("decision_exponential", lambda: eval_is_solvable(10, 10, solvable=True))
    ta.goals.check("solve_exponential", lambda: eval_solve(10, 10))
    ta.goals.check("decision_exponential", lambda: eval_is_solvable(20, 20))
    ta.goals.check("decision_exponential", lambda: eval_is_solvable(20, 20, solvable=True))
    ta.goals.check("solve_exponential", lambda: eval_solve(20, 20))

    ta.goals.check("decision_quadratic", lambda: eval_is_solvable(50, 50))
    ta.goals.check("decision_quadratic", lambda: eval_is_solvable(50, 50, solvable=True))
    ta.goals.check("solve_quadratic", lambda: eval_solve(50, 50))
    ta.goals.check("decision_quadratic", lambda: eval_is_solvable(100, 100))
    ta.goals.check("decision_quadratic", lambda: eval_is_solvable(100, 100, solvable=True))
    ta.goals.check("solve_quadratic", lambda: eval_solve(100, 100))

    ta.goals.setdefault("decision_exponential", True)
    ta.goals.setdefault("solve_exponential", True)
    ta.goals.setdefault("decision_quadratic", True)
    ta.goals.setdefault("solve_quadratic", True)
    ta.goals.setdefault("solve_minimum_reads", True)
    ta.goals.setdefault("decision_no_double_read", True)
    ta.goals.setdefault("solve_no_double_read", True)

    print(ta.goals)


if __name__ == "__main__":
    main()
