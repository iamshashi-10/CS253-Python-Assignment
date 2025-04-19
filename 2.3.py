# using numpy for matrix operations and solving linear equations
import numpy as np

# function to solve the equation AX = B
def solve_linear_system(A, B):
    try:
        # Using numpy's built-in function to solve the equation AX = B
        X = np.linalg.solve(A, B)  # This returns the solution vector X
        print("Solution X:")
        print(X)
        return

    except np.linalg.LinAlgError as e:
        # If A is a singular matrix (no unique solution)
        print("Error:", e)
        print("The matrix A is singular. No unique solution exists.")
        return None

# This function handles all the user input and calls the solver
def main():
    # ------- INPUT SECTION --------
    N = int(input("Enter the value of N (matrix size): "))  # User gives size of square matrix

    print("\nEnter the elements of matrix A ({}x{}):".format(N, N))
    A = []  # This will store the matrix A row by row
    for i in range(N):
        row = list(map(float, input(f"Row {i+1}: ").split()))  # Taking space-separated numbers
        if len(row) != N:
            # If the user doesn't enter exactly N numbers, restart the input
            print("Each row must have exactly", N, "elements.")
            main()  # Recursively call main() again (restarts the program)
        A.append(row)  # Add the valid row to the matrix

    print("\nEnter the elements of vector B ({} values):".format(N))
    B = []  # This will store the values for vector B
    for i in range(N):
        val = float(input(f"B[{i+1}]: "))  # One value at a time
        B.append(val)

    # ------- SOLVING SECTION -------
    solve_linear_system(A, B)  # Call the function to solve the system

# Calling the main function to start the program
main()
