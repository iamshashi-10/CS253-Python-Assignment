# In my laptop, I used the command 'python3 fileName.py' in the terminal
# (replace fileName.py with your actual filename) after going into the folder where the file is saved.

# Importing all the required libraries
import numpy as np           # For handling numbers and arrays
import matplotlib.pyplot as plt  # For plotting graphs
import random                # For random selections and values
import math                  # For mathematical functions

# This function sets a seed to get the same random values every time (makes results repeatable)
def set_random_seed(seed):
    np.random.seed(seed)
    random.seed(seed)

# This function applies the selected math function to x
def apply_function(func, x):
    if func == 'sin':
        return np.sin(x)
    elif func == 'cos':
        return np.cos(x)
    elif func == 'tan':
        return np.tan(x)
    elif func == 'log':
        return np.log(x)  # only works for positive numbers
    elif func == 'square':
        return np.power(x, 2)
    elif func == 'cube':
        return np.power(x, 3)

# generates the synthetic dataset
def generate_dataset(N, x_min, x_max):
    # Generating N random values of X between x_min and x_max
    X = np.random.uniform(x_min, x_max, N)

    # Randomly choosing 3 math functions from this list
    functions = ['sin', 'cos', 'tan', 'log', 'square', 'cube']
    f1 = random.choice(functions)
    f2 = random.choice(functions)
    f3 = random.choice(functions)

    # Generating random coefficients for the formula
    A, B = random.uniform(0.5, 2), random.uniform(0.5, 2)
    C, D = random.uniform(0.5, 2), random.uniform(0.5, 2)
    E, F = random.uniform(0.5, 2), random.uniform(0.5, 2)

    # Making sure to not pass negative or zero values into log
    X_safe = np.where(X <= 0, 0.1, X)

    # Creating Y values using the formula: Y = A*f1(B*X) + C*f2(D*X) + E*f3(F*X)
    Y = A * apply_function(f1, B * X_safe) + \
        C * apply_function(f2, D * X_safe) + \
        E * apply_function(f3, F * X_safe)

    # Printing the formula used for Y generation
    print(f"Generated Function: Y = {A:.2f}*{f1}({B:.2f}*X) + {C:.2f}*{f2}({D:.2f}*X) + {E:.2f}*{f3}({F:.2f}*X)")
    
    return X, Y

# ----------- PLOTTING FUNCTIONS -----------

# Scatter plot (shows points on graph)
def plot_scatter(X, Y):
    plt.figure()
    plt.scatter(X, Y, color='blue', alpha=0.6)
    plt.title("Scatter Plot of X vs Y")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Histogram (shows distribution/frequency of X values)
def plot_histogram(X):
    plt.figure()
    plt.hist(X, bins='auto', color='orange', alpha=0.7)
    plt.title("Histogram of X")
    plt.xlabel("X values")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

# Box plot (shows how Y values are spread — median, min, max, etc.)
def plot_box(Y):
    plt.figure()
    plt.boxplot(Y, vert=True)
    plt.title("Box Plot of Y")
    plt.ylabel("Y values")
    plt.grid(True)
    plt.show()

# Line plot (shows how Y changes with X, with X sorted)
def plot_line(X, Y):
    # Sorting X and Y for a clean line graph
    sorted_indices = np.argsort(X)
    X_sorted = X[sorted_indices]
    Y_sorted = Y[sorted_indices]

    plt.figure()
    plt.plot(X_sorted, Y_sorted, color='green')
    plt.title("Line Plot of Sorted X vs Y")
    plt.xlabel("X (sorted)")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# main program
if __name__ == "__main__":
    set_random_seed(42)  # Setting seed to get the same output every time
    
    # Taking user inputs
    N = int(input("Enter number of data points (N): "))
    x_min = float(input("Enter minimum value for X: "))
    x_max = float(input("Enter maximum value for X: "))

    # Generating the dataset
    X, Y = generate_dataset(N, x_min, x_max)
    
    # Plotting all the graphs
    plot_scatter(X, Y)
    plot_histogram(X)
    plot_box(Y)
    plot_line(X, Y)
