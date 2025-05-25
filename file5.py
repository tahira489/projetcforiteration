def multiply_once(n, m):
  return n * m

def multiply_by_addition(n, m):
    result = 0
    for _ in range(n):
        result += m
    return result
n = int(input("Enter N: "))
m = int(input("Enter M: "))

product = multiply_once(n, m)
iterative = multiply_by_addition(n, m)
print(f"Multiplying {n} and {m} using 1 iteration: {product}")
print(f"Multiplying {n} and {m} using {n} iterations : {iterative}")