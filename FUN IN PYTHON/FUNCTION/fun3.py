# Recursion is the process of defining something in terms of itself.

# A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

def face(x):
    if x==1:
        return 1
    else:
        return (x*face(x-1))

num=3
print('the facetorial of',num, 'is ', face(num))

# factorial(3)          # 1st call with 3
# 3 * factorial(2)      # 2nd call with 2
# 3 * 2 * factorial(1)  # 3rd call with 1
# 3 * 2 * 1             # return from 3rd call as number=1
# 3 * 2                 # return from 2nd call
# 6                     # return from 1st call