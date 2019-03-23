def is_solvable(m, n, is_on):
    P = [[is_on(i, j) for j in range(1, m + 1)] for i in range(1, n + 1)]
    first = P[0]
    inv = [int(not x) for x in first]
    for line in P:
        if line != first and line != inv:
            return False

    return True


def solve(m, n, is_on, switch_row, switch_col):
    for j in range(1, n + 1):
        if is_on(1, j):
            switch_col(j)
    for i in range(2, m + 1):
        if is_on(i, 1):
            switch_row(i)
