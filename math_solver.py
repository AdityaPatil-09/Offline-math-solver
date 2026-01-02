# ==========================================================
# OFFLINE MULTI-VARIABLE MATH SOLVER
# Uses: Python + SymPy
# ==========================================================

# Import required SymPy functions
from sympy import ( symbols, sympify, diff, integrate, limit, solve, simplify)

# ----------------------------------------------------------
# STEP 1: Declare symbols (variables)
# These are the variables the solver understands
# ----------------------------------------------------------
x, y, z = symbols('x y z')

# ----------------------------------------------------------
# BASIC OPERATIONS (Simplify, Add, Subtract, Multiply, Divide)
# ----------------------------------------------------------
def basic_operations():
    try:
        # Take expression input from user
        expr = sympify(input("Enter expression: "))

        print("\nChoose operation:")
        print("1. Simplify")
        print("2. Add number")
        print("3. Subtract number")
        print("4. Multiply by number")
        print("5. Divide by number")

        choice = input("Choice: ")

        if choice == "1":
            print("Result:", simplify(expr))

        elif choice == "2":
            n = sympify(input("Enter number: "))
            print("Result:", expr + n)

        elif choice == "3":
            n = sympify(input("Enter number: "))
            print("Result:", expr - n)

        elif choice == "4":
            n = sympify(input("Enter number: "))
            print("Result:", expr * n)

        elif choice == "5":
            n = sympify(input("Enter number: "))
            if n == 0:
                print("Error: Division by zero")
            else:
                print("Result:", expr / n)

        else:
            print("Invalid choice")

    except:
        print("Invalid expression input")

# ----------------------------------------------------------
# DERIVATIVE SOLVER (Supports partial derivatives)
# ----------------------------------------------------------
def derivative_solver():
    try:
        expr = sympify(input("Enter function: "))
        var = input("Differentiate with respect to (x/y/z): ")

        if var == "x":
            print("Derivative:", diff(expr, x))
        elif var == "y":
            print("Derivative:", diff(expr, y))
        elif var == "z":
            print("Derivative:", diff(expr, z))
        else:
            print("Invalid variable")

    except:
        print("Invalid input")

# ----------------------------------------------------------
# INTEGRATION SOLVER (Single / Double / Triple)
# ----------------------------------------------------------
def integration_solver():
    try:
        expr = sympify(input("Enter function: "))

        print("\nChoose integration type:")
        print("1. Single integral")
        print("2. Double integral")
        print("3. Triple integral")

        choice = input("Choice: ")

        # -------- SINGLE INTEGRAL --------
        if choice == "1":
            var = input("Integrate with respect to (x/y/z): ")
            lower = input("Lower limit (leave blank for indefinite): ")
            upper = input("Upper limit (leave blank for indefinite): ")

            if lower == "" or upper == "":
                print("Result:", integrate(expr, symbols(var)))
            else:
                print("Result:", integrate(expr, (symbols(var), sympify(lower), sympify(upper))))

        # -------- DOUBLE INTEGRAL --------
        elif choice == "2":
            v1 = input("First variable (x/y/z): ")
            l1 = sympify(input("Lower limit of first variable: "))
            u1 = sympify(input("Upper limit of first variable: "))

            v2 = input("Second variable (x/y/z): ")
            l2 = sympify(input("Lower limit of second variable: "))
            u2 = sympify(input("Upper limit of second variable: "))

            print("Result:", integrate(
                expr,
                (symbols(v1), l1, u1),
                (symbols(v2), l2, u2)
            ))

        # -------- TRIPLE INTEGRAL --------
        elif choice == "3":
            v1 = input("First variable (x/y/z): ")
            l1 = sympify(input("Lower limit: "))
            u1 = sympify(input("Upper limit: "))

            v2 = input("Second variable (x/y/z): ")
            l2 = sympify(input("Lower limit: "))
            u2 = sympify(input("Upper limit: "))

            v3 = input("Third variable (x/y/z): ")
            l3 = sympify(input("Lower limit: "))
            u3 = sympify(input("Upper limit: "))

            print("Result:", 
                integrate( expr,
                (symbols(v1), l1, u1),
                (symbols(v2), l2, u2),
                (symbols(v3), l3, u3))
                )

        else:
            print("Invalid choice")

    except:
        print("Invalid input")

# ----------------------------------------------------------
# LIMIT SOLVER (Single variable)
# ----------------------------------------------------------
def limit_solver():
    try:
        expr = sympify(input("Enter function: "))
        var = input("Limit with respect to (x/y/z): ")
        point = sympify(input("Value approached: "))

        print("Limit:", limit(expr, symbols(var), point))

    except:
        print("Invalid input")

# ----------------------------------------------------------
# EQUATION SOLVER (Single or Multiple variables)
# ----------------------------------------------------------
def equation_solver():
    try:
        print("Enter equations in =0 form")
        print("Example: x + y - 5")

        n = int(input("Number of equations: "))
        equations = []

        for i in range(n):
            eq = sympify(input(f"Equation {i+1}: "))
            equations.append(eq)

        vars_input = input("Variables (comma separated, e.g. x,y): ")
        vars_list = [symbols(v.strip()) for v in vars_input.split(",")]

        print("Solution:", solve(equations, vars_list))

    except:
        print("Invalid input")

# ----------------------------------------------------------
# MAIN MENU (User Interface)
# ----------------------------------------------------------
while True:
    print("\n===================================")
    print("       MATH SOLVER")
    print("===================================")
    print("1. Basic Operations")
    print("2. Derivative (Partial supported)")
    print("3. Integration (Single/Double/Triple)")
    print("4. Limit")
    print("5. Solve Equation(s)")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        basic_operations()
    elif choice == "2":
        derivative_solver()
    elif choice == "3":
        integration_solver()
    elif choice == "4":
        limit_solver()
    elif choice == "5":
        equation_solver()
    elif choice == "6":
        print("Exiting Math Solver. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")