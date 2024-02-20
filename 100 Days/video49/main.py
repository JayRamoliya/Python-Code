# FILE IO IN PYTHON
# R MOD= CAN ONLY READ THIS MODE IS DEFAULT
# W MOD = NEW FILE CREAT 
# A MOD = FILE ME APPEND
# T MOD = 
# RB MOD = BINARY MOD MA OPEN KARE

# f=open('video49\jay.txt','r')
# f=open('video49\new.txt','w')
# f=open('new.txt','a')

# print(f)
# text=f.read()
# print(text)


# f.close()

# file writing 
# f2=open("video49\jay.txt",'w')
# f2.write("jay is good person")
# f2.write("jay is good person")
# f2.close()

# file append mod
# f3=open("video49\jay.txt",'a')
# f3.write("jay is good person")
# f3.write("jay is good person")
# f3.close()

with open('video49\jay.txt','a') as f4:
    f4.write("hey i am inside with")
