# string is immutable

a="!! jay!! !!!!JAY !!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("jay","sneh")) #all jay is change to sneh
print(a.rstrip("!")) # after string is remove

print(a.split(" "))

b="introductioN tO jAy ramoliya"
print(b.capitalize()) #first letter is capitial and baki sab small

print(len(b))
print(len(b.center(50)))

print(a.count("jay"))
print(b.count("a"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
print(str1[4:10])
print(str1.endswith("to",4,10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) # first hoy e ape
print(str1.find("ishh")) # -1 return ape

# print(str1.index("ishh")) # error ape

str1 = "jayramoliya133"
print(str1.isalnum()) #a-z,A-Z,0-9
str1 = "ramoliyajay"
print(str1.isalpha()) #a-z,A-Z

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable()) #ji print thy sake te hoy to true varna false jeseki \n

str1 = "         " #using Spacebar true
print(str1.isspace())
str2 = "  " #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) #upper to lower\ lower to upper

str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) #first letter is capital