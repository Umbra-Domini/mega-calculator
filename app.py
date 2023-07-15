#Manraaj Singh
#Date started - July 14, 2023

#Importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

#Spacing
print("")
print("")

#Intro
print("█▀▄▀█ █▀▀ █▀▀ ▄▀█ ▄▄ █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█")
print("█░▀░█ ██▄ █▄█ █▀█ ░░ █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄")
print("Raaj-S-2005")

#Spacing
print("")
print("")

print("Options:")

#Spacing
print("")

#Options
print("1 - Cubic graph calculator (and grapher)")
print("2 - Quadratic calculator")
print("3 - Coming soon")

#Spacing
print("")
print("")

#Choose option
option = int(input("Choose option: "))

if option == 1:
    #Spacing
    print("")
    print("")
    
    #Printing the inro line
    print("The transformations will be calculated in the given form (y = a√(b(x - h)) + k")

    # Generate x values from -10 to 10
    x = np.linspace(-10, 10, 100)

    #Spacing
    print("")
    print("")

    # Ask for all the 4 values
    a_input = input("What is the value of a (leave blank if no 'a' is given): ")
    if '/' in a_input:
        numerator, denominator = a_input.split('/')
        a = float(numerator) / float(denominator)
    elif not a_input:
        a = 1.0
    else:
        a = float(a_input)


    b_input = input("What is the value of b (leave blank if no 'b' is given): ")
    if '/' in b_input:
        numerator, denominator = b_input.split('/')
        b = float(numerator) / float(denominator)
    elif not b_input:
        b = 1.0
    else:
        b = float(b_input)


    h_input = input("What is the value of h (leave blank if no 'h' is given): ")
    if '/' in h_input:
        numerator, denominator = h_input.split('/')
        h = float(numerator) / float(denominator)
    elif not h_input:
        h = 0
    else:
        h = float(h_input)


    k_input = input("What is the value of k (leave blank if no 'k' is given): ")
    if '/' in k_input:
        numerator, denominator = k_input.split('/')
        k = float(numerator) / float(denominator)
    elif not k_input:
        k = 0
    else:
        k = float(k_input)

    #Spacing
    print("")
    print("")


    # Print all the transformations
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"h = {h}")
    print(f"k = {k}")


    print("")
    print("")

    #a reflection
    if a > 0 :
        print("There is no reflection over the x-axis.")

    else:
        print("There is a reflection over the x-axis")

    #a vertical stretch
    if abs(a) > 1:
        print(f"There is a vertical stretch by a factor of {abs(a)}")

    elif abs(a) < 1:
        print(f"There is a vertical stretch by a factor of {abs(a)}")

    elif abs(a) == 1:
        print("There is no vertical stretch.")

    #spacing
    print("")
    print("")


    #b reflection
    if b > 0 :
        print("There is no reflection over the y-axis.")

    else:
        print("There is a reflection over the y-axis")

    #b horizontal stretch
    if abs(b) > 1:
        print(f"There is a horizontal stretch by a factor of {(1/abs(b))}")

    elif abs(b) < 1:
        print(f"There is a horizontal stretch by a factor of {(1/abs(b))}")

    elif abs(b) == 1:
        print("There is no horizontal stretch.")


    #spacing
    print("")
    print("")

    #h translations
    if h > 0:
        print(f"{abs(h)} units to the left")
    elif h < 0:
        print(f"{abs(h)} units to the right")
    elif h == 0:
        print("No horizontal translations")
    else:
        print('Invalid option chosen!')
        exit()

    #spacing
    print("")
    print("")


    #k translations
    if k > 0:
        print(f"{abs(k)} units up")
    elif k < 0:
        print(f"{abs(k)} units down")
    elif k == 0:
        print("No vertical translations")
    else:
        print('Invalid option chosen!')
        exit()

    #spacing
    print("")
    print("")


    #Points1
    x1 = 0
    x1_after = (x1 * (1/b)) + -(h)
    y1 = 0
    y1_after = (y1 * a) + k

    #Points2
    x2 = 1
    x2_after = (x2 * (1/b)) + -(h)
    y2 = 1
    y2_after = (y2 * a) + k

    #Points3
    x3 = 4
    x3_after = (x3 * (1/b)) + -(h)
    y3 = 2
    y3_after = (y3 * a) + k

    #Points4
    x4= 9
    x4_after = (x4 * (1/b)) + -(h)
    y4 = 3
    y4_after = (y4 * a) + k

    #Points5
    x5 = 16
    x5_after = (x5 * (1/b)) + -(h)
    y5 = 4
    y5_after = (y5 * a) + k

    #Points6
    x6 = 25
    x6_after = (x6 * (1/b)) + -(h)
    y6 = 5
    y6_after = (y6 * a) + k

    #Points7
    x7 = 36
    x7_after = (x7 * (1/b)) + -(h)
    y7 = 6
    y7_after = (y7 * a) + k

    #Points8
    x8 = 49
    x8_after = (x8 * (1/b)) + -(h)
    y8 = 7
    y8_after = (y8 * a) + k

    #Points9
    x9 = 64
    x9_after = (x9 * (1/b)) + -(h)
    y9 = 8
    y9_after = (y9 * a) + k

    #Points10
    x10 = 81
    x10_after = (x10 * (1/b)) + -(h)
    y10 = 9
    y10_after = (y10 * a) + k

    #Points11
    x11 = 100
    x11_after = (x11 * (1/b)) + -(h)
    y11 = 10
    y11_after = (y11 * a) + k


    # Define the new points
    new_points = [(x1_after, y1_after), (x2_after, y2_after), (x3_after, y3_after), (x4_after, y4_after), (x5_after, y5_after), (x6_after, y6_after),
                (x7_after, y7_after), (x8_after, y8_after), (x9_after, y9_after), (x10_after, y10_after), (x11_after, y11_after)]

    # Calculate the midpoint of the list
    midpoint = len(new_points) // 2

    #Print points
    print("The new points are:")

    #Spacing
    print("")

    # Print the list into two columns
    for i in range(midpoint):
        point1 = new_points[i]
        point2 = new_points[i + midpoint]
        print(f"{point1}    {point2}")


    # Separate the new points into x and y lists
    x_new = [point[0] for point in new_points]
    y_new = [point[1] for point in new_points]

    # Calculate square root values for x-range
    x_sqrt = np.linspace(0, max(x_new), 100)
    y_sqrt = np.sqrt(x_sqrt)

    # Plot the points and connect them with lines
    plt.figure(figsize=(8, 6))
    plt.scatter(x_new, y_new, color='blue', marker='o', label='Points')
    plt.plot(x_new, y_new, color='red', label="Transformed Graph")

    # Add labels to the points
    for i in range(len(new_points)):
        plt.text(x_new[i], y_new[i], f'({x_new[i]}, {y_new[i]})', ha='left', va='bottom')

    # Plot the square root graph
    plt.plot(x_sqrt, y_sqrt, color='green', label='Square Root (Original)')


    # Add labels and grid lines
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    # Maximize the graph window
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    # Show the plot
    plt.show()


    # Check for a 0 value in the y-coordinates
    rows_with_zero = []
    if y1_after == 0:
        rows_with_zero.append(1)
    if y2_after == 0:
        rows_with_zero.append(2)
    if y3_after == 0:
        rows_with_zero.append(3)
    if y4_after == 0:
        rows_with_zero.append(4)
    if y5_after == 0:
        rows_with_zero.append(5)
    if y6_after == 0:
        rows_with_zero.append(6)

    #spacing
    print("")
    print("")

    # Print the row(s) with a 0 value
    if rows_with_zero:
        print(f"The point(s) in row(s) {', '.join(map(str, rows_with_zero))} have a root.")
    else:
        print("No roots found in the first 10 points.")

