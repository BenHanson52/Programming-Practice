# PA1 Matrix Calculator
# Starter file - students implement functionality here
import numpy as np

def main():
    op_choice = menu_choice()
    if op_choice == 4:
        print("You chose to exit the program. Goodbye.")
        return 0 #this jumps down to the "if__name__... block and provides a clean exit code
    dims = dimension_select() #grabbing rows and columns from dimension_select() func
    matrix_1 = matrix_build(dims)
    matrix1_np=np.array(matrix_1)
    if op_choice in range(1,3): #add and sub operation requirements are similar, so this check handles both
        matrix_2 = matrix_build(dims) #a second matrix is required for add/sub
        matrix2_np = np.array(matrix_2)
        computed_matrix = add_sub_matrices(matrix_1, matrix_2, op_choice)
        if op_choice == 1: #this check only applies to numpy
            np_sum_matrix = np.add(matrix1_np, matrix2_np) #wow, numpy sure makes this easier
            print("The NumPy computed matrix is: ")
            for row in np_sum_matrix: #surprised numpy doesnt offer a one line, bracketless, print stmt
                print(*row) #using the unpacking operator to print the matrix in the cleanest format
        if op_choice == 2: #this check is only for numpy
            np_sub_matrix = np.subtract(matrix1_np, matrix2_np)
            print("The NumPy computed matrix is: ")
            for row in np_sub_matrix:
                print(*row) #using the unpacking operator to print the matrix in the cleanest format
        print("The custom computed matrix is: ") #this data comes from my custom implementation
        for row in computed_matrix:
            print(*row) #using the unpacking operator to print the matrix in the cleanest format
        return 0 #clean exit
    else:
        custom_computed_matrix, scalar = scal_matrix(matrix_1) #returning the custom matrix as well as the scalar so numpy can use the scalar
        np_scalar_matrix = np.array(matrix_1) #converting matrix_1 (pre-custom compute) to a numpy matrix
        np_computed_scalar_matrix = np.multiply(np_scalar_matrix, scalar) #numpy operation
        print("The NumPy computed matrix is: ")
        for row in np_computed_scalar_matrix:
            print(*row) #numpy print
        print("The custom computed matrix is: ")
        for row in custom_computed_matrix:
            print(*row) #custom print
        return 0 #clean exit

def menu_choice():
    print("Matrix Calculator")
    valid_choice = False
    while not valid_choice: #loop runs until valid input is given
        op_choice = (input(" 1 - Addition" \
        "\n 2 - Subtraction \n 3 - Scalar Multiplication \n 4 - Exit program \n Choose an option:"))
        try: #this seemed like the best 'coverage' for wacky input
            op_choice = int(op_choice)
        except ValueError:
            print("You must enter an integer between 1 and 4.")
            continue
        if op_choice not in range(1, 5): #checking the int is valid after confirming it's an int
            print("You must enter an integer between 1 and 4.")
        else:
            valid_choice = True
            return op_choice #returns menu selection and exits menu_choice()

def dimension_select():
    invalid_input = True
    while invalid_input:
        #normally id prompt for these separately, but i wanted to better match the expected output denoted in github
        rows_and_cols = input("Choose a number of rows and columns, must be two positive, space-separated integers: ").strip()
        indiv_vals = rows_and_cols.split()
        if len(indiv_vals) != 2: #verifying proper amount of numbers were entered
            print("Enter exactly two space-separated integers.")
            continue
        rows, cols = indiv_vals #splitting indiv_vals back into row and column values
        try: #verifying rows/cols are ints
            rows = int(rows)
            cols = int(cols)
        except ValueError:
            print("You must enter a positive integer for both rows and columns.")
            continue
        if rows <= 0 or cols <= 0: #chosen rows and cols cant be less than or equal to 0
            print("Invalid input; you must enter positive integers. Try again.")
        else:
            invalid_input = False #end loop if valid matrix dimensions given
    return rows, cols

def matrix_build(dims):
    matrix=[]
    rows, cols = dims #unpacking rows/cols from the dims variable, had to return each simultaneously in prev func.
    #I really liked this one-liner, but it doesnt validate: matrix=[[float(input(f"Enter the elements of a {rows}x{cols} matrix at position [{c+1}, {r+1}]: ")) for r in range(rows)] for c in range(cols)]
    for r in range(rows):
        row = []
        for c in range(cols):
            while True:
                inp_element = input(f"Enter element at ({r+1}, {c+1}): ")
                try:
                    val = float(inp_element)        
                    break #I've been told break stmts are bad practice, but I couldn't determine a good way to validate without one.                
                except ValueError: #verifying the input is a real number
                    print("Invalid. Enter a real number.")
            row.append(val)
        matrix.append(row)
    return matrix
                
def add_sub_matrices(matrix_1, matrix_2, op_choice):
    for i_row in matrix_1: 
        print(*i_row)
    print(f"{'+' if op_choice ==1 else '-'}") #reminding user of their selection.
    for j_row in matrix_2:
        print(*j_row)
    if op_choice == 1: #addition, [0] is rows, cols are implicitly covered by checking length per row
        sum_matrix = [[matrix_1[r][c] + matrix_2[r][c] for c in range(len(matrix_1[0]))]
                      for r in range(len(matrix_1))]
        return sum_matrix
    else:
        sub_matrix = [[matrix_1[r][c] - matrix_2[r][c] for c in range(len(matrix_1[0]))]
                      for r in range(len(matrix_1))]
    return sub_matrix

def scal_matrix(matrix_1):
    valid_input = False
    while not valid_input:
        scalar = input("Enter a scalar: ")
        try:
            scalar = float(scalar) #scalars are often floats, hence float
        except ValueError:
            print("You must enter a single real number.")
            continue
        valid_input = True
    #had a much easier time figuring out the line below after implementing the add/sub ops
    scal_matrix = [[matrix_1[r][c] * scalar for c in range(len(matrix_1[0]))]
                      for r in range(len(matrix_1))]
    for row in matrix_1:
        print(*row)
    print(f"* ({scalar})") #printing the scalar so the user can see the operation
    return scal_matrix, scalar #returning scalar as well so numpy can use it.


if __name__ == "__main__":
    raise SystemExit(main()) #a graceful exit upon a successful operation, or upon the user choosing 4 to exit.