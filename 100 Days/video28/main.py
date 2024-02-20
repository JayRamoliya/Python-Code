# STRING FORMATTING IN PYTHON

village="keradi"
name="jay"

letter="hey my name is {} and i am from {}"
print(letter.format(name,village))

letter="hey my name is {1} and i am from {0}"
print(letter.format(village,name))

txt = "For only {price:.2f} dollars!" #2f means 2 point ave
print(txt.format(price = 49))

# SOLUTION
print(f"hey my name is {name} and i from {village}")

print(f"{2 * 30}")

# TYPE IS ALSO STRING

# F STRING SHOW KARVA MATE
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")