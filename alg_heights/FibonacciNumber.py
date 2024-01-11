
proxy = {}

def Fibonacci_recursive(number):
  if number <= 2:
    return 1
  elif number in proxy:
    return proxy[number]
  else:
    result = Fibonacci_recursive(number - 1) + Fibonacci_recursive(number - 2)
    proxy[number] = result
    return result
  
print(Fibonacci_recursive(4))