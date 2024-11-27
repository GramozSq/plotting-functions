import numpy as np
import matplotlib.pyplot as plt

# Basic mathematical functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return np.inf  # Return infinity if dividing by zero
    return x / y

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def sine(x):
    return np.sin(x)

def cosine(x):
    return np.cos(x)

# Function to generate values for graphing based on operation code
def generate_values(operation, x_values, y_value=0):
    if operation == 1:  # Add
        return add(x_values, y_value)
    elif operation == 2:  # Subtract
        return subtract(x_values, y_value)
    elif operation == 3:  # Multiply
        return multiply(x_values, y_value)
    elif operation == 4:  # Divide
        return divide(x_values, y_value)
    elif operation == 5:  # Square
        return square(x_values)
    elif operation == 6:  # Cube
        return cube(x_values)
    elif operation == 7:  # Sine
        return sine(x_values)
    elif operation == 8:  # Cosine
        return cosine(x_values)
    else:
        raise ValueError("Invalid operation code. Please choose a valid option.")

# Function to graph the operations
def plot_function(operation, x_range, y_value=0):
    x_values = np.linspace(x_range[0], x_range[1], 400)  # Generate x-values in range
    y_values = generate_values(operation, x_values, y_value)  # Calculate corresponding y-values
    
    # Plotting the function
    plt.plot(x_values, y_values, label=f'Operation {operation}')
    plt.title(f"Graph of Operation {operation}")
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()

# Example usage:
print("Available operations: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square (x^2)")
print("6. Cube (x^3)")
print("7. Sine (sin(x))")
print("8. Cosine (cos(x))")

# Get user input for which function to graph
operation = int(input("Enter the operation number (1 for add, 2 for subtract, 3 for multiply, 4 for divide, 5 for x^2, 6 for x^3, 7 for sin(x), 8 for cos(x)): "))
x_start = float(input("Enter the start of the x-range: "))
x_end = float(input("Enter the end of the x-range: "))
y_value = float(input("Enter a constant value (y-value or second operand for operations like add, subtract, etc.): "))

# Graph the chosen operation
plot_function(operation, (x_start, x_end), y_value)
