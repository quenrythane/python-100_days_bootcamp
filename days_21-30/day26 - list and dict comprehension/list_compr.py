numbers = [n if n % 2 == 0 else "x" for n in range(5)]
func = lambda n: n+1
numbers2 = [func(n) for n in range(5)]



print(numbers)
print(numbers2)
