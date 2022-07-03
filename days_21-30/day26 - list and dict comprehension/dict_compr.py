numbers = [n for n in range(5)]
d = {n: f"x{n}" for n in numbers}
d2 = {n: f"x{n}" for n in numbers if n % 2 == 0}

d3 = {k: v[:1] for k, v in d.items() if k % 2 == 1}

d4 = {k if k % 2 == 0 else str(k) + "+": v if k % 2 == 0 else v*3 for k, v in d.items()}

print(d)
print(d2)
print(d3)
print(d4)


