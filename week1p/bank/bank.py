# Take user input
x = input("Greeting: ").lower().strip().split(" ")
# Apply Conditions
if "hello" in x[0]:
    print("$0")
elif x[0][0] == "h":
    print("$20")
else:
    print("$100")
