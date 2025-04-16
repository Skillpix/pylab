# Python Solutions for Educational Purposes
# Each solution will demonstrate a specific concept in a straightforward manner

# Ready for your questions! I'll implement solutions here.

# Question: Write a Python program to count the number of occurrences of a specific key value pair in a text file.
def count_key_value_occurrences(file_path, key, value):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if f"{key}: {value}" in line:
                count += 1
    return count

# Question: To develop a program that accepts an integer matrix of size R * C as input and replaces the last integer with 10. 
# The program must then print the modified matrix following specific formatting conditions. 
# Each row is separated by a comma and enclosed in parenthesis.
def modify_matrix(matrix):
    if matrix and matrix[-1]:
        matrix[-1][-1] = 10
    formatted_matrix = ', '.join(f"({', '.join(map(str, row))})" for row in matrix)
    print(formatted_matrix)

# Question: Create a custom exception invalid age error. Write a program that takes the user's age and raises this exception if the age is less than 18.
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    print("Age is valid.")

# Question: Create a basic calculator using tkinter with buttons for digits and basic operations.
# Display the result in an entry widget. Design a calculator interface with buttons for digits and operations,
# and calculate the results when the button is clicked.
import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Basic Calculator")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 1, 0
for button in buttons:
    btn = tk.Button(root, text=button, font="Arial 15", padx=20, pady=20)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

# Question: Write a Python program using the fundamental operations of plotting and visualizing data using Matplotlib. 
# The program should demonstrate how to create different types of plots, customize them, and apply various visualization techniques to effectively represent data.
import matplotlib.pyplot as plt

def demonstrate_plots():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 2, 1)
    plt.plot(x, y, label="Line Plot", color="blue", marker="o")
    plt.title("Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()

    categories = ['A', 'B', 'C', 'D']
    values = [5, 7, 3, 8]
    plt.subplot(2, 2, 2)
    plt.bar(categories, values, color="green")
    plt.title("Bar Plot")
    plt.xlabel("Categories")
    plt.ylabel("Values")

    plt.subplot(2, 2, 3)
    plt.scatter(x, y, color="red", label="Scatter Plot")
    plt.title("Scatter Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()

    plt.subplot(2, 2, 4)
    sizes = [15, 30, 45, 10]
    labels = ['A', 'B', 'C', 'D']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Pie Chart")

    plt.tight_layout()
    plt.show()

# Question: Write a Python program to get a string made of the first 2 and the last 2 characters of a given string. 
# If the string length is less than two, return the empty string instead.
def first_and_last_two_chars(s):
    if len(s) < 2:
        return ""
    return s[:2] + s[-2:]

# Question: Write a program that asks the user to enter 2 strings of the same length. 
# The program should then check to see whether the strings are of the same length. 
# If they are not, the program should print an appropriate message and exit. 
# If they are the same length, the program should alternate the characters of the two strings.
def alternate_characters():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    if len(str1) != len(str2):
        print("The strings are not of the same length. Exiting.")
        return
    result = ''.join(a + b for a, b in zip(str1, str2))
    print("Alternated string:", result)

# Question: Write a Python program to find the roots of a quadratic equation.
import math

def find_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Roots are real and distinct: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"Roots are real and equal: {root}")
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"Roots are complex: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i")

# Question: Write a program that asks the user for their name and how many times to print it. 
# The program should print out the user's name the specific number of times.
def print_name_multiple_times():
    name = input("Enter your name: ")
    count = int(input("How many times should I print your name? "))
    for _ in range(count):
        print(name)

# Question: Write a Python program using fundamental operations of mathematical computations and handling data using numpy and scipy packages in Python.
import numpy as np
from scipy import stats

def numpy_scipy_operations():
    data = np.array([1, 2, 3, 4, 5])
    print("Original Data:", data)
    print("Mean:", np.mean(data))
    print("Standard Deviation:", np.std(data))
    print("Sum:", np.sum(data))
    print("Square of each element:", np.square(data))

    data2 = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    mode = stats.mode(data2)
    print("Mode of data2:", mode.mode[0], "with count:", mode.count[0])
    print("Median of data2:", np.median(data2))
    print("Variance of data2:", np.var(data2))

