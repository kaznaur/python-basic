
def fibonaci(n):
  if n <= 1:
    return n
  else:
    return (fibonaci(n - 1)+fibonaci(n-2))

print(fibonaci(5))
# for i in range(11):
#   print(fibonaci(i))

