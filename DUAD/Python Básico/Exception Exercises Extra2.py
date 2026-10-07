def convert_to_integer(my_list):
    print("Result:")

    for value in my_list:
        try:
            number = int(value)
            print(value, "converted to", number)

        except ValueError:
            print("Could not convert the element:", value)


my_list = ["4", "hello", "10", "5.2"]

convert_to_integer(my_list)