# Question: The program must accept N integers as input. The value N is always a multiple of three. 
# The program must divide the given N integers into three equal parts. 
# Write a program to print the integers of the 1st part, then the integers of the last part, 
# and finally the integers in the middle part.
def divide_and_print_parts():
    n = int(input("Enter the number of integers (multiple of 3): "))
    if n % 3 != 0:
        print("The number of integers must be a multiple of 3.")
        return
    integers = list(map(int, input(f"Enter {n} integers separated by space: ").split()))
    if len(integers) != n:
        print(f"Please enter exactly {n} integers.")
        return
    part_size = n // 3
    first_part = integers[:part_size]
    middle_part = integers[part_size:2*part_size]
    last_part = integers[2*part_size:]
    print("First part:", *first_part)
    print("Last part:", *last_part)
    print("Middle part:", *middle_part)

# Question: Design a Python script using Tkinter graphics library to construct a bar chart representing the grades obtained by students. 
# Read from a file, categorizing them into distinction, 1st class, 2nd class, 3rd class, and failed.
import tkinter as tk
from tkinter import Canvas
import csv

def draw_bar_chart(file_path):
    categories = {"Distinction": 0, "1st Class": 0, "2nd Class": 0, "3rd Class": 0, "Failed": 0}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                grade = int(row[1])
                if grade >= 75:
                    categories["Distinction"] += 1
                elif grade >= 60:
                    categories["1st Class"] += 1
                elif grade >= 50:
                    categories["2nd Class"] += 1
                elif grade >= 35:
                    categories["3rd Class"] += 1
                else:
                    categories["Failed"] += 1
            except ValueError:
                continue

    root = tk.Tk()
    root.title("Bar Chart - Grades")
    canvas = Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    bar_width = 80
    spacing = 20
    x_start = 50
    max_height = 300
    max_value = max(categories.values())

    for i, (category, count) in enumerate(categories.items()):
        bar_height = (count / max_value) * max_height if max_value > 0 else 0
        x0 = x_start + i * (bar_width + spacing)
        y0 = 350 - bar_height
        x1 = x0 + bar_width
        y1 = 350
        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
        canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(count), fill="black")
        canvas.create_text((x0 + x1) / 2, 360, text=category, fill="black")

    root.mainloop()

# Question: Write a Python program to filter only even numbers from a given list without using the filter function.
def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# Question: Change all the numbers in the file to text. Construct a program for the same without external libraries.
def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 0:
        return "zero"
    elif n < 10:
        return ones[n]
    elif 10 < n < 20:
        return teens[n - 10]
    elif n % 10 == 0:
        return tens[n // 10]
    else:
        return tens[n // 10] + "-" + ones[n % 10]

def replace_numbers_with_text_no_lib(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    def replace_number(match):
        return number_to_words(int(match.group()))

    import re
    updated_content = re.sub(r'\b\d+\b', replace_number, content)

    with open(file_path, 'w') as file:
        file.write(updated_content)

# Question: Write a program that takes two numbers from the user and divides them. Handle the 0 division error and value error.
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"The result of division is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

# Question: Create a simple text editor using tkinter. Include the menu bar with options New, Open, Save, and Exit. 
# Implement file dialogs to open and save files. Allow the user to edit text in a text widget.
from tkinter import Tk, Text, Menu, filedialog, messagebox

def create_text_editor():
    def new_file():
        text_area.delete(1.0, "end")

    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                text_area.delete(1.0, "end")
                text_area.insert("1.0", file.read())

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, "end-1c"))

    def exit_editor():
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            root.destroy()

    root = Tk()
    root.title("Simple Text Editor")

    text_area = Text(root, wrap="word", font=("Arial", 12))
    text_area.pack(expand=True, fill="both")

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_editor)
    menu_bar.add_cascade(label="File", menu=file_menu)

    root.config(menu=menu_bar)
    root.mainloop()

# Question: A website requires the users to input username and password to register. Construct a program to check the validity of password input by users.
# The password must meet the following criteria:
# 1. At least one letter between a to z.
# 2. At least one letter between A to Z.
# 3. At least one number between 0 to 9.
# 4. At least one character from $, #, @.
# 5. Minimum length of 6 and maximum length of 12.
import re

