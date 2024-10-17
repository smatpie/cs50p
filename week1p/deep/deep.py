# Take user input
x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
# Print the output according to conditions
if x in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("no")
