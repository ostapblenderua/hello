def check(inputtext):

    while True:
        try:

            v = int(input(inputtext))
            print(f"{v} is a number")
        except ValueError:
            print(f"Try again")
            continue
        else:
            break

    return v




        