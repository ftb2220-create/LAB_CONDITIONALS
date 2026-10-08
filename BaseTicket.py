age:int = int(input("Enter your age: "))
day:str = input("Enter the day: ")
student:str = input("Are you a student? yes or no: ")

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday",]


if day not in days:
    print("Invalid day")
    
if age < 5:
    print("Ticket price: Free")
else:
    if age <= 12:
        price = 6
    elif age <= 59:
        price = 10
    else:
        price = 7

    if day == "friday":
        price += 2
    if student == "yes":
        price *= 0.8

    print(f"Ticket price: ${price:.2f}")
    
print("Thank you for using our ticketing system.")