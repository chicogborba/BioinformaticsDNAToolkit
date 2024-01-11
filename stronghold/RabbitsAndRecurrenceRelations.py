proxy = {}

def Fibonacci_recursive(month, offspring):
    if month <= 2:
        return 1
    elif month in proxy:
        return proxy[month]
    else:
        result = (Fibonacci_recursive(month - 1, offspring)) + Fibonacci_recursive(month - 2, offspring) * offspring
        proxy[month] = result
        return result

print(Fibonacci_recursive(32, 2))
