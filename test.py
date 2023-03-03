def test(a,b):
    return a+b

args = {"a":1,"b":2}

print(test(**args))
