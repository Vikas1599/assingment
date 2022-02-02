# question: From a dict, how can we print the Key whose value is maximum ??

x= {"a":6, "b": 2, "c": 3,"d": 4}
max_value = max(x,key=x.get)
print(max_value)