elif option == 2:
    #Spacing
    print("")
    print

    #Ask for the three nunmbers (a, b, c)
    a_input = input("What is the value of a (leave blank if no 'a' is given): ")
    if not a_input:
        a = 0
    else:
        a = float(a_input)

    b_input = input("What is the value of b (leave blank if no 'b' is given): ")
    if not b_input:
        b = 0
    else:
        b = float(b_input)

    c_input = input("What is the value of c (leave blank if no 'c' is given): ")
    if not c_input:
        c = 0
    else:
        c = float(c_input)

    #Spacing
    print("")
    print("")

    #Solve for the part inside the square_root
    d = b ** 2 - (4 * a *c)

    #If the part inside the square root is more than 0 then add/subtract with -b
    if d > 0:
        a1 = (-(b) + math.sqrt(d)) / (2 * a)
        a2 = (-(b) - math.sqrt(d)) / (2 * a)

        print("The values are:")

        #Spacing
        print("")

        #Print answers
        print(f"x = {a1:.5f}")
        print(f"x = {a2:.5f}")
            

    #if the part inside the square_root is 0, then add/subtract with -b
    elif d == 0:
        a1 = (-(b) + d) / (2 * a)
        a2 = (-(b) - d) / (2 * a)
        #Print answers
        print(f"a1: {a1:.3f}")
        print(f"a2: {a2:.3f}")

    #If the part inside the square root is less than zero, then disaply that there are no root possible
    else:
        print("No roots for this question!")

else:
    print("Coming soon!!")
