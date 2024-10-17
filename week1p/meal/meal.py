# main function
def main():
    x = input("What time is it? ")
    time = convert(x)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# convert time to integer


def convert(time):
    time = time.split(":")
    time[0] = int(time[0])
    time[1] = int(time[1])/60
    time = time[0] + time[1]
    return time


# for check50 to work
if __name__ == "__main__":
    main()
