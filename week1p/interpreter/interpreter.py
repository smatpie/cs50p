# Take user input
a = input("Expression: ").strip()
a = a.split(" ")
x = int(a[0])
y = (a[1])
z = int(a[2])
# Answer For each condition
match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        if z == 0:
            print("denominator cannot be 0")
        else:
            print(float(x / z))
