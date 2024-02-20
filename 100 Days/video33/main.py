# Python Dictionaries
# Dictionaries are ordered collection of data items. 
# They store multiple items in a single variable. 
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

dic={
    "name":"jay",
    "age":133,
    "drink":"No"
}
# print(type(dic))
print(dic["name"])
print(dic.get("age"))

# only print values
print(dic.values())
# only print keys
print(dic.keys())
# print both key-value pair
print(dic.items())

for key in dic.keys():
  print(f"The value corresponding to the key {key} is {dic[key]}")

print(dic.items())
for key, value in dic.items():
  print(f"The value corresponding to the key {key} is {value}")