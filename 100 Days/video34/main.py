ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# update mathod
ep2.update({222:133})
ep2.update({566:1903})
ep2.update(ep2)
print(ep2)

# clear mathod
ep3={1:989,2:"jay"}
ep3.clear()
print(ep3)

# pop mathod
ep1.pop(122)
print(ep1)

# popitem mathod
ep1.popitem()
print(ep1)

# del mathod
del ep1[567]
print(ep1)

del ep2
# print(ep2)