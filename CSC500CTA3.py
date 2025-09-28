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


# Run the program
if __name__ == "__main__":
    receiptView()
