first_value = input("Enter the first value: ")
second_value = input("Enter the second value: ")

if first_value >= second_value:
    print("The values are the equal.")
elif first_value > second_value:
    print(f"First value {first_value} is greater.")
else:
    print(f"Second value {second_value} is greater.")