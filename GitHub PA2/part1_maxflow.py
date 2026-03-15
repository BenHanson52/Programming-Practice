from sympy import Matrix
from sympy import pprint

def analyze_system(name, aug):
    print(f"\n=== {name} ===")
    print("Augmented matrix:")
    pprint(aug)

    rref_matrix, pivots = aug.rref()
    print("\nRREF:")
    pprint(rref_matrix) #pretty print is new to me, very helpful

    num_vars = aug.cols - 1
    pivot_vars = list(pivots)
    free_vars = [i for i in range(num_vars) if i not in pivot_vars]

    print("\nPivot columns:", pivot_vars)
    print("Free variable columns:", free_vars)
    print("Rank:", len(pivot_vars))

    # inconsistency check
    inconsistent = False
    for row in range(rref_matrix.rows):
        if all(rref_matrix[row, col] == 0 for col in range(num_vars)) and rref_matrix[row, num_vars] != 0:
            inconsistent = True
            break

    if inconsistent:
        print("Classification: inconsistent")
    elif len(pivot_vars) == num_vars:
        print("Classification: unique solution")
    else:
        print("Classification: infinitely many solutions")

part1 = Matrix([
    [1, 0, 0, 0, 0, -1, 0, 120],
    [1, -1, 0, 0, 0, 0, -1, 90],
    [0, -1, 1, 0, 0, 0, 0, 80],
    [0, 0, 1, -1, 0, 0, 0, 110],
    [0, 0, 0, -1, 1, 0, -1, 60],
    [0, 0, 0, 0, 1, -1, 0, 60]
])

analyze_system("Part 1", part1)