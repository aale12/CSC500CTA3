def receiptView():
    # Ask user to enter the charge for the food
    foodCharge = float(input("Please enter the charge for the food: $"))

    # Calculate tip, tax, and total values
    tip = foodCharge * 0.18
    tax = foodCharge * 0.07
    total = foodCharge + tip + tax

    # Print Output

    print("======================================")
    print(f"{'Food Charge:':<20} ${foodCharge:>8.2f}")
    print(f"{'Tip (18%):':<20} ${tip:>8.2f}")
    print(f"{'Sales Tax (7%):':<20} ${tax:>8.2f}")
    print("--------------------------------------")
    print(f"{'TOTAL:':<20} ${total:>8.2f}")
    print("======================================")
    print("        Thank you for dining!         ")
    print("======================================\n")


def militaryTimeAlarm():
    # Ask user to enter the time in 24-hour format
    time24h = int(
        input("Please enter the time in 24-hour format (e.g., 1300 for 1:00 PM): ")
    )
    # Ask user to enter the number of hours to set the alarm
    hoursToAdd = int(input("Please enter the number of hours to set the alarm: "))

    # Calculate the alarm time
    alarmTime = (time24h + (hoursToAdd * 100)) % 2400

    # Print the alarm time
    print(f"The alarm will go off at {alarmTime:04d} hours.")


# Run the program
if __name__ == "__main__":
    # Ask the user which function to run
    while True:
        choice = input(
            "Enter '1' for Receipt View, '2' for Military Time Alarm, or 'q' to quit: "
        )
        if choice == "1":
            receiptView()
        elif choice == "2":
            militaryTimeAlarm()
        elif choice.lower() == "q":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
