from msilib.schema import Condition


number=int(input())
num_str=str(number)
mul=((number%11)==0)
onemul=((number%11)==1)
condition=mul or onemul

if condition:
    print('special eleven')
else:
    print('normal number')