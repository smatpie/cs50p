


def main():
# Ask for their name
    name  = input("What's your name ")

    hello()
    hello(name)



# defining function
def hello(name = "world"):
# spliting names
    first = name.strip().title()
# Say hello to the user
    print(f"hello, {first}")



main()
