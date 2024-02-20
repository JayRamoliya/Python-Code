# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. 

import time

# times=time.strftime('%H:%M:%S')
# print(times)

H=int(time.strftime('%H'))
print(H)
# M=int(time.strftime('%M'))
# print(M)
# S=time.strftime('%S')
# print(S)

if(H>=0 and H<12):
    print("good morning")
elif(H>=12 and H<17):
    print("good afternoon")
elif(H>=17 and H<0):
    print("good night")

# and = both true so true
# or = one true so true