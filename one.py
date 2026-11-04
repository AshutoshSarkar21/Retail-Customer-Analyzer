import csv
from pathlib import Path
from statistics import mean, median


# --------------------------------------------------
# RETAIL CUSTOMER ANALYZER
# --------------------------------------------------

FILE_NAME = Path(__file__).resolve().parent / "customers.csv"

REQUIRED_COLUMNS = [
    "CustomerID",
    "Name",
    "City",
    "Purchases",
    "TotalSpent"
]

# Sample data used to create the CSV file if it is missing
SAMPLE_CUSTOMERS = [
    {
        "CustomerID": "C01",
        "Name": "Asha",
        "City": "Raipur",
        "Purchases": 5,
        "TotalSpent": 12000
    },
    {
        "CustomerID": "C02",
        "Name": "Bhavin",
        "City": "Durg",
        "Purchases": 2,
        "TotalSpent": 3000
    },
    {
        "CustomerID": "C03",
        "Name": "Chitra",
        "City": "Raipur",
        "Purchases": 8,
        "TotalSpent": 25000
    },
    {
        "CustomerID": "C04",
        "Name": "Deepak",
        "City": "Bhilai",
        "Purchases": 1,
        "TotalSpent": 800
    },
    {
        "CustomerID": "C05",
        "Name": "Esha",
        "City": "Durg",
        "Purchases": 4,
        "TotalSpent": 9000
    },
    {
        "CustomerID": "C06",
        "Name": "Farhan",
        "City": "Raipur",
        "Purchases": 3,
        "TotalSpent": 6000
    },
    {
        "CustomerID": "C07",
        "Name": "Gita",
        "City": "Bhilai",
        "Purchases": 6,
        "TotalSpent": 15000
    },
    {
        "CustomerID": "C08",
        "Name": "Hari",
        "City": "Durg",
        "Purchases": 2,
        "TotalSpent": 2200
    }
]


def create_sample_file():
    """Create a sample CSV file if one does not exist."""

    with FILE_NAME.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=REQUIRED_COLUMNS)
        writer.writeheader()
        writer.writerows(SAMPLE_CUSTOMERS)

    print("Sample customer file created successfully!")


def load_customers():
    """Read and validate customer information from CSV."""

    # Create sample data automatically if the file is missing.
    if not FILE_NAME.exists():
        try:
            create_sample_file()
        except OSError as error:
            print("Error creating the CSV file:", error)
            return None

    try:
        with FILE_NAME.open(
            "r", newline="", encoding="utf-8-sig"
        ) as file:

            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Error: The CSV file is empty.")
                return None

            # Check the column names.
            if not all(
                column in reader.fieldnames
                for column in REQUIRED_COLUMNS
            ):
                print("Error: Required columns are missing.")
                print("Required columns:", ", ".join(REQUIRED_COLUMNS))
                return None

            customers = []

            for row_number, row in enumerate(reader, start=2):
                try:
                    customer_id = row["CustomerID"].strip()
                    name = row["Name"].strip()
                    city = row["City"].strip()

                    purchases = int(row["Purchases"])
                    total_spent = float(row["TotalSpent"])

                    if not customer_id or not name or not city:
                        raise ValueError("Customer details cannot be blank.")

                    if purchases < 0 or total_spent < 0:
                        raise ValueError(
                            "Purchases and spending cannot be negative."
                        )

                    customers.append({
                        "CustomerID": customer_id,
                        "Name": name,
                        "City": city,
                        "Purchases": purchases,
                        "TotalSpent": total_spent
                    })

                except (ValueError, TypeError, KeyError) as error:
                    print(
                        f"Error in CSV row {row_number}: {error}"
                    )
                    return None

            if not customers:
                print("Error: No customer records found.")
                return None

            return customers

    except (OSError, csv.Error) as error:
        print("Error reading the CSV file:", error)
        return None


def spending_statistics(customers):
    """Calculate average, median, highest and lowest spending."""

    spending = [
        customer["TotalSpent"]
        for customer in customers
    ]

    average_spending = mean(spending)
    median_spending = median(spending)

    highest = max(customers, key=lambda c: c["TotalSpent"])
    lowest = min(customers, key=lambda c: c["TotalSpent"])

    print("\n========== SPENDING STATISTICS ==========")

    print(f"Total customers: {len(customers)}")
    print(f"Total spending: Rs. {sum(spending):.2f}")
    print(f"Mean spending: Rs. {average_spending:.2f}")
    print(f"Median spending: Rs. {median_spending:.2f}")

    print(
        f"Highest spender: {highest['Name']} "
        f"(Rs. {highest['TotalSpent']:.2f})"
    )

    print(
        f"Lowest spender: {lowest['Name']} "
        f"(Rs. {lowest['TotalSpent']:.2f})"
    )


def high_value_customers(customers):
    """Find customers who meet the spending limit."""

    try:
        limit = float(input("\nEnter the minimum spending limit: "))

        if limit < 0:
            print("Error: The limit cannot be negative.")
            return

    except ValueError:
        print("Error: Please enter a valid number.")
        return

    results = [
        customer for customer in customers
        if customer["TotalSpent"] >= limit
    ]

    print(f"\n========== HIGH-VALUE CUSTOMERS ==========")
    print(f"Minimum spending limit: Rs. {limit:.2f}")
    print(f"Number of matching customers: {len(results)}")

    if not results:
        print("No customers meet this spending limit.")
        return

    for customer in results:
        print(
            f"{customer['CustomerID']} | "
            f"{customer['Name']} | "
            f"{customer['City']} | "
            f"Rs. {customer['TotalSpent']:.2f}"
        )


def city_wise_summary(customers):
    """Calculate total and average spending by city."""

    city_data = {}

    for customer in customers:
        city = customer["City"]
        spending = customer["TotalSpent"]

        if city not in city_data:
            city_data[city] = {
                "total": 0,
                "count": 0
            }

        city_data[city]["total"] += spending
        city_data[city]["count"] += 1

    print("\n========== CITY-WISE SUMMARY ==========")

    sorted_cities = sorted(
        city_data.items(),
        key=lambda item: item[1]["total"],
        reverse=True
    )

    for city, data in sorted_cities:
        total = data["total"]
        count = data["count"]
        average_spending = total / count

        print(f"\nCity: {city}")
        print(f"Number of customers: {count}")
        print(f"Total spending: Rs. {total:.2f}")
        print(f"Average spending: Rs. {average_spending:.2f}")


def show_all_customers(customers):
    """Display all customer records."""

    print("\n========== ALL CUSTOMERS ==========")

    for customer in customers:
        print(
            f"{customer['CustomerID']} | "
            f"{customer['Name']} | "
            f"{customer['City']} | "
            f"Purchases: {customer['Purchases']} | "
            f"Spent: Rs. {customer['TotalSpent']:.2f}"
        )


def main():
    """Display the menu and run the selected operation."""

    customers = load_customers()

    if customers is None:
        print("\nPlease correct the CSV file and run the program again.")
        return

    print("\nCustomer data loaded successfully!")

    while True:
        print("\n==========================================")
        print("       RETAIL CUSTOMER ANALYZER")
        print("==========================================")
        print("1. Spending statistics")
        print("2. Find high-value customers")
        print("3. City-wise spending summary")
        print("4. Display all customers")
        print("5. Exit")
        print("==========================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            spending_statistics(customers)

        elif choice == "2":
            high_value_customers(customers)

        elif choice == "3":
            city_wise_summary(customers)

        elif choice == "4":
            show_all_customers(customers)

        elif choice == "5":
            print("Thank you for using Retail Customer Analyzer!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()