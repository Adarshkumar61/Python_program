# from sympy import symbols, diff, lambdify

# def fx(x):
#     input("Enter the function in terms of x: ")
#     func_str = input("Enter the function in terms of x (e.g., x**2 - 4): ")
#     def f(x):
#         return eval(func_str, {"x": x, "__builtins__": {}})
#     x_sym = symbols('x')
#     f_expr = eval(func_str, {"x": x_sym})
#     f_prime = lambdify(x_sym, diff(f_expr, x_sym))
#     root = float(input("Enter initial guess for root: "))
#     for i in range(10):
#         approx = root - f(root) / f_prime(root)
#         print(f"Iteration {i+1}: x = {approx}")
#         if abs(approx - root) < 1e-6:
#             break
#         root = approx
#     print(f"Approximate root: {approx}")
# while True:
#     try:
#         fx('x')
#         break
#     except Exception as e:
#         print("Wrong method, write again with proper term.")



import sympy as sp

# Step 1: Take user input for function
expr_input = input("Enter function f(x): ")  # e.g. x**3 - 3*x + 2

# Step 2: Define symbol and function
x = sp.symbols('x')
f = sp.sympify(expr_input)   # convert string to sympy expression

# Step 3: Derivative of f(x)
df = sp.diff(f, x)
print("f(x) =", f)
print("f'(x) =", df)

# Step 4: Take initial guess from user
x0 = float(input("Enter initial guess: "))

# Step 5: Newton–Raphson Method
tol = 1e-6
max_iter = 100
xn = x0

for i in range(max_iter):
    fx = f.subs(x, xn)
    dfx = df.subs(x, xn)
    
    if dfx == 0:
        print("Derivative is zero. Stopping.")
        break
    
    x_new = float(xn - fx/dfx)
    
    print(f"Iteration {i+1}: x = {x_new}, f(x) = {fx}")
    
    if abs(x_new - xn) < tol:
        print(f"\nApproximate root = {x_new}")
        break
    
    xn = x_new
else:
    print(f"\nDid not converge after {max_iter} iterations. Last value = {xn}")
