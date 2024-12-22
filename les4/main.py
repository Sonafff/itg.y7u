def input_int(message, min_value, max_value):
    while True:
        try:
            return int(input(message))
            # user_input = input(message)
            # result = int(user_input)
            # return result
        except ValueError:
            print("entered invalid number. Try again.")



a = input_int("enter number", 1 ,10)
b = input_int("enter number", 1 ,10)

while True:

    try:
        a = int(input("1-st number: "))
        b = int(input("2-nd number: "))

        print(f"{a} / {b} = {a / b}")
    except ValueError:
        print("neeeeet.")
    except ZeroDivisionError:
        print("no.")
    except Exception as error:
        print(f"{type(error)}: {error}")

    if input("Try once more? (yes/no): ").lower() == "no":
        break

