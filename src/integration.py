# integration.py
def integrate_simpson(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n, 2):
        result += 4 * f(a + i * h)

    for i in range(2, n-1, 2):
        result += 2 * f(a + i * h)

    result *= h / 3
    return result

def f(x):
    # Define the function to be integrated
    return x**2
