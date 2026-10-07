def sum_values(value_list):
    total = 0

    for value in value_list:
        try:
            number = float(value)
            total += number
            print(number, "added successfully")
        except ValueError:
            print("Invalid value:", value)

    print("Total sum:", total)


data = ["10", "keyboard", "5.5", "3", "error"]

sum_values(data)