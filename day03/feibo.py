def fib(l=5):
    feibo=[0, 1]
    for i in range(l-len(feibo)):
     feibo.append(feibo[-1]+feibo[-2])
    return feibo


print(fib())