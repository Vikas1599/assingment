def mod_div(fun):
  def x(a,b):
    if a < b:
      a,b = b, a
    return fun(a,b)

  return x
@mod_div
def div(a,b):
  return a // b

a,b = (int(i) for i in input('Enter two values: ').split())
print(div(a, b))