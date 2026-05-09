with open("rosalind_fib.txt") as f:
    n, k = map(int, f.read().strip().split())

a, b = 1, 1
for _ in range(n - 2):
    a, b = b, k * a + b

print(b)