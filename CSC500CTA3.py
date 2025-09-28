# CSC500 Critical Thinking Assignment 3
# Submission by: Anthony LE


def receiptView():
    # Ask user to enter the charge for the food
    # Prompt user for a valid monetary value (positive number)
    while True:
        userInput = input("Please enter the charge for the food: $")
        try:
            # Convert input to float and check if it's positive
            foodCharge = float(userInput)
            if foodCharge >= 0:
                # Input is valid, break out of the loop
                break
            else:
                print("Invalid input. Please enter a positive amount.")
        # Conversion to float failed, prompt for valid input
        except ValueError:
            print("Invalid input. Please enter a valid monetary value (e.g., 12.34).")

    # Calculate tip, tax, and total values
    tip = foodCharge * 0.18
    tax = foodCharge * 0.07
    total = foodCharge + tip + tax

    # Print Output
    print("======================================")
    # Format the charge, tip, tax, and total to two decimal places
    print(f"{'Food Charge:':<20} ${foodCharge:>8.2f}")
    print(f"{'Tip (18%):':<20} ${tip:>8.2f}")
    print(f"{'Sales Tax (7%):':<20} ${tax:>8.2f}")
    print("--------------------------------------")
    print(f"{'TOTAL:':<20} ${total:>8.2f}")
    print("======================================")
    print("        Thank you for dining!         ")
    print("======================================\n")


def militaryTimeAlarm():
    # Ask user to enter the time in 24-hour format (0000 to 2400)
    while True:
        time24h = input(
            "Please enter the time in 24-hour format (e.g., 1300 for 1:00 PM, between 0000 and 2400): "
        )
        # Check if the input is all digits and exactly 4 characters
        if time24h.isdigit() and len(time24h) == 4:
            time24h = int(time24h)
            # Extract hours and minutes from the 4-digit number
            hours = time24h // 100  # Get the first two digits as hours
            minutes = time24h % 100  # Get the last two digits as minutes
            # Validate the range
            # - Hours must be between 0 and 24
            # - Minutes must be between 0 and 59
            if (
                0 <= hours <= 24
                and 0 <= minutes < 60
                and (hours < 24 or (hours == 24 and minutes == 0))
            ):
                # Input is valid, break out of the loop
                break
            else:
                # Input is not a valid military time
                print(
                    "Invalid time. Hours must be 00-24 and minutes 00-59. 2400 is allowed, but not 2460, etc."
                )
        else:
            # Input is not a 4-digit number
            print(
                "Invalid input. Please enter a 4-digit military time between 0000 and 2400."
            )
    # Ask user to enter the number of hours to set the alarm
    while True:
        hoursToAdd = input(
            "Please enter the number of hours to set the alarm (whole hours only): "
        )
        # Validate that the input is a whole number
        if hoursToAdd.isdigit():
            hoursToAdd = int(hoursToAdd)
            # Input is valid, break out of the loop
            break
        else:
            # Input is not a valid whole number
            print("Invalid input. Please enter a whole number (e.g., 2, 5, 10).")

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
