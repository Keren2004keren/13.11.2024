# START
power_of_3: dict[int, int] = {num: num ** 3 for num in range(1, 21)}
print(power_of_3)
number: int= int(input("Enter a number: "))
if number in power_of_3:
    print(power_of_3[number])
else:
    print("The number doesn't exist in the dictionary.")

# STOP