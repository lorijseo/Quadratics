# include imaginary solutions.

def quadratic_e():
    print("Welcome to 'Exploring Quadratics'. Given the quadratic in standard form, ax^2 + bx + c = 0,"
          " provide 'a', 'b', and 'c' so we can help you with your quadratic!")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    while a != 0:
        menu = input("\nMENU:\ntype '1' to solve for x\ntype '2' to get help with graphing\n"
                     "type '3' to know the concavity of your graph\ntype '4' for x and y intercepts\n"
                     "type '5' to find roots\ntype '6' to find the zeroes\n"
                     "type '7' to find number of solutions\ntype '8' to find vertex\ntype '9' to exit\n")
        # information
        discriminant = (b ** 2) - (4 * a * c)
        solution_1 = (-b + (discriminant ** 0.5)) / (2 * a)
        solution_2 = (-b - (discriminant ** 0.5)) / (2 * a)
        vertex_x = (-b / (2 * a))
        vertex_y = a * (vertex_x ** 2) + (b * vertex_x) + c
        # solve
        if menu == '1':
            if discriminant > 0:
                print(f"Solutions are x = {solution_1} and x = {solution_2}")
            elif discriminant == 0:
                print(f"Solution is x = {solution_1}")
            else:
                print("There are no real solutions. 'Quadratic Solver' cannot find imaginary solutions yet. ")
        # graph
        elif menu == '2':
            print("We can use the vertex, intercepts, and concavity to graph quadratics.")
            print(f"First, plot the vertex. The vertex is at ({vertex_x},{vertex_y}).")
            if discriminant > 0:
                print(
                    f"Second, plot the intercepts. x-intercepts = ({solution_1},0) and ({solution_2},0)\n"
                    f"y-intercept = (0,{c})")
            elif discriminant == 0:
                print(f"Second, plot the intercepts. x-intercept = ({solution_1},0),0)\ny-intercept = (0,{c})")
            else:
                print(
                    f"There are no x-intercepts, so the graph will be above or below the x-axis. "
                    f"Plot only the y-intercept at (0,{c})")
            if a > 0:
                print("This quadratic is CONCAVE UP. Connect your points so your parabola opens upwards.")
            elif a < 0:
                print("This quadratic is CONCAVE DOWN. Connect your points so your parabola opens downwards.")
            else:
                print("This is not a quadratic.")
        # concavity
        elif menu == '3':
            if a > 0:
                print("This quadratic is CONCAVE UP. This means the parabola will open upwards.")
            elif a < 0:
                print("This quadratic is CONCAVE DOWN. This means the parabola will open downwards.")
            else:
                print("This is not a quadratic. 'Quadratic Solver' cannot help you with this problem.")
        # intercepts
        elif menu == '4':
            if discriminant > 0:
                print(f"x-intercept(s) = ({solution_1},0) and ({solution_2},0)")
            elif discriminant == 0:
                print(f"x-intercept = ({solution_1},0)")
            else:
                print("There are no x-intercepts.")
        # roots
        elif menu == '5':
            print(
                f"Roots are the values that make the quadratic equal to zero. "
                f"This means that roots are the same as x-intercepts and zeros.")
            if discriminant > 0:
                print(f"The roots are at x = {solution_1} and x = {solution_2}.")
            elif discriminant == 0:
                print(f"The root is at x = {solution_1}")
            else:
                print("There are no roots.")
                # zeroes
        elif menu == '6':
            print(
                f"Zeros are the values that make the quadratic equal to zero. "
                f"This means that zeros are the same as x-intercepts and roots.")
            if discriminant > 0:
                print(f"The zeros are at x = {solution_1} and x = {solution_2}.")
            elif discriminant == 0:
                print(f"The zero is at x = {solution_1}")
            else:
                print("There are no zeros.")
                # number of solutions, discriminant
        elif menu == '7':
            if discriminant > 0:
                print("This quadratic has two real solutions.")
            elif discriminant == 0:
                print("This quadratic has one real solution.")
            else:
                print("This quadratic has no real solutions.")
        # vertex
        elif menu == '8':
            print(f"The vertex is at ({vertex_x},{vertex_y}).")
        elif menu == '9':
            print("Good luck! Bye :)")
            exit()
        # other
        else:
            print("Please type a number in the menu.")

    else:
        option = input("This is not a quadratic. The value of 'a' should not be zero.\nType '1' to try again.\n"
                       "Type '2' to quit 'Exploring Quadratics'.\n")
        if option == '1':
            quadratic_e()
        else:
            print("Good luck with your math adventures! Hope to see you soon :)")
            exit()


quadratic_e()
