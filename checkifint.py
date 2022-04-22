def check():

    while True:
        try:
            v = int(input())
            print(f"{v} is a number")
        except ValueError:
            print(f"Try again")
            continue
        else:
            break

    return v




        