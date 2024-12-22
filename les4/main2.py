fruits = ["Apple", "Banana", "Orange", "Peach", "Grape"]

print("List:")
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

while True:
    try:
        index = int(input("Print fruit number: ")) -1
        print(f"You chose: {fruits[index]}")
        break
    except (ValueError):
        print("Error1(неправильное значение)")
    except (IndexError):
        print("Error2(несуществующий номер)")
