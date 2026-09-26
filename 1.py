# ELECTRICITY BILL CALCULATOR
# Single-file Python Project

consumer_name = ""
consumer_number = ""
connection_type = ""
units_consumed = 0
total_bill = 0


def get_consumer_details():
    global consumer_name, consumer_number, connection_type

    print("\n--- Consumer Details ---")

    consumer_name = input("Enter consumer name: ").strip()

    while True:
        consumer_number = input("Enter consumer number: ").strip()
        if consumer_number:
            break
        print("Consumer number cannot be empty.")

    while True:
        print("\nConnection Type:")
        print("1. Domestic")
        print("2. Commercial")

        choice = input("Enter choice: ")

        if choice == "1":
            connection_type = "Domestic"
            break
        elif choice == "2":
            connection_type = "Commercial"
            break
        else:
            print("Invalid choice. Please try again.")


def calculate_bill():
    global units_consumed, total_bill

    print("\n--- Meter Reading ---")

    while True:
        try:
            previous_reading = float(input("Enter previous meter reading: "))
            current_reading = float(input("Enter current meter reading: "))

            if previous_reading < 0 or current_reading < 0:
                print("Meter readings cannot be negative.")
            elif current_reading < previous_reading:
                print("Current reading cannot be less than previous reading.")
            else:
                break

        except ValueError:
            print("Please enter valid numbers.")

    units_consumed = current_reading - previous_reading

    print("\nUnits consumed:", units_consumed)

    # Domestic tariff
    if connection_type == "Domestic":

        if units_consumed <= 100:
            energy_charge = units_consumed * 3.00

        elif units_consumed <= 200:
            energy_charge = (100 * 3.00) + ((units_consumed - 100) * 4.50)

        elif units_consumed <= 400:
            energy_charge = (100 * 3.00) + (100 * 4.50) + \
                            ((units_consumed - 200) * 6.00)

        else:
            energy_charge = (100 * 3.00) + (100 * 4.50) + \
                            (200 * 6.00) + ((units_consumed - 400) * 7.50)

        fixed_charge = 100

    # Commercial tariff
    else:

        if units_consumed <= 100:
            energy_charge = units_consumed * 5.00

        elif units_consumed <= 200:
            energy_charge = (100 * 5.00) + ((units_consumed - 100) * 6.50)

        elif units_consumed <= 400:
            energy_charge = (100 * 5.00) + (100 * 6.50) + \
                            ((units_consumed - 200) * 7.50)

        else:
            energy_charge = (100 * 5.00) + (100 * 6.50) + \
                            (200 * 7.50) + ((units_consumed - 400) * 9.00)

        fixed_charge = 250

    electricity_duty = energy_charge * 0.05
    surcharge = energy_charge * 0.02

    total_bill = energy_charge + fixed_charge + electricity_duty + surcharge

    print("\n--- Bill Calculation ---")
    print(f"Energy Charge     : ₹{energy_charge:.2f}")
    print(f"Fixed Charge      : ₹{fixed_charge:.2f}")
    print(f"Electricity Duty  : ₹{electricity_duty:.2f}")
    print(f"Surcharge         : ₹{surcharge:.2f}")
    print("-" * 35)
    print(f"Total Bill        : ₹{total_bill:.2f}")


def appliance_estimator():
    print("\n--- Appliance Consumption Estimator ---")

    appliances = []

    while True:
        try:
            count = int(input("How many appliances do you want to add? "))

            if count <= 0:
                print("Enter a number greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    total_units = 0

    for i in range(count):
        print(f"\nAppliance {i + 1}")

        name = input("Enter appliance name: ")

        while True:
            try:
                wattage = float(input("Enter power rating (watts): "))
                hours = float(input("Enter usage per day (hours): "))
                days = int(input("Enter usage days per month: "))

                if wattage <= 0 or hours <= 0 or days <= 0:
                    print("Values must be greater than zero.")
                elif hours > 24:
                    print("Hours per day cannot exceed 24.")
                elif days > 31:
                    print("Days cannot exceed 31.")
                else:
                    break

            except ValueError:
                print("Please enter valid numbers.")

        monthly_units = (wattage * hours * days) / 1000
        total_units += monthly_units

        appliances.append((name, monthly_units))

    print("\n--- Appliance Consumption ---")

    for name, units in appliances:
        print(f"{name}: {units:.2f} units/month")

    print("-" * 35)
    print(f"Total Estimated Consumption: {total_units:.2f} units/month")


def display_bill_summary():
    if not consumer_name:
        print("\nPlease enter consumer details first.")
        return

    if units_consumed == 0:
        print("\nPlease calculate the bill first.")
        return

    print("\n" + "=" * 40)
    print("          ELECTRICITY BILL")
    print("=" * 40)

    print(f"Consumer Name   : {consumer_name}")
    print(f"Consumer Number : {consumer_number}")
    print(f"Connection Type : {connection_type}")
    print(f"Units Consumed  : {units_consumed:.2f}")
    print("-" * 40)
    print(f"Total Amount    : ₹{total_bill:.2f}")
    print("=" * 40)


def main():
    while True:
        print("\n" + "=" * 45)
        print("       ELECTRICITY BILL CALCULATOR")
        print("=" * 45)

        print("1. Enter Consumer Details")
        print("2. Calculate Electricity Bill")
        print("3. Appliance Consumption Estimator")
        print("4. View Bill Summary")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            get_consumer_details()

        elif choice == "2":
            if not consumer_name:
                print("\nPlease enter consumer details first.")
            else:
                calculate_bill()

        elif choice == "3":
            appliance_estimator()

        elif choice == "4":
            display_bill_summary()

        elif choice == "5":
            print("\nThank you for using the Electricity Bill Calculator!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


main()