def validate_passwords(passwords):
    valid_passwords = []
    for password in passwords.split(","):
        if (6 <= len(password) <= 12 and
            re.search(r"[a-z]", password) and
            re.search(r"[A-Z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[$#@]", password)):
            valid_passwords.append(password)
    print(",".join(valid_passwords))

# Question: Create a tuple and perform the following methods. Add items, "len", check for items in tuple, access items.
def tuple_operations():
    my_tuple = ("apple", "banana", "cherry")
    my_tuple = my_tuple + ("orange",)
    print("Tuple after adding an item:", my_tuple)
    print("Length of the tuple:", len(my_tuple))
    print(f"Is 'banana' in the tuple?", "banana" in my_tuple)
    print("First item in the tuple:", my_tuple[0])
    print("Last item in the tuple:", my_tuple[-1])

# Question: Write a program that asks the user to enter a length in feet. The program should then give the user the option to convert feet into inches, yards, miles, millimeters, centimeters, meters, or kilometers.
def convert_length():
    conversions = {
        1: ("inches", 12),
        2: ("yards", 1 / 3),
        3: ("miles", 1 / 5280),
        4: ("millimeters", 304.8),
        5: ("centimeters", 30.48),
        6: ("meters", 0.3048),
        7: ("kilometers", 0.0003048)
    }

    try:
        feet = float(input("Enter the length in feet: "))
        print("Choose a conversion option:")
        print("1. Inches")
        print("2. Yards")
        print("3. Miles")
        print("4. Millimeters")
        print("5. Centimeters")
        print("6. Meters")
        print("7. Kilometers")
        choice = int(input("Enter your choice (1-7): "))

        if choice in conversions:
            unit, factor = conversions[choice]
            result = feet * factor
            print(f"{feet} feet is equal to {result} {unit}.")
        else:
            print("Invalid choice. Please select a number between 1 and 7.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Question: Write a Python program to create a lab timer that records the time for each lap, displays the total time, and allows the time to be started, stopped, or reset.
import time

def lab_timer():
    laps = []
    start_time = None

    while True:
        print("\nOptions:")
        print("1. Start Timer")
        print("2. Record Lap")
        print("3. Stop Timer")
        print("4. Reset Timer")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            if start_time is None:
                start_time = time.time()
                print("Timer started.")
            else:
                print("Timer is already running.")

        elif choice == "2":
            if start_time is not None:
                lap_time = time.time() - start_time
                laps.append(lap_time)
                print(f"Lap {len(laps)} recorded: {lap_time:.2f} seconds.")
            else:
                print("Timer is not running. Start the timer first.")

        elif choice == "3":
            if start_time is not None:
                total_time = time.time() - start_time
                print(f"Timer stopped. Total time: {total_time:.2f} seconds.")
                start_time = None
            else:
                print("Timer is not running.")

        elif choice == "4":
            laps.clear()
            start_time = None
            print("Timer reset.")

        elif choice == "5":
            print("Exiting lab timer.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Question: Write a Python program using fundamental operations of indexing, slicing using numpy and scipy packages in Python.
import numpy as np
from scipy import stats

def numpy_scipy_indexing_slicing():
    # Create a numpy array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Original Array:")
    print(arr)

    # Indexing
    print("Element at position (1, 2):", arr[1, 2])  # Access element at row 1, column 2
    print("First row:", arr[0])  # Access the first row
    print("First column:", arr[:, 0])  # Access the first column

    # Slicing
    print("Sub-array (first two rows and columns):")
    print(arr[:2, :2])  # Slice first two rows and columns
    print("Last row:", arr[-1])  # Access the last row
    print("Last two columns:")
    print(arr[:, -2:])  # Slice the last two columns

    # Scipy operation (mean along axis)
    print("Mean of each column:", np.mean(arr, axis=0))
    print("Mean of each row:", np.mean(arr, axis=1))

# Question: Write a Python program that takes an integer input from the user and computes the prime factorization of the integer. 
# The program should return a list of prime factors, where each factor appears as many times as it divides the integer.
def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

# Question: Given a square matrix with N rows and N columns, write a program to rotate this matrix such that each element is shifted by one place in a clockwise manner.
def rotate_matrix_clockwise(matrix):
    n = len(matrix)
    if n == 0 or n != len(matrix[0]):
        print("The input must be a square matrix.")
        return

    # Extract the outer layer
    top = matrix[0]
    right = [matrix[i][n - 1] for i in range(1, n)]
    bottom = matrix[n - 1][:-1][::-1]
    left = [matrix[i][0] for i in range(n - 2, 0, -1)]

    # Combine the outer layer into a single list
    outer_layer = top + right + bottom + left

    # Rotate the outer layer by one position
    rotated_layer = [outer_layer[-1]] + outer_layer[:-1]

    # Place the rotated values back into the matrix
    idx = 0
    for i in range(n):
        matrix[0][i] = rotated_layer[idx]
        idx += 1
    for i in range(1, n):
        matrix[i][n - 1] = rotated_layer[idx]
        idx += 1
    for i in range(n - 2, -1, -1):
        matrix[n - 1][i] = rotated_layer[idx]
        idx += 1
    for i in range(n - 2, 0, -1):
        matrix[i][0] = rotated_layer[idx]
        idx += 1

    # Print the rotated matrix
    for row in matrix:
        print(row)

# Question: Write a program that opens a tkinter window with a button. When the button is clicked, a new window pops up with a label saying "Hello World".
# Create a button that when clicked opens a new top-level window with a label.
import tkinter as tk
from tkinter import Toplevel, Label, Button

def open_new_window():
    new_window = Toplevel()
    new_window.title("New Window")
    new_window.geometry("200x100")
    label = Label(new_window, text="Hello World", font=("Arial", 14))
    label.pack(pady=20)

def main_window():
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x200")

    button = Button(root, text="Open New Window", command=open_new_window, font=("Arial", 12))
    button.pack(pady=50)

    root.mainloop()

# Demonstration of string_utils module functions

# In the string_utils.py file, you would have the following functions:

# def reverse_string(s):
#     """Reverses the given string."""
#     return s[::-1]

# def count_character(s, char):
#     """Counts the occurrences of a specific character in the string."""
#     return s.count(char)

# def is_palindrome(s):
#     """Checks if the given string is a palindrome."""
#     return s == s[::-1]

from string_utils import reverse_string, count_character, is_palindrome

def demonstrate_string_utils():
    test_string = "madam"
    char_to_count = "a"

    # Reverse the string
    reversed_str = reverse_string(test_string)
    print(f"Reversed string: {reversed_str}")

    # Count occurrences of a specific character
    count = count_character(test_string, char_to_count)
    print(f"Occurrences of '{char_to_count}': {count}")

    # Check if the string is a palindrome
    palindrome_check = is_palindrome(test_string)
    print(f"Is the string '{test_string}' a palindrome? {palindrome_check}")

# Question: Using numpy module, create an array and check the following:
# Reshape 3x4 array into 2x2x3 array, sequence of integers from zero to 30 with step of five, flatten array, constant value array of complex type.
import numpy as np

def numpy_array_operations():
    # Reshape 3x4 array into 2x2x3 array
    arr = np.arange(12).reshape(3, 4)
    reshaped_arr = arr.reshape(2, 2, 3)
    print("Original 3x4 array:")
    print(arr)
    print("Reshaped 2x2x3 array:")
    print(reshaped_arr)

    # Sequence of integers from 0 to 30 with step of 5
    sequence = np.arange(0, 31, 5)
    print("Sequence of integers from 0 to 30 with step of 5:")
    print(sequence)

    # Flatten a 2D array into a 1D array
    flattened = arr.flatten()
    print("Flattened 1D array:")
    print(flattened)

    # Constant value array of complex type
    complex_arr = np.full((3, 3), 7 + 2j, dtype=complex)
    print("Constant value array of complex type:")
    print(complex_arr)

# Question: Write a Python program to find how many times each day of the week occurs in a given year.
import calendar

def count_weekdays_in_year(year):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_counts = {day: 0 for day in weekdays}

    for month in range(1, 13):
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            weekday = calendar.weekday(year, month, day)
            weekday_counts[weekdays[weekday]] += 1

    print(f"Day counts for the year {year}:")
    for day, count in weekday_counts.items():
        print(f"{day}: {count}")

# Question: Write a Python program to find the line numbers in a text file where a given word appears.
def find_word_in_file(file_path, word):
    line_numbers = []
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if word in line:
                line_numbers.append(line_number)
    print(f"The word '{word}' appears in the following lines: {line_numbers}")

# Question: Write a program that asks the user for a weight in kilograms and converts it into pounds.
def convert_kg_to_pounds():
    try:
        weight_kg = float(input("Enter weight in kilograms: "))
        weight_pounds = weight_kg * 2.20462
        print(f"{weight_kg} kilograms is equal to {weight_pounds:.2f} pounds.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Question: Python program to check whether the given integer is a multiple of both five and seven.
def is_multiple_of_five_and_seven():
    try:
        num = int(input("Enter an integer: "))
        if num % 5 == 0 and num % 7 == 0:
            print(f"The number {num} is a multiple of both 5 and 7.")
        else:
            print(f"The number {num} is not a multiple of both 5 and 7.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Question: Write a Python program using fundamental operations of array creation and manipulation using numpy and scipy packages in Python.
import numpy as np
from scipy import stats

def numpy_scipy_array_operations():
    # Create a 1D array
    arr_1d = np.array([1, 2, 3, 4, 5])
    print("1D Array:", arr_1d)

    # Create a 2D array
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D Array:")
    print(arr_2d)

    # Reshape the array
    reshaped = arr_1d.reshape(5, 1)
    print("Reshaped Array (5x1):")
    print(reshaped)

    # Perform basic operations
    print("Sum of elements in 1D array:", np.sum(arr_1d))
    print("Mean of elements in 2D array:", np.mean(arr_2d))
    print("Standard deviation of 1D array:", np.std(arr_1d))

    # Find the mode of a 1D array
    mode_result = stats.mode(arr_1d)
    print("Mode of 1D array:", mode_result.mode[0], "with count:", mode_result.count[0])

    # Transpose the 2D array
    transposed = arr_2d.T
    print("Transposed 2D Array:")
    print(transposed)

    # Flatten the 2D array
    flattened = arr_2d.flatten()
    print("Flattened Array:")
    print(flattened)

# Question: Write a Python program to draw the line plot and bar chart for the following data. Imagine data for elapsed time and speed.
import matplotlib.pyplot as plt

def plot_time_speed():
    # Imaginary data for elapsed time (in seconds) and speed (in m/s)
    elapsed_time = [0, 1, 2, 3, 4, 5, 6]
    speed = [0, 3, 7, 12, 20, 30, 45.6]

    # Line plot
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(elapsed_time, speed, marker='o', color='blue', label='Speed vs Time')
    plt.title("Line Plot: Speed vs Time")
    plt.xlabel("Elapsed Time (s)")
    plt.ylabel("Speed (m/s)")
    plt.legend()
    plt.grid()

    # Bar chart
    plt.subplot(1, 2, 2)
    plt.bar(elapsed_time, speed, color='green', label='Speed')
    plt.title("Bar Chart: Speed vs Time")
    plt.xlabel("Elapsed Time (s)")
    plt.ylabel("Speed (m/s)")
    plt.legend()
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()

# Question: Write a Python program to accept the lengths of three sides of a triangle. 
# First, check whether the sides can form a triangle. If so, determine if it's equilateral, isosceles, or scalene.
def classify_triangle():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    # Check if the sides can form a triangle
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("The triangle is equilateral.")
        elif a == b or b == c or a == c:
            print("The triangle is isosceles.")
        else:
            print("The triangle is scalene.")
    else:
        print("The given sides do not form a triangle.")

# Question: Write a program where a global variable score equal to zero is modified inside a function, update score using the global keyword. Call the function multiple times and print the final score.
score = 0

def update_score(points):
    global score
    score += points
    print(f"Score updated by {points}. Current score: {score}")

# Example usage
update_score(10)
update_score(5)
update_score(20)
print(f"Final score: {score}")

# Question: Write a Python program to create a zip file of a particular folder which contains several files inside it.
import os
import zipfile

def create_zip(folder_path, zip_name):
    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)
        print(f"Zip file '{zip_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# folder_path = "path_to_folder"
# zip_name = "output.zip"
# create_zip(folder_path, zip_name)

# Question: Write a Python program to accept a positive integer N and print its square root with precision up to five decimal places.
import math

def print_square_root():
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer.")
            return
        square_root = math.sqrt(n)
        print(f"The square root of {n} is {square_root:.5f}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

# Question: Write a script named copyfile.py. The script should prompt the user for the names of the two text files. 
# The contents of the first file should be input and written to the second file.
# Note: This code must be in a file named copyfile.py.
def copy_file():
    try:
        source_file = input("Enter the name of the source file: ")
        destination_file = input("Enter the name of the destination file: ")

        with open(source_file, 'r') as src:
            content = src.read()

        with open(destination_file, 'w') as dest:
            dest.write(content)

        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
    except FileNotFoundError:
        print("The source file does not exist. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
copy_file()

# Question: Create a package mathpack with sub-packages algebra and geometry. 
# In algebra, create linear.py with a function solve_linear(a, b) to solve ax + b = 0.
# In geometry, create circle.py with a function area(radius) to calculate the area of a circle.
# Write a main script that uses both.

# Note: The following code must be organized into the specified package structure.

# File: mathpack/algebra/linear.py
def solve_linear(a, b):
    if a == 0:
        return "No solution" if b != 0 else "Infinite solutions"
    return -b / a

# File: mathpack/geometry/circle.py
import math

def area(radius):
    return math.pi * radius ** 2

# Main script to use both modules
# Using solve_linear from algebra.linear
from mathpack.algebra.linear import solve_linear
a, b = 2, -4
print(f"Solution to {a}x + {b} = 0 is x = {solve_linear(a, b)}")

# Using area from geometry.circle
from mathpack.geometry.circle import area
radius = 5
print(f"Area of a circle with radius {radius} is {area(radius):.2f}")

# Question: Write a Python program that simulates two moving shapes on a 2D plane and checks for collision between them.
# Use the tkinter library to create and animate the shapes.

import tkinter as tk
import random

def check_collision(canvas, shape1, shape2):
    coords1 = canvas.coords(shape1)
    coords2 = canvas.coords(shape2)
    return not (coords1[2] < coords2[0] or coords1[0] > coords2[2] or coords1[3] < coords2[1] or coords1[1] > coords2[3])

def move_shapes():
    global dx1, dy1, dx2, dy2

    canvas.move(shape1, dx1, dy1)
    canvas.move(shape2, dx2, dy2)

    coords1 = canvas.coords(shape1)
    coords2 = canvas.coords(shape2)

    # Reverse direction if the shape hits the canvas boundary
    if coords1[0] <= 0 or coords1[2] >= 400:
        dx1 = -dx1
    if coords1[1] <= 0 or coords1[3] >= 400:
        dy1 = -dy1
    if coords2[0] <= 0 or coords2[2] >= 400:
        dx2 = -dx2
    if coords2[1] <= 0 or coords2[3] >= 400:
        dy2 = -dy2

    # Check for collision
    if check_collision(canvas, shape1, shape2):
        canvas.itemconfig(shape1, fill="red")
        canvas.itemconfig(shape2, fill="red")
    else:
        canvas.itemconfig(shape1, fill="blue")
        canvas.itemconfig(shape2, fill="green")

    root.after(50, move_shapes)

# Create the main window
root = tk.Tk()
root.title("Moving Shapes Collision Detection")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Create two shapes
shape1 = canvas.create_oval(50, 50, 100, 100, fill="blue")
shape2 = canvas.create_rectangle(200, 200, 250, 250, fill="green")

# Initial movement directions
dx1, dy1 = random.choice([-3, 3]), random.choice([-3, 3])
dx2, dy2 = random.choice([-3, 3]), random.choice([-3, 3])

# Start the animation
move_shapes()

root.mainloop()

# Question: Create a global variable rate equal to five. Define a function calculate_interest(principal) that:
# a. Uses the global rate without modifying it.
# b. Calculates the interest as interest = principal * rate / 100.
# c. Does not use the global keyword.

rate = 5

def calculate_interest(principal):
    interest = principal * rate / 100
    return interest

# Example usage
principal_amount = 1000
calculated_interest = calculate_interest(principal_amount)
print(f"The interest on a principal of {principal_amount} at a rate of {rate}% is {calculated_interest}.")

# Question: Create a canvas where a ball moves and bounces off the window edges. 
# Use the after method for smooth animation. Allow the user to start and stop the animation with buttons.

import tkinter as tk

class BouncingBallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Ball Animation")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(180, 180, 220, 220, fill="blue")
        self.dx, self.dy = 3, 3
        self.running = False

        self.start_button = tk.Button(root, text="Start", command=self.start_animation)
        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_animation)
        self.stop_button.pack(side="right", padx=10, pady=10)

    def move_ball(self):
        if not self.running:
            return

        self.canvas.move(self.ball, self.dx, self.dy)
        coords = self.canvas.coords(self.ball)

        # Bounce off edges
        if coords[0] <= 0 or coords[2] >= 400:
            self.dx = -self.dx
        if coords[1] <= 0 or coords[3] >= 400:
            self.dy = -self.dy

        self.root.after(20, self.move_ball)

    def start_animation(self):
        if not self.running:
            self.running = True
            self.move_ball()

    def stop_animation(self):
        self.running = False

# Example usage
root = tk.Tk()
app = BouncingBallApp(root)
root.mainloop()

# Question: Write a function named nearly_equal to test whether two strings are nearly equal.
# Two strings A and B are nearly equal when A can be generated by a single mutation on B.
# i. Write a function 'dups' to find all the duplicates in the list.
# ii. Write a function 'unique' to find all the unique elements in the list.

def nearly_equal(a, b):
    if len(a) != len(b):
        return False
    differences = sum(1 for x, y in zip(a, b) if x != y)
    return differences == 1

def dups(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def unique(lst):
    return list(set(lst))

# Example usage
# Test nearly_equal
print(nearly_equal("hello", "hallo"))  # True
print(nearly_equal("hello", "hella"))  # False

# Test dups
print(dups([1, 2, 3, 2, 4, 5, 1]))  # [1, 2]

# Test unique
print(unique([1, 2, 3, 2, 4, 5, 1]))  # [1, 2, 3, 4, 5]

# Question: Write a recursive function decimal_to_binary to convert a number to binary format.

def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

# Example usage
number = 10
print(f"Binary representation of {number} is {decimal_to_binary(number)}")  # Output: 1010

# Question: Write a program that asks the user to enter a word and prints out whether the word contains any vowels.

def contains_vowels(word):
    vowels = "aeiouAEIOU"
    for char in word:
        if char in vowels:
            return True
    return False

# Example usage
word = input("Enter a word: ")
if contains_vowels(word):
    print(f"The word '{word}' contains vowels.")
else:
    print(f"The word '{word}' does not contain any vowels.")

# Question: Write a program with Tkinter window that acts as a timer. Start the timer by pressing a button and stop it by pressing another button. Display the elapsed time on the label.

import tkinter as tk
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.start_time = None
        self.running = False

        self.label = tk.Label(root, text="Elapsed Time: 0.00s", font=("Arial", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Arial", 12))
        self.start_button.pack(side="left", padx=20, pady=20)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, font=("Arial", 12))
        self.stop_button.pack(side="right", padx=20, pady=20)

    def update_timer(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.label.config(text=f"Elapsed Time: {elapsed_time:.2f}s")
            self.root.after(100, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

# Example usage
root = tk.Tk()
app = TimerApp(root)
root.mainloop()

# Question: Write a Python program that uses recursion to determine whether a given string is palindrome or symmetrical.

def is_palindrome_or_symmetrical(s):
    # Helper function to check palindrome using recursion
    def is_palindrome(s, start, end):
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return is_palindrome(s, start + 1, end - 1)

    # Check if the string is symmetrical
    mid = len(s) // 2
    is_symmetrical = s[:mid] == s[-mid:]

    # Check if the string is a palindrome
    is_palindrome_result = is_palindrome(s, 0, len(s) - 1)

    return is_palindrome_result, is_symmetrical

# Example usage
string = input("Enter a string: ")
palindrome, symmetrical = is_palindrome_or_symmetrical(string)
if palindrome:
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")
if symmetrical:
    print(f"The string '{string}' is symmetrical.")
else:
    print(f"The string '{string}' is not symmetrical.")

# Question: Construct a program to read a CSV dataset, remove the last column and save it in an array. Save the last column to another array. Plot the first two columns.

import os
import numpy as np
import matplotlib.pyplot as plt
import csv

def process_and_plot_csv(file_path="cities.csv"):
    # Resolve the relative path to an absolute path
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    
    data = []
    last_column = []

    # Read the CSV file and process the data
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row[1:-1])  # Exclude the first (city names) and last column
            last_column.append(row[-1])  # Save the last column separately

    # Convert data to numpy arrays
    data_array = np.array(data, dtype=float)
    # Skip non-numeric values in the last column
    last_column_array = np.array([value for value in last_column if value.replace('.', '', 1).isdigit()], dtype=float)

    # Plot the first two columns
    plt.scatter(data_array[:, 0], data_array[:, 1], color='blue', label='First vs Second Column')
    plt.title("Scatter Plot of First Two Columns")
    plt.xlabel("First Column")
    plt.ylabel("Second Column")
    plt.legend()
    plt.grid()
    plt.show()

    return data_array, last_column_array

data_array, last_column_array = process_and_plot_csv()
print("Data Array (excluding last column):")
print(data_array)
print("Last Column Array:")
print(last_column_array)

# Question: Write a Python program to print the following pattern:
#      1
#    1  2
#   1  2  3
#  1  2  3  4
# 1  2  3  4  5

def print_number_pattern(n):
    for i in range(1, n + 1):
        # Print spaces for alignment
        print(" " * (n - i), end="")
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Move to the next line

# Example usage
rows = 5
print_number_pattern(rows)

# Question: Use a for loop to print a triangle like the one below. Allow the user to specify how high the triangle should be.
# *
# **
# ***
# ****

def print_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)

# Example usage
height = int(input("Enter the height of the triangle: "))
print_triangle(height)

# Question: Write a Python program that adds a button to the tkinter window. When the button is clicked, a message should be printed in the console like the button is clicked.

import tkinter as tk

def on_button_click():
    print("Button is clicked!")

root = tk.Tk()
root.title("Button Click Example")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

root.mainloop()

# Question: Write a Python program that takes two strings as input and determines if they are anagrams of each other, using dictionaries to count character frequencies.

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return all(count == 0 for count in char_count.values())

# Example usage
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if are_anagrams(str1, str2):
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")

# Question: Write a Python program that calculates the area of the circle using a function defined in a separate module.
# Import the function into your main program and use it to calculate the area of the circle with a radius of 5 units.

from mathpack.geometry.circle import area

# Example usage
radius = 5
circle_area = area(radius)
print(f"The area of the circle with radius {radius} units is {circle_area:.2f} square units.")

# Question: Construct a program which accepts a sequence of words separated by white space as file input. Print the words composed of digits only.

def print_digit_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        digit_words = [word for word in words if word.isdigit()]
        print("Words composed of digits only:", digit_words)

# Example usage
file_path = input("Enter the file path: ")
print_digit_words(file_path)

# Question: Write a function called primes that is given a number N and returns a list of the first N primes. Let the default value of N be 100.

def primes(N=100):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = []
    candidate = 2
    while len(prime_list) < N:
        if is_prime(candidate):
            prime_list.append(candidate)
        candidate += 1
    return prime_list

# Example usage
print(primes(10))  # Prints the first 10 prime numbers

# Question: Write a function called is_phone_number to recognize a pattern like 415-555-4242 without using regular expressions.

def is_phone_number(text):
    if len(text) != 12:
        return False
    if not text[:3].isdigit() or text[3] != '-' or not text[4:7].isdigit() or text[7] != '-' or not text[8:].isdigit():
        return False
    return True

# Question: Write the code to recognize the same pattern using regular expressions.

import re

def is_phone_number_regex(text):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, text))

# Example usage
print(is_phone_number("415-555-4242"))  # True
print(is_phone_number("123-abc-4567"))  # False
print(is_phone_number_regex("415-555-4242"))  # True
print(is_phone_number_regex("123-abc-4567"))  # False

# Question: Write a simple Python program that opens a tkinter window with a title "My First Workflow" and specified size of 400x300 pixels.

import tkinter as tk

def create_window():
    root = tk.Tk()
    root.title("My First Workflow")
    root.geometry("400x300")
    root.mainloop()

# Example usage
create_window()

# Question: Generate a random number between one and 10. Ask the user to guess the number and print the message based on whether they get it right or not.

import random

def guess_the_number():
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed it right.")
    else:
        print(f"Sorry, the correct number was {number}.")

# Example usage
guess_the_number()

