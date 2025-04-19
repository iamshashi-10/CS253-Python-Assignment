# Importing the statistics module to use built-in functions like mean, median, etc.
import statistics

# This function takes a list of temperatures to analyze it
def analyze_temperatures(temperatures):
    n = len(temperatures)  # length of the list
    
    # If the list is empty, we can't do any analysis
    if n == 0:
        print("No temperature data provided.")  # Show a message to the user
        return None  # Return nothing

    # Calculating the mean (average temperature)
    mean = statistics.mean(temperatures)

    # Calculating the median (middle value after sorting)
    median = statistics.median(temperatures)

    # If we have more than one value, we can calculate standard deviation and variance
    if n > 1:
        stdev = statistics.stdev(temperatures)  # This automatically uses Bessel's correction
        variance = statistics.variance(temperatures)  # This is sample variance (unbiased)
    else:
        # If there's only one value, there's no variation, so both are 0
        # this is a special case
        stdev = 0.0
        variance = 0.0

    # Displaying all the results nicely
    print(f"Mean Temperature: {mean}")
    print(f"Median Temperature: {median}")
    print(f"Standard Deviation: {stdev}")
    print(f"Sample Variance: {variance}")
    

# taking input from user
temps = []  # Empty list to store the temperatures

print("Enter temperatures one by one (type 'done' to finish):")
while True:
    user_input = input()  # Take input from the user
    if user_input.lower() == 'done':  # If the user types "done", stop the loop
        break
    try:
        temp = float(user_input)  # Try to convert the input to a float
        temps.append(temp)  # If successful, add it to the list
    except ValueError:
        # If the input isn't a number, show an error message
        print("Invalid input. Please enter a valid number or 'done' to finish.")

# Call the function to analyze the temperatures we collected
analyze_temperatures(temps)
